import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtCore import  QThreadPool
from PyQt5.QtCore import pyqtSlot
from package.mainwindow import Ui_gui_histo_main
from package.advanced_settings import Ui_advanced_settings
from package.cohort_window import Ui_cohort_settings
import os
import pandas as pd
from deepmed.evaluators.aggregate_stats import AggregateStats
from deepmed.experiment_imports import *
import time
import threading
import multiprocessing


class Mainwindow_con(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_gui_histo_main()
        self.ui.setupUi(self)

        # Events Deeplearn
        
        self.slidmasttab_path_DL = " "  # empty values
        self.patmasttab_path_DL = " "  # empty values
        self.folderpath_DL = " "  # empty values
        self.tilepath_DL = " "  # empty values
        self.advanced_values = [0,0]  # basic values from advanced settings Default NEEDS TO BE SET
        self.subgroup_values_DL = [] # from subgroups
        self.batch_size_DL = self.ui.batch_size_DL.text()
        self.max_tile_num_DL = self.ui.maxTileNum_DL.text()
        self.max_epochs_DL = self.ui.max_epochs_DL.text()
        self.gpu_num_DL = self.ui.GPU_num_DL.text()
        self.mode_DL = "test/train"
        self.validratio_DL = self.ui.validratio_DL.value()
        self.kfolds_DL = self.ui.kfolds_DL.text()
        
        self.targets_DL = self.ui.choosetarg_DL.selectedItems()

        self.threadpool = QtCore.QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.ui.advanced_sets_DL.setEnabled(False) # disable advanced settings for now
        self.ui.slide_masttab_DL.clicked.connect(self.open_slidmasttab)
        self.ui.clini_table_DL.clicked.connect(self.open_patmasttab)
        self.ui.savingpath_DL.clicked.connect(self.open_savingpath)
        self.ui.tilespath_DL.clicked.connect(self.open_tile_path)
        self.ui.run_DL.clicked.connect(self.runDL_click)
        self.ui.reset_DL.clicked.connect(self.resetDL_click)
        self.ui.advanced_sets_DL.clicked.connect(self.open_DL_dialog)
        self.ui.choosemode_DL.currentIndexChanged.connect(self.mode_chosen)
        self.ui.addcohortlist_DL.clicked.connect(self.add_list_clicked_DL)
        self.ui.del_list_DL.clicked.connect(self.delete_list_clicked_DL)
        self.ui.cohortlist_DL.itemClicked.connect(self.changename_DL)
        self.ui.test_dl.clicked.connect(self.testclick_DL)
        self.ui.stop_DL.clicked.connect(self.stopclick_DL)
        self.ui.cohort_click.clicked.connect(self.cohortclick_DL)
        ###########


        # Events Deploy
        
        self.project_dir_deploy = ""  # empty values
        self.batch_size_deploy = self.ui.batchsize_Deploy
        self.max_tile_num_deploy = self.ui.maxtilenum_Deploy
        self.model_path_deploy = ""
        self.slidmasttab_path_deploy = ""  # empty values
        self.patmasttab_path_deploy = " "
        self.choose_tiledir_deploy = ""  # empty values
        self.cohortlist_deploy= []
        self.cohort_name_list_deploy= []
        self.targets_Deploy = self.ui.targetlabels_Deploy.selectedItems()


        self.ui.advanced_Deploy.setEnabled(False) # disable advanced settings for now
        self.ui.projectdir_Deploy.clicked.connect(self.open_project_dir_Deploy)
        self.ui.choose_slidetable_Deploy.clicked.connect(self.open_slidmasttab_Deploy)
        self.ui.choose_tiledir_Deploy.clicked.connect(self.open_tile_dir_Deploy)
        self.ui.choose_model_Deploy.clicked.connect(self.open_model_path_Deploy)
        self.ui.run_Deploy.clicked.connect(self.run_Deploy_click)
        self.ui.reset_Deploy.clicked.connect(self.reset_Deploy_click)
        self.ui.advanced_Deploy.clicked.connect(self.advanced_Deploy_click)
        self.ui.clini_table_Deploy.clicked.connect(self.open_patmasttab_deploy)
        self.ui.addlist_Deploy.clicked.connect(self.add_list_clicked_Deploy)
        self.ui.del_list_deploy.clicked.connect(self.delete_list_clicked_Deploy)
        self.ui.cohortlist_Deploy.itemClicked.connect(self.changename_Deploy)
        self.ui.test_Deploy.clicked.connect(self.testclick_Deploy)
        ###########
        # Events Visualize
        self.ui.nextIm_Vis.clicked.connect(self.count_up)
        self.ui.prevIm_Vis.clicked.connect(self.count_down)
        ###########



    ### DEEP LEARN
    def mode_chosen(self):
        self.ui.kfolds_DL.setEnabled(False)
        self.ui.validratio_DL.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.mode_DL = self.ui.choosemode_DL.currentIndex()
        if self.mode_DL==0:
            print("test/train chosen")
            self.ui.validratio_DL.setEnabled(True)
            self.ui.label_4.setEnabled(True)
        elif self.mode_DL==1:
            print("k-fold crossvalidation chosen")
            self.ui.kfolds_DL.setEnabled(True)
            self.ui.label_5.setEnabled(True)

        else:
            print("unknown mode chosen")

    def open_slidmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData")
        if path != ('', ''):
            self.slidmasttab_path_DL = path[0]
            print(path)

    def open_patmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData","*.xlsx")

        if path != ('', ''):
            self.patmasttab_path_DL = path[0]

        if path[0] != "":
            df = pd.read_excel(path[0])
            print(list(df))
            self.ui.choosetarg_DL.setEnabled(True)
            self.ui.choosetarg_DL.clear()
            self.ui.choosetarg_DL.addItems(list(df))

    def open_savingpath(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.folderpath_DL = path

    def open_tile_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.tilepath_DL = path

    def runDL_click(self):
        def execute_traintest():
            do_experiment(
                        project_dir=self.folderpath_DL,
                        get=get.MultiTarget(
                            get.SimpleRun(),
                            train_cohorts_df=pd.concat([
                                cohort(tile_path, clin_path, slid_path)
                                for tile_path, clin_path, slid_path in cohortlist_DL ]
                            ),
                            target_labels=[str(x.text()) for x in self.ui.choosetarg_DL.selectedItems()],  
                            resample_each_epoch=True,
                            valid_frac=int(self.validratio_DL)/100,
                            na_values=['NA','Not Available', 'Equivocal', 'Not Performed',"unknown","na","Na","nA","NA","x"],
                            ),
                            
                            train=Train(
                                batch_size= int(self.ui.batch_size_DL.text()),
                                max_epochs=int(self.ui.max_epochs_DL.text()),
                                ),
                                devices={'cuda:0': 8},
                        num_concurrent_tasks=0,
                        )
                        

        def execute_Kfold():
            cohorts_df=pd.concat([
                                    cohort(tile_path, clin_path, slid_path)
                                    for tile_path, clin_path, slid_path in cohortlist_DL ]
                                )

            do_experiment(
                        project_dir=self.folderpath_DL,
                        get=get.MultiTarget(    
                        get.Crossval(),
                        get.SimpleRun(),

                        cohorts_df=cohorts_df,
                        target_labels=[str(x.text()) for x in self.ui.choosetarg_DL.selectedItems()],  
                        max_train_tile_num=int(self.max_tile_num_DL),  
                        max_valid_tile_num=128,  #TO DO
                        folds = int(self.kfolds_DL),
                        valid_frac=int(self.validratio_DL)/100,
                        na_values=['NA','Not Available', 'Equivocal', 'Not Performed',"unknown","na","Na","nA","NA","x"],
                        balance=True,   
                        #min_support=5,
                        train=Train(
                            batch_size= int(self.ui.batch_size_DL.text()),
                            max_epochs=int(self.ui.max_epochs_DL.text()),
                            ),
                        ),
                        devices={'cuda:0': 4},
                        num_concurrent_tasks=0,
                        )


        cohortnamelist_DL=[]
        cohortlist_DL=[]

        # Looping through items
        for item_index in range(self.ui.cohortlist_DL.count()):  
                # Getting the data embedded in each item from the listWidget
                item_data = self.ui.cohortlist_DL.item(item_index).data(QtCore.Qt.UserRole)  
                cohortlist_DL.append(item_data)
                # Getting the datatext of each item from the listWidget
                item_text = self.ui.cohortlist_DL.item(item_index).text()  
                cohortnamelist_DL.append(item_text)

        self.validratio_DL =  str(self.ui.validratio_DL.text())[:-1]
        print(self.validratio_DL)
        text = ["",
                "Saved Data: ",
                "",
                "Folder path: " + self.folderpath_DL,
                "PMT path: " + os.path.basename(self.patmasttab_path_DL),
                "SMT path: " + os.path.basename(self.slidmasttab_path_DL),
                "Folder path: " + self.folderpath_DL,
                "Chosen target(s): " + str([str(x.text()) for x in self.ui.choosetarg_DL.selectedItems()]),
                "Max epochs: " + str(self.ui.max_epochs_DL.text()),
                "Batch size: " + str(self.ui.batch_size_DL.text()),
                "Max tile num: " + str(self.ui.maxTileNum_DL.text()),
                "GPU Num: " +str(self.ui.GPU_num_DL.text()),
                "Mode: " +str(self.ui.choosemode_DL.currentText()),
                "validation ratio: " +str(self.ui.validratio_DL.text()),
                "K-folds: " +str(self.ui.kfolds_DL.text()),
                "Tile path: " + self.tilepath_DL,
                "Cohort list"+ str(cohortlist_DL),
                "Cohort Name list"+ str(cohortnamelist_DL),
                "ADVANCED SETTINGS:",
                "GPU num advanced : " + str(self.advanced_values[0]),
                "Binarize quantil advanced: " + str(self.advanced_values[1]),
                "Chosen subgroup: " + str(self.subgroup_values_DL)
                ]

        print(*text, sep='\n')
        

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to run the training?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
        
            if True:
                if self.ui.choosemode_DL.currentText() == 'test/train':
                    self.worker = Worker(execute_traintest) # Any other args, kwargs are passed to the run function
                    # Execute
                    self.threadpool.start(self.worker)
                     

                elif self.ui.choosemode_DL.currentText() == 'k-fold cross validation':
                    self.worker = Worker(execute_Kfold) # Any other args, kwargs are passed to the run function
                    # Execute
                    self.threadpool.start(self.worker)
                
                else:
                    raise ValueError(self.mode_DL)

            """except:
                # if not working raise dialog
                QtWidgets.QMessageBox.critical(self, "Error","Oh no!  \n Something went wrong ")

            finally:
                print("cont'd")"""

    def resetDL_click(self):
        
        
        self.slidmasttab_path_DL = " "
        self.patmasttab_path_DL = " "
        self.folderpath_DL = " "
        self.tilepath_DL = " "
        self.ui.choosetarg_DL.clear()
        self.targets_DL = [str(x.text()) for x in self.ui.choosetarg_DL.selectedItems()]
        self.ui.kfolds_DL.setEnabled(False)
        self.kfolds_DL = self.ui.kfolds_DL.text()
        self.ui.validratio_DL.setEnabled(True)
        self.validratio_DL = self.ui.validratio_DL.value()
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(True)
        self.ui.max_epochs_DL.setProperty("value", 4)  # hardcoded
        self.max_epochs_DL = self.ui.max_epochs_DL.text()
        self.ui.batch_size_DL.setProperty("value", 64)  # hardcoded
        self.batch_size_DL = self.ui.batch_size_DL.text()
        self.ui.maxTileNum_DL.setProperty("value", 20)  # hardcoded
        self.max_tile_num_DL = self.ui.maxTileNum_DL.text()
        self.ui.cohortlist_DL.clear()
        self.ui.GPU_num_DL.setProperty("value", 3)  # hardcoded
        self.gpu_num_DL = self.ui.GPU_num_DL.text()
        self.advanced_values = [0, 0]  # basic values from advanced settings Default NEEDS TO BE SET

    def open_DL_dialog(self):
        """open advanced settings for Deep Learn"""
        my_dialog = Advanced_Sets()
        execval = my_dialog.exec_()
        if execval == True:
            self.advanced_values = my_dialog.save_advanced()  # values from dialog window
        print(self.advanced_values)

    def add_list_clicked_DL(self):

        t1 = "SMT path: " + os.path.basename(self.slidmasttab_path_DL)
        t2 = "PMT path: " + os.path.basename(self.patmasttab_path_DL)
        t3 = "tile path: " + self.tilepath_DL
        text="Do you wont to save this setting?"+"\n\n"+"\n\n"+t1+"\n\n"+t2+"\n\n"+t3
        data=[self.tilepath_DL,self.patmasttab_path_DL,self.slidmasttab_path_DL]

        msgBox=QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            n_items=self.ui.cohortlist_DL.count()+1
            item = QtWidgets.QListWidgetItem(f"Cohort {n_items}")

            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)
            
            # Setting your QListWidgetItem Data  
            item.setData(QtCore.Qt.UserRole, data) 

            self.ui.cohortlist_DL.addItem(item)

    def delete_list_clicked_DL(self):
        self.ui.cohortlist_DL.clear()

    def changename_DL(self):
        item_index = self.ui.cohortlist_DL.currentRow()
        t1,t2,t3=self.ui.cohortlist_DL.item(item_index).data(QtCore.Qt.UserRole)
        t1 = "tile path: " + str(t1)
        t2 = "PMT path: " + str(t2)
        t3 = "SMT path: " + str(t3)
        
        text = "Cohort:" + "cohortname" + "\n\n" + "\n\n" + t1 + "\n\n" + t2 + "\n\n" + t3
        #print(str(self.clicked_cohort_DL))

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        deleteButton = msgBox.addButton("delete cohort",QtWidgets.QMessageBox.ActionRole)
        returnValue = msgBox.exec()
        if deleteButton == msgBox.clickedButton():
            print("delete cohort")
            self.ui.cohortlist_DL.takeItem(self.ui.cohortlist_DL.currentRow())
              
    def testclick_DL(self):

        project_dir='C:/Users/tseibel/Desktop/test/savepath2' 
        tiles_path='C:/Users/tseibel/Desktop/test/BLOCKS_NORM_MACENKO'
        clini_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_CLINI.xlsx'
        slide_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_SLIDE.xlsx'
        target_label=['ER Status By IHC','Cancer Type Detailed', 'Neoplasm Histologic Type Name', 
                    'Fraction Genome Altered']
        cohorts_df = cohort(
                                tiles_path,
                                clini_path,
                                slide_path
                            )

        def Execute_test():
            do_experiment(
                    project_dir=project_dir,
                    get=get.MultiTarget(    
                    
                    get.SimpleRun(),
                    train_cohorts_df=cohorts_df,
                    target_labels=target_label,  
                    max_train_tile_num=500, # how many tiles from each whole slide image (maximum)
                    min_support=8,    # how many patients are required in each category?
                    valid_frac=.2,    # which fraction of patients is used for validation (early stopping)+
                    na_values=['NA','Not Available', 'Equivocal', 'Not Performed',"unknown","na","Na","nA","NA","x"],
                    balance=True,   # weather to balance the training set
                    #min_support=5,
                    train=Train(
                        batch_size= 128,
                        max_epochs=int(self.max_epochs_DL),
                        ),
                    ),
                    devices={'cuda:0': 4},
                    num_concurrent_tasks=0,
                    
                )
                                                
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Do you want to start the pipeline?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            self.ui.stop_DL.setEnabled(True)
            print('OK clicked')
            self.worker = Worker(Execute_test) # Any other args, kwargs are passed to the run function
            # Execute
            self.threadpool.start(self.worker)
        
    def stopclick_DL(self):   
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Do you want to stop the pipeline?\n Progress will be lost.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            #####
            #kill worker, TO DO
            #####
            print("close pipeline")

    def cohortclick_DL(self):
        """open cohort settings for Deep Learn"""
        path = self.patmasttab_path_DL
        my_dialog = Cohort_Sets(path)
        execval = my_dialog.exec_()
        if execval == True:
            self.subgroup_values_DL = my_dialog.save_cohort()  # values from dialog window
            print(self.subgroup_values_DL)


    ### DEPLOY
    def open_project_dir_Deploy(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.project_dir_deploy = path

    def open_patmasttab_deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData", "*.xlsx")

        if path != ('', ''):
            self.patmasttab_path_deploy = path[0]

        if path[0] != "":
            df = pd.read_excel(path[0])
            print(list(df))
            self.ui.targetlabels_Deploy.setEnabled(True)
            self.ui.targetlabels_Deploy.clear()
            self.ui.targetlabels_Deploy.addItems(list(df))

            self.ui.targetlabels2_Deploy.setEnabled(True)
            self.ui.targetlabels2_Deploy.clear()
            self.ui.targetlabels2_Deploy.addItems(list(df))

    def open_slidmasttab_Deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData")
        if path != ('', ''):
            self.slidmasttab_path_deploy = path[0]
            print(path)

    def open_tile_dir_Deploy(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.choose_tiledir_deploy = path

    def open_model_path_Deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/models", "*.pkl")
        if path != ('', ''):
            self.model_path_deploy = path[0]
            print(path)

    def run_Deploy_click(self):
        
        def execute_deploy():
            do_experiment(
                    project_dir=self.project_dir_deploy,
                    get=get.MultiTarget(    
                    get.SimpleRun(),
                    test_cohorts_df = pd.concat([
                                cohort(tile_path, clin_path, slid_path)
                                for tile_path, clin_path, slid_path in self.cohortlist_deploy ]
                            )  ,
                    target_labels = [str(x.text()) for x in self.targets_Deploy],  
                    
                   
                    balance=True,   # weather to balance the training set
                    #min_support=5,
                    train=Load(
                            project_dir=self.project_dir_deploy,
                            training_project_dir=self.model_path_deploy),
                    ),
                    evaluators=[Grouped(auroc), Grouped(p_value)],
                        crossval_evaluators=[AggregateStats(label='fold')],
                        multi_target_evaluators=[AggregateStats(label='target', over=['fold'])],
                )



        cohortnamelist_Deploy=[]
        cohortlist_Deploy=[]

        # Looping through items
        for item_index in range(self.ui.cohortlist_Deploy.count()):  
                # Getting the data embedded in each item from the listWidget
                item_data = self.ui.cohortlist_Deploy.item(item_index).data(QtCore.Qt.UserRole)  
                cohortlist_Deploy.append(item_data)
                # Getting the datatext of each item from the listWidget
                item_text = self.ui.cohortlist_Deploy.item(item_index).text()  
                cohortnamelist_Deploy.append(item_text)

        print("run")
        text = ["Project dir: " + str(self.project_dir_deploy),
                "batch size: " + str(self.ui.batchsize_Deploy.text()),
                "max tile num: " + str(self.ui.maxtilenum_Deploy.text()),
                "SMT path: " + os.path.basename(self.slidmasttab_path_deploy),
                "PMT path: " + os.path.basename(self.patmasttab_path_deploy),
                "tile directory: " + str(self.choose_tiledir_deploy),
                "model path: " + str(self.model_path_deploy),
                "target evaluator" + str("yes"),
                "chosen groups: " + str([str(x.text()) for x in self.ui.targetlabels_Deploy.selectedItems()]),
                "chosen subgroups: " + str([str(x.text()) for x in self.ui.targetlabels2_Deploy.selectedItems()]),
                "cohortlists:" + str(cohortlist_Deploy),
                "cohort name list" + str(cohortnamelist_Deploy),
                ]
        print(*text, sep='\n')

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to run the deploy?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            try:
                self.worker = Worker(execute_deploy) # Any other args, kwargs are passed to the run function
                # Execute
                self.threadpool.start(self.worker)
                
                
            except:
                # if not working raise dialog
                QtWidgets.QMessageBox.critical(self, "Error", "Oh no!  \n Something went wrong ")

            finally:
                print("cont'd")

    def reset_Deploy_click(self):
        self.cohort_path_deploy = ""
        self.tile_dir_deploy = ""
        self.model_path_deploy = ""
        self.project_dir_deploy = ""
        self.ui.targetlabels_Deploy.clear()
        self.ui.targetlabels2_Deploy.clear()
        self.ui.batchsize_Deploy.setProperty("value",64) #hardcoded
        self.cohortlist_deploy = []
        self.cohort_name_list_deploy= []
        print("reset")

    def advanced_Deploy_click(self):
        print("advanced settings")
        #still empty

    def add_list_clicked_Deploy(self):

        t1 = "SMT path: " + os.path.basename(self.slidmasttab_path_deploy)
        t2 = "PMT path: " + os.path.basename(self.patmasttab_path_deploy)
        t3 = "tile directory: " + str(self.choose_tiledir_deploy)
        text="Do you wont to save this setting?"+"\n\n"+"\n\n"+t1+"\n\n"+t2+"\n\n"+t3
        data=[self.choose_tiledir_deploy,self.patmasttab_path_deploy,self.slidmasttab_path_deploy]

        msgBox=QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            n_items=self.ui.cohortlist_Deploy.count()+1
            item = QtWidgets.QListWidgetItem(f"Cohort {n_items}")

            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)
            
            # Setting your QListWidgetItem Data  
            item.setData(QtCore.Qt.UserRole, data) 

            self.ui.cohortlist_Deploy.addItem(item)

    def delete_list_clicked_Deploy(self):
        self.ui.cohortlist_Deploy.clear()

    def changename_Deploy(self):
        item_index = self.ui.cohortlist_Deploy.currentRow()
        t1,t2,t3=self.ui.cohortlist_Deploy.item(item_index).data(QtCore.Qt.UserRole)
        t1 = "Tile path: " + str(t1)
        t2 = "PMT path: " + str(t2)
        t3 = "SMT path: " + str(t3)
        
        text = "Cohort:" + "cohortname" + "\n\n" + "\n\n" + t1 + "\n\n" + t2 + "\n\n" + t3
        

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        deleteButton = msgBox.addButton("delete cohort",QtWidgets.QMessageBox.ActionRole)
        returnValue = msgBox.exec()
        if deleteButton == msgBox.clickedButton():
            print("delete cohort")
            self.ui.cohortlist_Deploy.takeItem(self.ui.cohortlist_Deploy.currentRow())

    def testclick_Deploy(self):
         
        project_dir='C:/Users/tseibel/Desktop/test/testbuttonbenchmark' 
        

        def Execute_test():
            do_experiment(
                    project_dir=project_dir,
                    get=get.MultiTarget(    
                    get.SimpleRun(),
                    test_cohorts_df = cohort(
                    tiles_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-TESTSET-DEEPMED-TILES/BLOCKS_NORM_MACENKO',
                    clini_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_CLINI.xlsx',
                    slide_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_SLIDE.xlsx')  ,
                    target_labels =['ER Status By IHC','Cancer Type Detailed', 'Neoplasm Histologic Type Name', 
                    'Fraction Genome Altered'],  
                    na_values=['NA','Not Available', 'Equivocal', 'Not Performed'],
                   
                    balance=True,   # weather to balance the training set
                    #min_support=5,
                    evaluators=[Grouped(auroc), Grouped(p_value)],
                       
                        multi_target_evaluators=[AggregateStats(label='target')],
                    train=Load(
                            project_dir=self.project_dir_deploy,
                            training_project_dir=self.model_path_deploy),
                    ),
                    
                )


        def Execute_test2():
            project_dir2='C:/Users/tseibel/Desktop/test/savepath1' 
            do_experiment(
                    project_dir=project_dir2,
                    get=get.MultiTarget(    
                    get.SimpleRun(),
                    test_cohorts_df = cohort(
                    tiles_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-TESTSET-DEEPMED-TILES/BLOCKS_NORM_MACENKO',
                    clini_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_CLINI.xlsx',
                    slide_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_SLIDE.xlsx')  ,
                    target_labels =['ER Status By IHC'],  
                    na_values=['NA','Not Available', 'Equivocal', 'Not Performed'],
                   
                    balance=True,   # weather to balance the training set
                    #min_support=5,
                    evaluators=[Grouped(auroc), Grouped(p_value)],
                       
                        
                    train=Load(
                            project_dir='C:/Users/tseibel/Desktop/test/savepath1',
                            training_project_dir='C:/Users/tseibel/Desktop/test/savepath1'),
                    ),
                    
                )

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Do you want to start the deployment?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            
            print('OK clicked')
            self.worker = Worker(Execute_test2) # Any other args, kwargs are passed to the run function
            # Execute
            self.threadpool.start(self.worker)
                 








    ###Visualize
    def count_up(self):
        n=self.ui.imgcounter_Vis.intValue()
        self.ui.imgcounter_Vis.display(n+1)

    def count_down(self):
        n=self.ui.imgcounter_Vis.intValue()
        if n>0:
            self.ui.imgcounter_Vis.display(n-1)



class Advanced_Sets(QtWidgets.QDialog):
    """"advanced settings dialog for Deep Learn"""

    def __init__(self, parent=None):
        super(Advanced_Sets, self).__init__(parent)
        self.ui = Ui_advanced_settings()
        self.ui.setupUi(self)

        self.ui.cancel_advancedDL.clicked.connect(self.close)
        self.ui.save_advancedDL.clicked.connect(self.accept)
        self.ui.reset_advancedDL.clicked.connect(self.reset_advanced)

    def save_advanced(self):
        print("Save...")
        a = str(self.ui.GPUnum.text())
        b = str(self.ui.binarize_quantile.value())

        return [a, b]

    def reset_advanced(self):
        self.ui.GPUnum.setProperty("value", 4)
        self.ui.binarize_quantile.setProperty("value", 14)

class Cohort_Sets(QtWidgets.QDialog):
    """"cohort settings dialog for Deep Learn"""

    def __init__(self,path, parent=None):
        super(Cohort_Sets, self).__init__(parent)

        self.ui = Ui_cohort_settings()
        self.ui.setupUi(self)
        self.path = path
        #Values
        self.text = []
        self.groupname = ""
        self.subgroupname = ""
       
        self.path = 'cliniData/TCGA-BRCA-DX_CLINI.xlsx'
        try:
            self.df = pd.read_excel(self.path)
            self.ui.groups.setEnabled(True)
            self.ui.groups.clear()
            self.ui.groups.addItems(list(self.df))
        except:
            QtWidgets.QMessageBox.critical(self, "Error", "problem with the   \n clinitable ")
        finally:
            print("cont'd")

        self.ui.subgroups.setEnabled(False)
        self.ui.and_button.setEnabled(False)
        self.ui.or_button.setEnabled(False)
        self.ui.back_button.setEnabled(False)
        self.ui.min_label.setEnabled(False)
        self.ui.max_label.setEnabled(False)
        self.ui.median_label.setEnabled(False)


        #Events
        self.ui.and_button.clicked.connect(self.and_clicked)
        self.ui.back_button.clicked.connect(self.back_clicked)
        self.ui.or_button.clicked.connect(self.or_clicked)
        self.ui.save_button.clicked.connect(self.accept)
        
        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.groups.activated.connect(self.groups_clicked)
        self.ui.subgroups.activated.connect(self.subgroup_clicked)
    
    def and_clicked(self):
        self.ui.subgroups.clear()
        self.ui.subgroups.setEnabled(False)
        #self.ui.and_button.setEnabled(False)
        #self.ui.or_button.setEnabled(False)
        #self.ui.back_button.setEnabled(False)
        
        self.text.append(self.groupname + self.subgroupname)
        self.text.append(" AND ")
        self.ui.querybox.setText(''.join(self.text))

        self.groupname = ""
        self.subgroupname = ""
        

    def back_clicked(self):
        if len(self.text)>1 and  self.groupname == "":
            self.text=self.text[0:-1]
        elif len(self.text)==1 and  self.groupname == "":
            self.text=[]
        self.groupname = ""
        self.subgroupname = ""
        self.ui.querybox.setText(''.join(self.text))

    def or_clicked(self):
        self.ui.subgroups.clear()
        self.ui.subgroups.setEnabled(False)
        #self.ui.and_button.setEnabled(False)
        #self.ui.or_button.setEnabled(False)
        #self.ui.back_button.setEnabled(False)
        
        self.text.append(self.groupname + self.subgroupname)
        self.text.append(" OR ")
        self.ui.querybox.setText(''.join(self.text))
        
        self.groupname = ""
        self.subgroupname = ""


    def save_cohort(self):
        print(self.groupname)
        if self.groupname !="":
            self.text.append(self.groupname + self.subgroupname)
            self.ui.querybox.setText(''.join(self.text))
        else:#last item in list is either AND or OR operator
            
            self.text=self.text[:-1]

        self.groupname = ""
        self.subgroupname = ""
        print("Save...")
        
        return self.text

    

    def groups_clicked(self):
        print(self.ui.groups.currentText())
        

        
        
        self.ui.min_label.setEnabled(False)
        self.ui.max_label.setEnabled(False)
        self.ui.median_label.setEnabled(False)
        
        self.ui.subgroups.clear()
        self.ui.subgroups.setEnabled(False)
        #self.ui.and_button.setEnabled(True)
        #self.ui.or_button.setEnabled(True)
        #self.ui.back_button.setEnabled(True)
        self.subgroupname = ""
        self.groupname = self.ui.groups.currentText()
        addText = "<span style=\" font-size:8pt; font-weight:400; color:#0000ff;\" >"+self.groupname+"</span>"
        self.ui.querybox.setText(''.join(self.text) + addText  )
        self.ui.querybox.setText(''.join(self.text) + addText  )


        if self.df[self.ui.groups.currentText()].dtype == float:

            print("float")
            """
            min = self.df[self.ui.groups.currentText()].min()
            max = self.df[self.ui.groups.currentText()].max()
            median = self.df[self.ui.groups.currentText()].median()

            
            self.ui.min_label.setEnabled(True)
            self.ui.max_label.setEnabled(True)
            self.ui.median_label.setEnabled(True)
            self.ui.median_label.setText(str(median))
            self.ui.min_label.setText(str(min))
            self.ui.max_label.setText(str(max))
            """
        else:
            subgroup_cat = pd.Categorical(self.df[self.ui.groups.currentText()])
            self.ui.subgroups.setEnabled(True)
            self.ui.subgroups.addItem("-no subgrouping-")
            self.ui.subgroups.addItems([str(val) for val in subgroup_cat.categories])


    def subgroup_clicked(self):
        #self.ui.and_button.setEnabled(True)
        #self.ui.or_button.setEnabled(True)
        #self.ui.back_button.setEnabled(True)

        self.subgroupname = "[" + self.ui.subgroups.currentText() + "]"
        

        if self.ui.subgroups.currentText() !=  "-no subgrouping-":
            addText =self.groupname + self.subgroupname
            
        else:
            addText =self.groupname 

        addText = "<span style=\" font-size:8pt; font-weight:400; color:#0000ff;\" >"+ addText +"</span>"
        self.ui.querybox.setText(''.join(self.text) + addText  )
        

##

class Worker(QtCore.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)


#####
# end


"""
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

def testbutton_click(self):
    
    codename = self.ui.projectname.text() + "-generated"

    text = {"ProjectName": self.ui.projectname.text(), "folderName": {"Temp": self.folderpath_path},
            "codename": codename, "allTargets": [str(x.text()) for x in self.ui.choosetarg.selectedItems()]}
    a = os.path.exists("experiments/" + codename + ".txt")
    if a == True:
        QtWidgets.QMessageBox.critical(self, "File already exists",
                                       "File already exists  \n please choose another projectname")

    else:
        # "no experiment file with same name, can safe text as "experiments/"+codename+".txt" in folder
        filename = "experiments/" + codename + ".txt"
        text = str(text).replace(" ", "")
        text = text.replace("\'", "\"")
        f = open(filename, "w")
        f.write(text)
        f.close()


def plotter(self):

    scene = QtWidgets.QGraphicsScene()
    plt.style.use('classic')
    figure = Figure()
    axes = figure.gca()
    axes.set_title("Training Plot")
    x = np.linspace(0, 20, 100)
    y = 0.9 - np.exp(-x) + 0.03 * np.random.random(len(x))
    y2 = 0.7 - np.exp(-x) + 0.01 * np.random.random(len(x))
    axes.plot(x, y, label="train")
    axes.plot(x, y2, "-.", label="test")
    axes.set_xlabel("epochs")

    axes.grid()
    axes.legend()
    canvas = FigureCanvas(figure)
    canvas.setGeometry(0, 0, 440, 500)
    scene.addWidget(canvas)

        self.ui.graph_autoDL.setScene(scene)
        self.ui.graph_autoDL.show()
"""

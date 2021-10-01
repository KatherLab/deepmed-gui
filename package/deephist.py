import sys
from PyQt5 import QtWidgets,QtCore
from package.mainwindow import Ui_gui_histo_main
from package.advanced_settings import Ui_advanced_settings
import os
import pandas as pd
#from deepmed.evaluators.aggregate_stats import AggregateStats
#from deepmed.experiment_imports import *






class Mainwindow_con(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_gui_histo_main()
        self.ui.setupUi(self)

        # Events Deeplearn
        self.projectname_DL = self.ui.project_name_DL.text()
        self.slidmasttab_path_DL = " "  # empty values
        self.patmasttab_path_DL = " "  # empty values
        self.folderpath_path_DL = " "  # empty values
        self.tilepath_DL = " "  # empty values
        self.advanced_values = [0, 0]  # basic values from advanced settings Default NEEDS TO BE SET

        self.batch_size_DL = self.ui.batch_size_DL.text()
        self.max_tile_num_DL = self.ui.maxTileNum_DL.text()
        self.max_epochs_DL = self.ui.max_epochs_DL.text()
        self.gpu_num_DL = self.ui.GPU_num_DL.text()
        self.mode_DL = "test/train chosen"
        self.traintestratio_DL = self.ui.traintestratio_DL.value()
        self.kfolds_DL = self.ui.kfolds_DL.text()
        self.cohortlist_DL = []
        self.targets_DL = self.ui.choosetarg_DL.selectedItems()




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
        self.ui.cohort_list_DL.itemClicked.connect(self.changename_DL)
        self.clicked_cohort_DL = self.ui.cohort_list_DL
        self.ui.test_dl.clicked.connect(self.testclick_DL)

        ###########


        # Events Deploy
        self.slidmasttab_path_deploy = ""  # empty values
        self.choose_tiledir_deploy = ""  # empty values
        self.model_path_deploy = ""  # empty values
        self.project_dir_open = ""  # empty values
        self.patmasttab_path_deploy = " "  # empty values
        self.cohortlist_deploy= []

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
        ###########
        # Events Visualize
        self.ui.nextIm_Vis.clicked.connect(self.count_up)
        self.ui.prevIm_Vis.clicked.connect(self.count_down)
        ###########



    ### DEEP LEARN
    def mode_chosen(self):
        self.ui.kfolds_DL.setEnabled(False)
        self.ui.traintestratio_DL.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.mode_DL = self.ui.choosemode_DL.currentIndex()
        if self.mode_DL==0:
            print("test/train chosen")
            self.ui.traintestratio_DL.setEnabled(True)
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
            self.folderpath_path_DL = path

    def open_tile_path(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.tilepath_DL = path



    def runDL_click(self):

        text = ["Projectname: " + self.projectname_DL,
                "SMT path: " + os.path.basename(self.slidmasttab_path_DL),
                "PMT path: " + os.path.basename(self.patmasttab_path_DL),
                "Folder path: " + self.folderpath_path_DL,
                "Chosen target(s): " + str([str(x.text()) for x in self.targets_DL]),
                "Max epochs: " + str(self.max_epochs_DL),
                "Batch size: " + str(self.batch_size_DL),
                "Max tile num: " + str(self.max_tile_num_DL),
                "GPU Num: " +str(self.gpu_num_DL),
                "Mode: " +str(self.mode_DL),
                "Train/test ratio: " +str(self.traintestratio_DL),
                "K-folds: " +str(self.kfolds_DL),
                "Tile path: " + self.tilepath_DL,
                "Cohort list"+ str(self.cohortlist_DL),
                "ADVANCED SETTINGS:",
                "GPU num: " + str(self.advanced_values[0]),
                "Binarize quantil: " + str(self.advanced_values[1]),
                ]

        print(*text, sep='\n')

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to run the training?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            if self.mode_DL == 'test/train':
                    do_experiment(
                        project_dir=self.projectname_DL,
                        get=get.MultiTarget(
                            get.SimpleRun(),
                            train_cohorts_df=pd.concat([
                                cohort(tiles_path, clini_path, slide_path)
                                for tiles_path, clini_path, slide_path in self.cohortlist_DL]
                            ),
                            target_labels=[str(x.text()) for x in self.targets_DL],
                            resample_each_epoch=True,
                            valid_frac=self.traintestratio_DL/100
                        )
                    )
                    
            try:
                if self.mode_DL == 'test/train':
                    do_experiment(
                        project_dir=self.projectname_DL,
                        get=get.MultiTarget(
                            get.SimpleRun(),
                            train_cohorts_df=pd.concat([
                                cohort(tiles_path, clini_path, slide_path)
                                for tiles_path, clini_path, slide_path in self.cohortlist_DL]
                            ),
                            target_labels=[str(x.text()) for x in self.targets_DL],
                            resample_each_epoch=True,
                            valid_frac=self.traintestratio_DL / 100
                        )
                    )
                elif self.mode_DL == 'k-fold cross validation':
                    do_experiment(
                        project_dir=self.projectname_DL,
                        get=get.MultiTarget(
                            get.Crossval(),
                            get.SimpleRun(),
                            cohorts_df=pd.concat(
                                cohort(tiles_path, clini_path, slide_path)
                                for tiles_path, clini_path, slide_path in self.cohortlist_DL
                            ),
                            folds=int(self.kfolds_DL),
                            target_labels=[str(x.text()) for x in self.targets_DL],
                            resample_each_epoch=True,
                            valid_frac=self.traintestratio_DL/100,
                        )
                    )
                else:
                    raise ValueError(self.mode_DL)

            except:
                # if not working raise dialog
                QtWidgets.QMessageBox.critical(self, "Error","Oh no!  \n Something went wrong ")

            finally:
                print("cont'd")

    def resetDL_click(self):
        self.ui.project_name_DL.clear()
        self.projectname_DL = self.ui.project_name_DL.text()
        self.slidmasttab_path_DL = " "
        self.patmasttab_path_DL = " "
        self.folderpath_path_DL = " "
        self.ui.choosetarg_DL.clear()
        self.targets_DL = self.ui.choosetarg_DL.selectedItems()
        self.ui.kfolds_DL.setEnabled(False)
        self.kfolds_DL = self.ui.kfolds_DL.text()
        self.ui.traintestratio_DL.setEnabled(True)
        self.traintestratio_DL = self.ui.traintestratio_DL.value()
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(True)
        self.ui.max_epochs_DL.setProperty("value", 4)  # hardcoded
        self.max_epochs_DL = self.ui.max_epochs_DL.text()
        self.ui.batch_size_DL.setProperty("value", 0)  # hardcoded
        self.batch_size_DL = self.ui.batch_size_DL.text()
        self.ui.maxTileNum_DL.setProperty("value", 0)  # hardcoded
        self.max_tile_num_DL = self.ui.maxTileNum_DL.text()
        self.ui.cohort_list_DL.clear()
        self.cohortlist = []
        self.ui.GPU_num_DL.setProperty("value", 3)  # hardcoded
        self.gpu_num_DL = self.ui.GPU_num_DL.text()
        self.advanced_values = [0, 0]  # basic values from advanced settings Default NEEDS TO BE SET



    def open_DL_dialog(self):
        """open advanced settings for Deep Learn"""
        my_dialog = MyDialog()
        execval = my_dialog.exec_()
        if execval == True:
            self.advanced_values = my_dialog.save_advanced()  # values from dialog window
        print(self.advanced_values)

    def add_list_clicked_DL(self):

        t1 = "SMT path: " + os.path.basename(self.slidmasttab_path_DL)
        t2 = "PMT path: " + os.path.basename(self.patmasttab_path_DL)
        t3 = "tile path: " + self.tilepath_DL
        text="Do you wont to save this setting?"+"\n\n"+"\n\n"+t1+"\n\n"+t2+"\n\n"+t3


        msgBox=QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            n_items=self.ui.cohort_list_DL.count()+1
            item = QtWidgets.QListWidgetItem(f"Cohort {n_items}")

            item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)

            self.ui.cohort_list_DL.addItem(item)



            #self.ui.cohort_list_DL.addItem(f"Cohort {n_items}")

            self.cohortlist_DL.append([self.tilepath_DL,self.patmasttab_path_DL,self.slidmasttab_path_DL])
    def delete_list_clicked_DL(self):
        self.ui.cohort_list_DL.clear()

    def changename_DL(self):
        i=0
        t1,t2,t3 = self.cohortlist_DL[i]
        t1 = "SMT path: " + str(t1)
        t2 = "PMT path: " + str(t2)
        t3 = "tile path: " + str(t3)
        text = "Cohort:" + "cohortname" + "\n\n" + "\n\n" + t1 + "\n\n" + t2 + "\n\n" + t3
        print(str(self.clicked_cohort_DL))

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        msgBox.addButton("delete cohort",QtWidgets.QMessageBox.ActionRole)
        returnValue = msgBox.exec()

    def testclick_DL(self):
    
        if True:
            project_dir='C:/Users/tseibel/Desktop/test/savepath',  # define the output directory
            tiles_path='C:/Users/tseibel/Desktop/test/BLOCKS_NORM_MACENKO'
            clini_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_CLINI.xlsx'
            slide_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_SLIDE.xlsx'
            target_label=['ER Status By IHC']
            if self.ui.choosemode_DL.currentText() == 'test/train':
                    do_experiment(
                        project_dir=self.ui.project_name_DL.text(),
                        get=get.MultiTarget(
                            get.SimpleRun(),
                            train_cohorts_df=pd.concat([
                                cohort(tile_path, clin_path, slid_path)
                                for tile_path, clin_path, slid_path in [[tiles_path,clini_path,slide_path]] ]
                            ),
                            target_labels= target_label,  #[str(x.text()) for x in self.ui.choosetarg_DL.selectedItems()],
                            resample_each_epoch=True,
                            valid_frac=self.ui.traintestratio_DL.value()/100
                        )
                    )
        
        if False:
            do_experiment(

                

        
                                
                                
                get=partial(
                    get.MultiTarget,
                    get.Crossval,
                    get.SimpleRun,
                    # define where the tiles and tables are located
                    
                    cohorts_df=cohort(
                        tiles_path='C:/Users/tseibel/Desktop/test/BLOCKS_NORM_MACENKO',
                        clini_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_CLINI.xlsx',
                        slide_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_SLIDE.xlsx'),
                    # now choose a binary categorical, a multiclass categorical and a continuous target
                    # the continuous target will be binarized at the median
                    target_labels=['ER Status By IHC', 'Cancer Type Detailed', 'Neoplasm Histologic Type Name', \
                                   'Fraction Genome Altered'],
                    max_train_tile_num=500,  # how many tiles from each whole slide image? (maximum)
                    min_support=8,  # how many patients are required in each category?
                    valid_frac=.2,  # which fraction of patients is used for validation (early stopping)+
                    # now define all the values which will be excluded (set to missing)
                    na_values=['NA', 'Not Available', 'Equivocal', 'Not Performed', 'Other, specify'],
                    multi_target_evaluators=[partial(AggregateStats, group_levels=[-3, -1])],  # group_levels=[-3, -1]
                    crossval_evaluators=[AggregateStats, Grouped(Roc), TopTiles],
                    # partial(AggregateStats, group_levels=[-1,-3])

                    # define all the output statistics, can be on the level of tiles, slides or patients
                    # crossval_evaluators=[AggregateStats, Grouped(Roc), TopTiles],
                    evaluators=[Grouped(auroc), Grouped(count), TopTiles, Grouped(p_value)],
                    Train=partial(
                        Train,
                        batch_size=128,  # mini batch size, can be larger if GPU RAM is larger
                        max_epochs=20,  # maximum number of epochs if no early stopping
                        tfms=aug_transforms(size=224),  # additional transforms defined in fastai
                    )
                ),

                # num_concurrent_tasks=0,

                # devices = {'cuda:0': 4}, # which cuda device to use and how many threads per device
            )



    ### DEPLOY
    def open_project_dir_Deploy(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.project_dir_open = path

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
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData", "*.csv")
        if path != ('', ''):
            self.slidmasttab_path_deploy = path[0]
            print(path)

    def open_tile_dir_Deploy(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.choose_tiledir_deploy = path

    def open_model_path_Deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/models", "*.csv")
        if path != ('', ''):
            self.model_path_deploy = path[0]
            print(path)

    def run_Deploy_click(self):
        print("run")
        text = ["Project dir: " + str(self.project_dir_open),
                "batch size: " + str(self.ui.batchsize_Deploy.text()),
                "max tile num: " + str(self.ui.maxtilenum_Deploy.text()),
                "SMT path: " + os.path.basename(self.slidmasttab_path_deploy),
                "PMT path: " + os.path.basename(self.patmasttab_path_deploy),
                "tile directory: " + str(self.choose_tiledir_deploy),
                "model path: " + str(self.model_path_deploy),
                "target evaluator" + str("yes"),
                "chosen groups: " + str([str(x.text()) for x in self.ui.targetlabels_Deploy.selectedItems()]),
                "chosen subgroups: " + str([str(x.text()) for x in self.ui.targetlabels2_Deploy.selectedItems()]),
                "cohortlists:" + str(self.cohortlist_deploy),
                ]
        print(*text, sep='\n')

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to run the deploy?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            try:
                do_experiment(
                    project_dir=self.project_dir_open,
                    get=get.MultiTarget(
                        get.SimpleRun(),
                        test_cohorts_df=pd.concat(
                            cohort(tiles_path, clini_path, slide_path)
                            for slide_path, clini_path, tiles_path in self.cohortlist_deploy
                        ),
                        target_labels=[str(x.text()) for x in self.ui.targetlabels_Deploy.selectedItems()],
                        train=Load(
                            project_dir=self.project_dir_open,
                            training_project_dir=self.model_path_deploy),
                        evaluators=[Grouped(auroc), Grouped(p_value)],
                        crossval_evaluators=[AggregateStats(label='fold')],
                        multi_target_evaluators=[AggregateStats(label='target', over=['fold'])]
                    )
                )
            except:
                # if not working raise dialog
                QtWidgets.QMessageBox.critical(self, "Error", "Oh no!  \n Something went wrong ")

            finally:
                print("cont'd")



    def reset_Deploy_click(self):
        self.cohort_path_deploy = ""
        self.tile_dir_deploy = ""
        self.model_path_deploy = ""
        self.project_dir_open = ""
        self.ui.targetlabels_Deploy.clear()
        self.ui.targetlabels2_Deploy.clear()
        self.ui.batchsize_Deploy.setProperty("value",64) #hardcoded
        self.cohortlist_deploy = []

        print("reset")
    def advanced_Deploy_click(self):
        print("advanced settings")
        #still empty

    def add_list_clicked_Deploy(self):

        t1 = "SMT path: " + os.path.basename(self.slidmasttab_path_deploy)
        t2 = "PMT path: " + os.path.basename(self.patmasttab_path_deploy)
        t3 = "tile directory: " + str(self.choose_tiledir_deploy)
        text="Do you wont to save this setting?"+"\n\n"+"\n\n"+t1+"\n\n"+t2+"\n\n"+t3
        msgBox=QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            n_items=self.ui.cohortlist_Deploy.count()+1
            self.ui.cohortlist_Deploy.addItem(f"Cohort {n_items}")
            self.cohortlist_deploy.append([os.path.basename(self.slidmasttab_path_deploy),os.path.basename(self.patmasttab_path_deploy),str(self.choose_tiledir_deploy)])
    def delete_list_clicked_Deploy(self):
        self.ui.cohortlist_Deploy.clear()
    ###Visualize
    def count_up(self):
        n=self.ui.imgcounter_Vis.intValue()
        self.ui.imgcounter_Vis.display(n+1)

    def count_down(self):
        n=self.ui.imgcounter_Vis.intValue()
        if n>0:
            self.ui.imgcounter_Vis.display(n-1)


class MyDialog(QtWidgets.QDialog):
    """"advanced settings dialog for Deep Learn"""

    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
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



app = QtWidgets.QApplication(sys.argv)
widget = Mainwindow_con()
widget.show()

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

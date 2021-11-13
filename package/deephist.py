import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QThreadPool
from PyQt5.QtCore import pyqtSlot
from package.mainwindow import Ui_gui_histo_main
from package.advanced_settings import Ui_advanced_settings
from package.cohort_window import Ui_cohort_settings
from package.add_target import Ui_add_target
from fastai.vision.all import *

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

        # Values Deep Learn
        self.slidmasttab_path_learn = " "  # path for slide table
        self.patmasttab_path_learn = " "  # path for clini table
        self.folderpath_learn = " "  # path for saving path, where the project should be saved
        self.tilepath_learn = " "  # path for tiles
        #self.advanced_values_learn = [3, 10, 100, 50, 0, 4, ['NA', 'Not Available', 'Equivocal', 'Not Performed', 'unknown']]  # HARDCODED returned values from advanced settings. # TODO delete if not needed anymore
        self.advanced_values_learn = 0  # advanced settings.
        self.subgroup_values_learn = ["",""]  # [group,subgroup]
        self.get_adv_settings()  # if self.advanced_values_learn = 0 fetches values from advanced ui

        self.mode_learn = self.ui.choosemode_learn.currentText()  # chosen mode, either test/train or k-fold cross validation
        self.validratio_learn = self.ui.validratio_learn.value()  # for test/train the ratio for the size of test set XX %
        self.kfolds_learn = self.ui.kfolds_learn.text()  # number of folds
        self.targets_learn = self.ui.choosetarg_learn.selectedItems()  # chosen targets

        self.threadpool = QtCore.QThreadPool()  # get number of threads
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        # Events  Deep Learn
        self.ui.slide_masttab_learn.clicked.connect(self.open_slidmasttab_learn)
        self.ui.clini_table_learn.clicked.connect(self.open_patmasttab_learn)
        self.ui.savingpath_learn.clicked.connect(self.open_savingpath_learn)
        self.ui.tilespath_learn.clicked.connect(self.open_tile_path_learn)
        self.ui.run_learn.clicked.connect(self.run_click_learn)
        self.ui.reset_learn.clicked.connect(self.reset_click_learn)
        self.ui.advanced_sets_learn.clicked.connect(self.open_advanced_dialog_learn)
        self.ui.choosemode_learn.currentIndexChanged.connect(self.mode_chosen_learn)
        self.ui.addcohortlist_learn.clicked.connect(self.add_list_clicked_learn)
        self.ui.del_list_learn.clicked.connect(self.delete_list_clicked_learn)
        self.ui.cohortlist_learn.itemClicked.connect(self.changename_learn)
        self.ui.test_learn.clicked.connect(self.testclick_learn)
        self.ui.stop_learn.clicked.connect(self.stop_clicked_learn)
        self.ui.cohort_click_learn.clicked.connect(self.subgrouping_clicked_learn)  # TODO subgrouping has to be fixed
        self.ui.add_target_learn.clicked.connect(self.add_target_clicked_learn)
        ###########

        # Values Deploy
        self.project_dir_deploy = ""  # path for project directory
        self.batch_size_deploy = self.batch_size_learn  #
        self.max_tile_num_deploy = self.max_tile_num_learn  #
        self.model_path_deploy = ""  # path for the model
        self.slidmasttab_path_deploy = ""  # path for slide table
        self.patmasttab_path_deploy = " "  # path for clini table
        self.choose_tile_dir_deploy = ""  # empty values
        self.cohortlist_deploy = []  # list of chosen cohorts, each cohort is a list containing tile, clini , slide path
        self.cohort_name_list_deploy = []  # list of cohort names
        self.targets_deploy = self.ui.targetlabels_deploy.selectedItems()  # targets chosen for deployment
        self.advanced_values_deploy = [3, 10, 100, 50, 0, 4, ['NA', 'Not Available', 'Equivocal', 'Not Performed', 'unknown']]  # TODO add advanced settings to deploy

        # Events Deploy
        self.ui.advanced_deploy.setEnabled(False)  # TODO advanced settings
        self.ui.projectdir_deploy.clicked.connect(self.open_project_dir_deploy)
        self.ui.choose_slidetable_deploy.clicked.connect(self.open_slidmasttab_deploy)
        self.ui.choose_tiledir_deploy.clicked.connect(self.open_tile_dir_deploy)
        self.ui.choose_model_deploy.clicked.connect(self.open_model_path_deploy)
        self.ui.run_deploy.clicked.connect(self.run_deploy_click)
        self.ui.reset_deploy.clicked.connect(self.reset_deploy_click)
        self.ui.advanced_deploy.clicked.connect(self.advanced_deploy_click)
        self.ui.clini_table_deploy.clicked.connect(self.open_patmasttab_deploy)
        self.ui.addlist_deploy.clicked.connect(self.add_list_clicked_deploy)
        self.ui.del_list_deploy.clicked.connect(self.delete_list_clicked_deploy)
        self.ui.cohortlist_deploy.itemClicked.connect(self.changename_deploy)
        self.ui.test_deploy.clicked.connect(self.testclick_deploy)
        ###########

        # Values Visualize

        # Events Visualize
        self.ui.nextIm_vis.clicked.connect(self.count_up_vis)
        self.ui.prevIm_vis.clicked.connect(self.count_down_vis)
        ###########

    def mode_chosen_learn(self):
        #  disable all mode settings
        self.ui.kfolds_learn.setEnabled(False)
        self.ui.validratio_learn.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.mode_learn = self.ui.choosemode_learn.currentIndex()  # returns chosen mode to value
        if self.mode_learn == 0:
            #  enable settings for test/train mode
            print("test/train chosen")
            self.ui.validratio_learn.setEnabled(True)
            self.ui.label_4.setEnabled(True)
        elif self.mode_learn == 1:
            #  enable settings for test/train mode
            print("k-fold crossvalidation chosen")
            self.ui.kfolds_learn.setEnabled(True)
            self.ui.label_5.setEnabled(True)

        else:
            print("unknown mode chosen")

    def open_slidmasttab_learn(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', r"/GUI_deephist_python/cliniData")
        if path != ('', ''):
            self.slidmasttab_path_learn = path[0]  # path to slide table
            print(path)

    def open_patmasttab_learn(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', r"/GUI_deephist_python/cliniData", "*.xlsx")

        if path != ('', ''):
            self.patmasttab_path_learn = path[0]  # path to clini table

        if path[0] != "":
            df = pd.read_excel(path[0])
            print(list(df))
            self.ui.choosetarg_learn.setEnabled(True)
            self.ui.choosetarg_learn.clear()
            self.ui.choosetarg_learn.addItems(list(df))  # adds feature names to target list

    def open_savingpath_learn(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, r"\home")
        if path != ('', ''):
            self.folderpath_learn = path  # saving path

    def open_tile_path_learn(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, r"\home")
        if path != ('', ''):
            self.tilepath_learn = path  # path where tiles can be found

    def run_click_learn(self):

        def execute_traintest():
            """starts Deepmed in train/test mode"""
            do_experiment(
                project_dir=self.folderpath_learn,
                get=get.MultiTarget(
                    get.SimpleRun(),
                    train_cohorts_df=pd.concat([
                        cohort(tile_path, clin_path, slid_path)
                        for tile_path, clin_path, slid_path in cohortlist_learn]
                    ),
                    target_labels=[str(x.text()) for x in self.ui.choosetarg_learn.selectedItems()],
                    resample_each_epoch=True,
                    valid_frac=int(self.validratio_learn) / 100,
                    na_values=['NA', 'Not Available', 'Equivocal', 'Not Performed', "unknown", "na", "Na", "nA", "NA",
                               "x"],  # TODO add na_values to advanced settings
                    ),
                train=Train(
                    batch_size=int(self.ui.batch_size_learn.text()),
                    max_epochs=int(self.ui.max_epochs_learn.text()),
                    ),
                devices={'cuda:0': 8},  # TODO add workers settings to  advanced settings
                num_concurrent_tasks=0,  # TODO add concurrent task number to advanced settings
            )

        def execute_Kfold_learn():
            """starts Deepmed in k fold crossvalidation mode"""
            cohorts_df = pd.concat([
                cohort(tile_path, clini_path, slide_path)
                for tile_path, clini_path, slide_path in cohortlist_learn]
            )

            do_experiment(
                project_dir=self.folderpath_learn,
                get=get.MultiTarget(
                    get.Crossval(),
                    get.SimpleRun(),

                    cohorts_df=cohorts_df,
                    target_labels=[str(x.text()) for x in self.ui.choosetarg_learn.selectedItems()],
                    max_train_tile_num=int(self.max_tile_num_learn),
                    max_valid_tile_num=128,  # TO DO
                    folds=int(self.kfolds_learn),
                    valid_frac=int(self.validratio_learn) / 100,
                    na_values=['NA', 'Not Available', 'Equivocal', 'Not Performed', "unknown", "na", "Na", "nA", "NA",
                               "x"],  #
                    balance=True,
                    # min_support=5,
                    train=Train(
                        batch_size=int(self.ui.batch_size_learn.text()),
                        max_epochs=int(self.ui.max_epochs_learn.text()),
                    ),
                ),
                devices={'cuda:0': 4},
                num_concurrent_tasks=0,
            )

        # Looping through items
        cohortnamelist_learn = []
        cohortlist_learn = []
        for item_index in range(self.ui.cohortlist_learn.count()):
            # Getting the data embedded in each item from the listWidget
            item_data = self.ui.cohortlist_learn.item(item_index).data(QtCore.Qt.UserRole)
            cohortlist_learn.append(item_data)
            # Getting the data text of each item from the list Widget
            item_text = self.ui.cohortlist_learn.item(item_index).text()
            cohortnamelist_learn.append(item_text)

        self.get_adv_settings()  # actualize advanced settings
        text = [
                f"\n Saved Data:\n",
                f"Folder path: {self.folderpath_learn}",
                f"Chosen target(s): {str([str(x.text()) for x in self.ui.choosetarg_learn.selectedItems()])}",

                f"Mode: {str(self.ui.choosemode_learn.currentText())}",
                f"validation ratio: {str(self.ui.validratio_learn.text())[:-1]}",
                f"K-folds: {str(self.ui.kfolds_learn.text())}",
                f"Tile path: {self.tilepath_learn}",
                f"Cohort list: {str(cohortlist_learn)}",
                f"Cohort Name list {str(cohortnamelist_learn)}",
                f"\nADVANCED SETTINGS:\n",  #
                f"Max epochs: {str(self.max_epochs_learn)}",
                f"Batch size: {str(self.batch_size_learn)}",
                f"Max tile num: {str(self.max_tile_num_learn)}",
                f"GPU Num: {str(self.gpu_num_learn)}",
                f"na Values: {str(self.na_values_learn)}",
                f"Chosen subgroup: {str(self.subgroup_values_learn)}"  # TODO print chosen subgroups
                ]

        print(*text, sep='\n')

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to run the training?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()

        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')

            if True:  # TODO if everything is running, change to try, return specific error in except
                if self.ui.choosemode_learn.currentText() == 'test/train':
                    self.worker = Worker(execute_traintest)  # Any other args, kwargs are passed to the run function
                    # Execute
                    self.threadpool.start(self.worker)

                elif self.ui.choosemode_learn.currentText() == 'k-fold cross validation':
                    self.worker = Worker(execute_Kfold)  # Any other args, kwargs are passed to the run function
                    # Execute
                    self.threadpool.start(self.worker)

                else:
                    raise ValueError(self.mode_learn)

            """except:
                # if not working raise dialog
                QtWidgets.QMessageBox.critical(self, "Error","Oh no!  \n Something went wrong ")

            finally:
                print("cont'd")"""

    def reset_click_learn(self):

        self.slidmasttab_path_learn = " "
        self.patmasttab_path_learn = " "
        self.folderpath_learn = " "
        self.tilepath_learn = " "
        self.ui.choosetarg_learn.clear()
        self.targets_learn = [str(x.text()) for x in self.ui.choosetarg_learn.selectedItems()]
        self.ui.kfolds_learn.setEnabled(False)
        self.kfolds_learn = self.ui.kfolds_learn.text()
        self.ui.validratio_learn.setEnabled(True)
        self.validratio_learn = self.ui.validratio_learn.value()
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(True)
        self.advanced_values_learn = 0

        #self.ui.max_epochs_learn.setProperty("value", 4)  # TODO reset hardcoded
        #self.max_epochs_learn = self.ui.max_epochs_learn.text()
        #self.ui.batch_size_learn.setProperty("value", 64)  # TODO reset hardcoded
        #self.batch_size_learn = self.ui.batch_size_learn.text()
        #self.ui.maxTileNum_learn.setProperty("value", 20)  # TODO reset hardcoded
        #self.max_tile_num_learn = self.ui.maxTileNum_learn.text()
        #self.ui.cohortlist_learn.clear()
        #self.ui.GPU_num_learn.setProperty("value", 3)  # TODO reset hardcoded
        #self.gpu_num_learn = self.ui.GPU_num_learn.text()
        #self.advanced_values_learn = [0, 0]  # TODO reset hardcoded

    def get_adv_settings(self):
        settings = self.advanced_values_learn
        my_dialog = Advanced_Sets(settings)

        self.advanced_values_learn = my_dialog.save_advanced()

        self.gpu_num_learn,self.max_epochs_learn,self.batch_size_learn,self.max_tile_num_learn,self.num_workers_learn, self.concurrent_tasks_learn, self.na_values_learn = self.advanced_values_learn


    def open_advanced_dialog_learn(self):


        """open advanced settings for Deep Learn"""
        settings = self.advanced_values_learn  #TODO gives hardcoded settings to advanced settings.
        my_dialog = Advanced_Sets(settings)
        execval = my_dialog.exec_()
        if execval:
            self.advanced_values_learn = my_dialog.save_advanced()  # returns values from advanced settings
            self.gpu_num_learn, self.max_epochs_learn, self.batch_size_learn, self.max_tile_num_learn, self.num_workers_learn, self.concurrent_tasks_learn, self.na_values_learn = self.advanced_values_learn

            print(f"Advanced settings\n returns {self.advanced_values_learn}")

    def add_list_clicked_learn(self):

        t1 = f"SMT path: {os.path.basename(self.slidmasttab_path_learn)}"
        t2 = f"PMT path: {os.path.basename(self.patmasttab_path_learn)}"
        t3 = f"tile path: {self.tilepath_learn}"
        text = f"Do you want to save this setting?\n\n\n\n{t1}\n\n{t2}\n\n{t3}"
        data = [self.tilepath_learn, self.patmasttab_path_learn, self.slidmasttab_path_learn]

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            n_items = self.ui.cohortlist_learn.count() + 1
            item = QtWidgets.QListWidgetItem(f"Cohort {n_items}")

            item.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)

            # Setting your QListWidgetItem Data  
            item.setData(QtCore.Qt.UserRole, data)  # connects the paths to the given cohort

            self.ui.cohortlist_learn.addItem(item)

    def delete_list_clicked_learn(self):
        self.ui.cohortlist_learn.clear()  # delete all cohorts and clear list

    def changename_learn(self):
        """when a single cohort is clicked, will show a window containing the paths and the name.
         Cohort can be deleted. """
        item_index = self.ui.cohortlist_learn.currentRow()
        t1, t2, t3 = self.ui.cohortlist_learn.item(item_index).data(QtCore.Qt.UserRole)
        t1 = f"tile path: {str(t1)}"
        t2 = f"PMT path: {str(t2)}"
        t3 = f"SMT path: {str(t3)}"
        text = f"Cohort: {str(self.clicked_cohort_learn)}\n\n{t1}\n\n{t2}\n\n{t3}"

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        deleteButton = msgBox.addButton("delete cohort", QtWidgets.QMessageBox.ActionRole)
        returnValue = msgBox.exec()
        if deleteButton == msgBox.clickedButton():
            print("delete cohort")
            self.ui.cohortlist_learn.takeItem(self.ui.cohortlist_learn.currentRow())

    def testclick_learn(self):

        project_dir = 'C:/Users/tseibel/Desktop/test/savepath2'
        tiles_path = 'C:/Users/tseibel/Desktop/test/BLOCKS_NORM_MACENKO'
        clini_path = 'C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_CLINI.xlsx'
        slide_path = 'C:/Users/tseibel/Desktop/test/TCGA-BRCA-A2_SLIDE.xlsx'
        target_label = ['ER Status By IHC', 'Cancer Type Detailed', 'Neoplasm Histologic Type Name',
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
                    max_train_tile_num=500,  # how many tiles from each whole slide image (maximum)
                    min_support=8,  # how many patients are required in each category?
                    valid_frac=.2,  # which fraction of patients is used for validation (early stopping)+
                    na_values=['NA', 'Not Available', 'Equivocal', 'Not Performed', "unknown", "na", "Na", "nA", "NA",
                               "x"],
                    balance=True,  # weather to balance the training set
                    # min_support=5,
                    train=Train(
                        batch_size=128,
                        max_epochs=int(self.max_epochs_learn),
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
            self.ui.stop_learn.setEnabled(True)
            print('OK clicked')
            self.worker = Worker(Execute_test)  # Any other args, kwargs are passed to the run function
            # Execute
            self.threadpool.start(self.worker)

    def stop_clicked_learn(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Do you want to stop the pipeline?\n Progress will be lost.")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('stop clicked')
            #####
            # TODO kill worker to stop training
            #####
            print("close pipeline")

    def subgrouping_clicked_learn(self):
        """open cohort settings for Deep Learn"""
        path = self.patmasttab_path_learn
        my_dialog = Cohort_Sets(path)
        execval = my_dialog.exec_()
        if execval:
            self.subgroup_values_learn = my_dialog.save_cohort()  # values from cohort window
            print(self.subgroup_values_learn)

    def add_target_clicked_learn(self):
        my_dialog = Add_Targs(self.patmasttab_path_learn)
        execval = my_dialog.exec_()
        if execval:
            self.target_learn,self.threshold_learn  = my_dialog.save_add_target()  # returns values from advanced settings
            print(f"Added Target settings\n returns {self.target_learn}")
            self.ui.choosetarg_learn.addItem(f"custom_{self.target_learn}")  # adds feature names to target list

            def subgrouper( x: pd.Series):
                thresh = self.threshold_learn
                target=str(self.target_learn)
                if x[target] > float(thresh):
                    return f'{target}above{thresh}'
                elif x[target] <= float(thresh):
                    return f'{target}below{thresh}'
                else:
                    return None



    def open_project_dir_deploy(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, r"\home")
        if path != ('', ''):
            self.project_dir_deploy = path

    def open_patmasttab_deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', r"/GUI_deephist_python/cliniData", "*.xlsx")

        if path != ('', ''):
            self.patmasttab_path_deploy = path[0]

        if path[0] != "":
            df = pd.read_excel(path[0])
            print(list(df))
            self.ui.targetlabels_deploy.setEnabled(True)
            self.ui.targetlabels_deploy.clear()
            self.ui.targetlabels_deploy.addItems(list(df))

            self.ui.targetlabels2_deploy.setEnabled(True)
            self.ui.targetlabels2_deploy.clear()
            self.ui.targetlabels2_deploy.addItems(list(df))

    def open_slidmasttab_deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData")
        if path != ('', ''):
            self.slidmasttab_path_deploy = path[0]
            print(path)

    def open_tile_dir_deploy(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, r"\home")
        if path != ('', ''):
            self.choose_tiledir_deploy = path

    def open_model_path_deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', r"/GUI_deephist_python/models", "*.pkl")
        if path != ('', ''):
            self.model_path_deploy = path[0]
            print(path[0])

            learner = load_learner(
                path[0])


            #print(learner.dls.tfms[1][0]) # TODO not working yet. 



    def run_deploy_click(self):

        def execute_deploy():
            do_experiment(
                project_dir=self.project_dir_deploy,
                get=get.MultiTarget(
                    get.SimpleRun(),
                    test_cohorts_df=pd.concat([
                        cohort(tile_path, clin_path, slid_path)
                        for tile_path, clin_path, slid_path in self.cohortlist_deploy]
                    ),
                    target_labels=[str(x.text()) for x in self.targets_deploy],

                    balance=True,  # weather to balance the training set
                    # min_support=5,
                    train=Load(
                        project_dir=self.project_dir_deploy,
                        training_project_dir=self.model_path_deploy),
                ),
                evaluators=[Grouped(auroc), Grouped(p_value)],
                crossval_evaluators=[AggregateStats(label='fold')],
                multi_target_evaluators=[AggregateStats(label='target', over=['fold'])],
            )

        cohortnamelist_deploy = []
        cohortlist_deploy = []

        # Looping through items
        for item_index in range(self.ui.cohortlist_deploy.count()):
            # Getting the data embedded in each item from the listWidget
            item_data = self.ui.cohortlist_deploy.item(item_index).data(QtCore.Qt.UserRole)
            cohortlist_deploy.append(item_data)
            # Getting the datatext of each item from the listWidget
            item_text = self.ui.cohortlist_deploy.item(item_index).text()
            cohortnamelist_deploy.append(item_text)

        print("run")




        text = ["Project dir: " + str(self.project_dir_deploy),
                "batch size: " + str(self.batch_size_deploy),
                "max tile num: " + str(self.max_tile_num_deploy),
                "SMT path: " + os.path.basename(self.slidmasttab_path_deploy),
                "PMT path: " + os.path.basename(self.patmasttab_path_deploy),
                "tile directory: " + str(self.choose_tile_dir_deploy),
                "model path: " + str(self.model_path_deploy),
                "target evaluator" + str("yes"),
                "chosen groups: " + str([str(x.text()) for x in self.ui.targetlabels_deploy.selectedItems()]),

                "cohortlists:" + str(cohortlist_deploy),
                "cohort name list" + str(cohortnamelist_deploy),
                ]
        print(*text, sep='\n')

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Are you sure you want to run the deploy?")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            try:
                self.worker = Worker(execute_deploy)  # Any other args, kwargs are passed to the run function
                # Execute
                self.threadpool.start(self.worker)

            except (ValueError, Exception):
                # if not working raise dialog
                QtWidgets.QMessageBox.critical(self, "Error", "Oh no!  \n Something went wrong ")

            finally:
                print("cont'd")

    def reset_deploy_click(self):
        self.cohort_path_deploy = ""
        self.choose_tile_dir_deploy = ""
        self.model_path_deploy = ""
        self.project_dir_deploy = ""
        self.ui.targetlabels_deploy.clear()
        self.ui.targetlabels2_deploy.clear()
        self.ui.batchsize_deploy.setProperty("value", 64)  # hardcoded
        self.cohortlist_deploy = []
        self.cohort_name_list_deploy = []
        print("reset")

    def advanced_deploy_click(self):
        """open advanced settings for deploy"""
        settings = self.advanced_values_deploy  # TODO gives hardcoded settings to advanced settings.
        my_dialog = Advanced_Sets(settings)
        execval = my_dialog.exec_()
        if execval is True:
            self.advanced_values_deploy = my_dialog.save_advanced()  # returns values from advanced settings
            print(f"Advanced settings\n returns {self.advanced_values_deploy}")  # TODO add advanced settings to deploy

    def add_list_clicked_deploy(self):

        t1 = "SMT path: " + os.path.basename(self.slidmasttab_path_deploy)
        t2 = "PMT path: " + os.path.basename(self.patmasttab_path_deploy)
        t3 = "tile directory: " + str(self.choose_tiledir_deploy)
        text = "Do you wont to save this setting?" + "\n\n" + "\n\n" + t1 + "\n\n" + t2 + "\n\n" + t3
        data = [self.choose_tiledir_deploy, self.patmasttab_path_deploy, self.slidmasttab_path_deploy]

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        if returnValue == QtWidgets.QMessageBox.Ok:
            print('OK clicked')
            n_items = self.ui.cohortlist_deploy.count() + 1
            item = QtWidgets.QListWidgetItem(f"Cohort {n_items}")

            item.setFlags(
                QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEnabled)

            # Setting your QListWidgetItem Data  
            item.setData(QtCore.Qt.UserRole, data)

            self.ui.cohortlist_deploy.addItem(item)

    def delete_list_clicked_deploy(self):
        self.ui.cohortlist_deploy.clear()

    def changename_deploy(self):
        item_index = self.ui.cohortlist_deploy.currentRow()
        t1, t2, t3 = self.ui.cohortlist_deploy.item(item_index).data(QtCore.Qt.UserRole)
        t1 = "Tile path: " + str(t1)
        t2 = "PMT path: " + str(t2)
        t3 = "SMT path: " + str(t3)

        text = "Cohort:" + "cohortname" + "\n\n" + "\n\n" + t1 + "\n\n" + t2 + "\n\n" + t3

        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(text)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        deleteButton = msgBox.addButton("delete cohort", QtWidgets.QMessageBox.ActionRole)
        returnValue = msgBox.exec()
        if deleteButton == msgBox.clickedButton():
            print("delete cohort")
            self.ui.cohortlist_deploy.takeItem(self.ui.cohortlist_deploy.currentRow())

    def testclick_deploy(self):

        project_dir = 'C:/Users/tseibel/Desktop/test/testbuttonbenchmark'

        def Execute_test():
            do_experiment(
                project_dir=project_dir,
                get=get.MultiTarget(
                    get.SimpleRun(),
                    test_cohorts_df=cohort(
                        tiles_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-TESTSET-DEEPMED-TILES/BLOCKS_NORM_MACENKO',
                        clini_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_CLINI.xlsx',
                        slide_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_SLIDE.xlsx'),
                    target_labels=['ER Status By IHC', 'Cancer Type Detailed', 'Neoplasm Histologic Type Name',
                                   'Fraction Genome Altered'],
                    na_values=['NA', 'Not Available', 'Equivocal', 'Not Performed'],

                    balance=True,  # weather to balance the training set
                    # min_support=5,
                    evaluators=[Grouped(auroc), Grouped(p_value)],

                    multi_target_evaluators=[AggregateStats(label='target')],
                    train=Load(
                        project_dir=self.project_dir_deploy,
                        training_project_dir=self.model_path_deploy),
                ),

            )

        def Execute_test2():
            project_dir2 = 'C:/Users/tseibel/Desktop/test/savepath1'
            do_experiment(
                project_dir=project_dir2,
                get=get.MultiTarget(
                    get.SimpleRun(),
                    test_cohorts_df=cohort(
                        tiles_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-TESTSET-DEEPMED-TILES/BLOCKS_NORM_MACENKO',
                        clini_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_CLINI.xlsx',
                        slide_path='C:/Users/tseibel/Desktop/test/TCGA-BRCA-E2_SLIDE.xlsx'),
                    target_labels=['ER Status By IHC'],
                    na_values=['NA', 'Not Available', 'Equivocal', 'Not Performed'],

                    balance=True,  # weather to balance the training set
                    # min_support=5,
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
            self.worker = Worker(Execute_test2)  # Any other args, kwargs are passed to the run function
            # Execute
            self.threadpool.start(self.worker)

    def count_up_vis(self):
        n = self.ui.imgcounter_vis.intValue()
        self.ui.imgcounter_vis.display(n + 1)

    def count_down_vis(self):
        n = self.ui.imgcounter_vis.intValue()
        if n > 0:
            self.ui.imgcounter_vis.display(n - 1)


class Advanced_Sets(QtWidgets.QDialog):
    """"advanced settings dialog for Deep Learn"""

    def __init__(self,settings, parent=None):
        super(Advanced_Sets, self).__init__(parent)
        self.ui = Ui_advanced_settings()
        self.ui.setupUi(self)
        self.settings = settings
        if self.settings == 0:
            self.gpunum,self.max_epochs,self.batch_size,self.max_tile_num ,self.num_workers,self.concurrent_tasks,self.na_values = self.save_advanced()
        else:
            # Values
            self.gpunum = self.settings[0]
            self.ui.GPUnum.setValue(int(self.gpunum))
            self.max_epochs = self.settings[1]
            self.ui.max_epochs.setValue(int(self.max_epochs))
            self.batch_size = self.settings[2]
            self.ui.batch_size.setValue(int(self.batch_size))
            self.max_tile_num = self.settings[3]
            self.ui.maxTileNum.setValue(int(self.max_tile_num))
            self.num_workers = self.settings[4]
            self.ui.workers.setValue(int(self.num_workers))
            self.concurrent_tasks = self.settings[5]

            self.ui.conc_tasks.setValue(int(self.concurrent_tasks))
            self.na_values = self.settings[6]
            self.ui.na_settings.setText(str(self.na_values))

        # Events
        self.ui.cancel_advancedDL.clicked.connect(self.close)
        self.ui.save_advancedDL.clicked.connect(self.accept)
        self.ui.reset_advancedDL.clicked.connect(self.reset_advanced)

    def save_advanced(self):
        print("Save...")
        gpunum = self.ui.GPUnum.value()
        max_epochs =self.ui.max_epochs.value()
        batch_size = self.ui.batch_size.value()
        max_tile_num = self.ui.maxTileNum.value()
        num_workers = self.ui.workers.value()
        concurrent_tasks = self.ui.conc_tasks.value()
        na_values = self.ui.na_settings.toPlainText()

        try:
            na_value_list = na_values[1:-1].replace("\'", "").replace("\"","")
            #print(na_value_list)
            na_value_list = na_value_list.split(",")
            #print(na_value_list)
            na_value_list = [val[1:] if val[0]==" " and len(val)>1 else val for val in na_value_list]
            #print(na_value_list)
        except:
            raise "error"
        else:
            print("cont'd")

        return [gpunum,max_epochs,batch_size,max_tile_num,num_workers,concurrent_tasks,na_value_list]


    def reset_advanced(self):
        self.ui.GPUnum.setProperty("value", self.settings[0])

        self.ui.max_epochs.setProperty("value",self.settings[1])
        self.ui.batch_size.setProperty("value",self.settings[2])
        self.ui.maxTileNum.setProperty("value",self.settings[3])
        self.ui.workers.setProperty("value",self.settings[4])
        self.ui.conc_tasks.setProperty("value",self.settings[5])
        self.ui.na_settings.setText(str(self.settings[6]))

class Add_Targs(QtWidgets.QDialog):
    '''add targets dialog in DL '''

    def __init__(self,clinitab,parent=None):
        super(Add_Targs, self).__init__(parent)
        self.ui = Ui_add_target()
        self.ui.setupUi(self)
        self.clinitab = clinitab
        self.clinitab =  r'cliniData/TCGA-BRCA-DX_CLINI.xlsx'
        self.df = pd.read_excel(self.clinitab)

        self.ui.groups.setEnabled(True)
        self.ui.groups.clear()
        self.ui.groups.addItems(list(self.df))  # adds feature names to target list

        self.ui.groups.currentIndexChanged.connect(self.groups_clicked)
        self.ui.save_button.clicked.connect(self.accept)
        self.ui.cancel_button.clicked.connect(self.close)




    def groups_clicked(self):
        self.name =  self.ui.groups.currentText()
        if self.df[self.name].dtype == float:
            self.ui.min_val.setEnabled(True)
            self.ui.min_label.setEnabled(True)
            self.ui.max_val.setEnabled(True)
            self.ui.max_label.setEnabled(True)
            self.ui.threshold_value.setEnabled(True)
            self.ui.threshold_label.setEnabled(True)
            self.ui.min_val.setText(str(self.df[self.name].min()))
            self.ui.max_val.setText(str(self.df[self.name].max()))
            self.ui.threshold_value.setText(str(self.df[self.name].median()))
        else:
            self.ui.min_val.setEnabled(False)
            self.ui.min_label.setEnabled(False)
            self.ui.max_val.setEnabled(False)
            self.ui.max_label.setEnabled(False)
            self.ui.threshold_value.setEnabled(False)
            self.ui.threshold_label.setEnabled(False)

    def save_add_target(self):

        return [self.name, self.ui.threshold_value .text()]

class Cohort_Sets(QtWidgets.QDialog):
    """"cohort settings dialog for Deep Learn"""

    def __init__(self, path, parent=None):
        super(Cohort_Sets, self).__init__(parent)

        self.ui = Ui_cohort_settings()
        self.ui.setupUi(self)
        self.path = path
        # Values
        self.text = []
        self.groupname = ""
        self.subgroupname = ""
        self.min = 0
        self.max = 0
        self.threshold = 0
        self.isfloat = True

        self.path = r'cliniData/TCGA-BRCA-DX_CLINI.xlsx'
        try:
            self.df = pd.read_excel(self.path)
            self.ui.groups.setEnabled(True)
            self.ui.groups.clear()
            self.ui.groups.addItems(list(self.df))
        except (ValueError, Exception):
            QtWidgets.QMessageBox.critical(self, "Error", "problem with the   \n clinitable ")

        finally:
            print("cont'd")

        self.ui.and_button.setEnabled(False)  # TODO implement and, or etc.
        self.ui.or_button.setEnabled(False)
        self.ui.back_button.setEnabled(False)
        self.enable_widgets(bool_val=False, mode=2)

        # Events
        self.ui.and_button.clicked.connect(self.and_clicked)
        self.ui.back_button.clicked.connect(self.back_clicked)
        self.ui.or_button.clicked.connect(self.or_clicked)
        self.ui.save_button.clicked.connect(self.accept)

        self.ui.cancel_button.clicked.connect(self.close)
        self.ui.groups.activated.connect(self.groups_clicked)
        self.ui.subgroups.activated.connect(self.subgroup_clicked)
        self.ui.threshold_value.textChanged.connect(self.threshold_changed)

    def and_clicked(self):
        self.ui.subgroups.clear()
        self.text.append(self.groupname + self.subgroupname)
        self.text.append(" AND ")
        self.ui.querybox.setText(''.join(self.text))
        self.groupname = ""
        self.subgroupname = ""

    def back_clicked(self):
        if len(self.text) > 1 and self.groupname == "":
            self.text = self.text[0:-1]
        elif len(self.text) == 1 and self.groupname == "":
            self.text = []
        self.groupname = ""
        self.subgroupname = ""
        self.ui.querybox.setText(''.join(self.text))

    def or_clicked(self):
        self.ui.subgroups.clear()
        self.ui.subgroups.setEnabled(False)
        self.text.append(self.groupname + self.subgroupname)
        self.text.append(" OR ")
        self.ui.querybox.setText(''.join(self.text))
        self.groupname = ""
        self.subgroupname = ""

    def save_cohort(self):
        print(self.groupname)
        if self.groupname != "":
            self.text.append(self.groupname + self.subgroupname)
            self.ui.querybox.setText(''.join(self.text))
        else:  # last item in list is either AND or OR operator

            self.text = self.text[:-1]

        self.groupname = ""
        self.subgroupname = ""
        print("Save...")
        if self.isfloat:
            return [self.groupname,float(self.threshold)]
        else:
            return [self.groupname,self.subgroupname]


    def groups_clicked(self):
        print(self.ui.groups.currentText())

        self.enable_widgets(bool_val=False, mode=2)

        self.ui.subgroups.clear()
        self.subgroupname = ""
        self.groupname = self.ui.groups.currentText()
        addText = f"<span style=\" font-size:14pt; font-weight:400; color:#0000ff;\" >  [\"{self.groupname}\"] </span>"
        self.ui.querybox.setText(''.join(self.text) + addText)
        self.ui.querybox.setText(''.join(self.text) + addText)
        self.isfloat = self.df[self.ui.groups.currentText()].dtype == float
        if self.isfloat:

            print("float")
            self.enable_widgets(bool_val=True, mode=2)
            self.ui.subgroups.addItem("-choose subgroup-")
            self.ui.subgroups.addItems(["class1","class2"])


            self.min = self.df[self.ui.groups.currentText()].min()
            self.max = self.df[self.ui.groups.currentText()].max()
            self.threshold = self.df[self.ui.groups.currentText()].median()
            self.ui.min_val.setText(str(self.min))
            self.ui.max_val.setText(str(self.max))
            self.ui.threshold_value.setText(str(self.threshold))

            addText = f" {self.groupname}[ {self.min} < class1 < {self.threshold}  < class2 < {self.max}] ]"
            self.ui.querybox.setText(''.join(self.text) + addText)

        else:
            subgroup_cat = pd.Categorical(self.df[self.ui.groups.currentText()])
            self.enable_widgets(bool_val=True, mode=0)
            self.ui.subgroups.addItem("-choose subgroup-")
            self.ui.subgroups.addItems([str(val) for val in subgroup_cat.categories])

    def subgroup_clicked(self):
        self.subgroupname = f" {self.ui.subgroups.currentText()} "
        if self.ui.subgroups.currentText() != "-choose subgroup-" and not self.isfloat:
            addText = f"[\"{self.groupname}\"] == \"{self.subgroupname}\" "

        elif self.ui.subgroups.currentText() != "-choose subgroup-" and self.isfloat:

            if self.ui.subgroups.currentText() == "class1":

                addText = f"[\"{self.groupname}\"] < {self.threshold} "

            else:
                addText = f"[\"{self.groupname}\"] > {self.threshold} "



        else:

            addText = f"[\"{self.groupname}\"]"

        print(addText)

        #addText = f"<span style=\" font-size:14pt; font-weight:400; color:#0000ff;\" >  {addText} </span>"

        self.ui.querybox.setText(''.join(self.text) + addText)

    def threshold_changed(self):
        self.threshold = self.ui.threshold_value.text()
        addText = f" {self.groupname}[ {self.min} < class1 < {self.threshold}  < class2 < {self.max}] ]"
        self.ui.querybox.setText(''.join(self.text) + addText)
        print(3)

    def enable_widgets(self, bool_val, mode):
        """Helper function to enable(bool=True) or disable(bool=False)
         categorical(mode=0) or continuous(mode=1) or  both(mode=2)"""
        # self.ui.back_button.setEnabled(bool_val)
        # self.ui.and_button.setEnabled(bool_val)
        # self.ui.or_button.setEnabled(bool_val)
        if mode == 0:
            self.ui.subgroups.setEnabled(bool_val)
        elif mode == 1:
            self.ui.min_label.setEnabled(bool_val)
            self.ui.min_val.setEnabled(bool_val)
            self.ui.max_label.setEnabled(bool_val)
            self.ui.max_val.setEnabled(bool_val)
            self.ui.threshold_label.setEnabled(bool_val)
            self.ui.threshold_value.setEnabled(bool_val)
        elif mode == 2:
            self.ui.subgroups.setEnabled(bool_val)
            self.ui.min_label.setEnabled(bool_val)
            self.ui.min_val.setEnabled(bool_val)
            self.ui.max_label.setEnabled(bool_val)
            self.ui.max_val.setEnabled(bool_val)
            self.ui.threshold_label.setEnabled(bool_val)
            self.ui.threshold_value.setEnabled(bool_val)

        else:
            raise ValueError('Error: wrong inputs.')


class Worker(QtCore.QRunnable):
    """ Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function
    """

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @pyqtSlot()
    def run(self):
        """ Initialise the runner function with passed args, kwargs."""
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

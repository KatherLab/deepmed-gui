import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from package.mainwindow import Ui_gui_histo_main
from package.advanced_settings import Ui_advanced_settings
import os
import pandas as pd
import numpy as np

#from deepest_histology.experiment_imports import *


import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


class Mainwindow_con(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_gui_histo_main()
        self.ui.setupUi(self)

        # Events Deeplearn
        self.slidmasttab_path_DL = " "  # empty values
        self.patmasttab_path_DL = " "  # empty values
        self.folderpath_path_DL = " "  # empty values
        self.tilepath_DL = " "  # empty values
        self.advanced_values = [0, 0]  # basic values from advanced settings Default NEEDS TO BE SET
        self.cohortlist_DL=[]

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
        if self.ui.choosemode_DL.currentIndex()==0:
            print("test/train chosen")
            self.ui.traintestratio_DL.setEnabled(True)
            self.ui.label_4.setEnabled(True)
        elif self.ui.choosemode_DL.currentIndex()==1:
            print("k-fold crossvalidation chosen")
            self.ui.kfolds_DL.setEnabled(True)
            self.ui.label_5.setEnabled(True)

        else:
            print("unknown mode chosen")
    def open_slidmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData", "*.csv")
        if path != ('', ''):
            self.slidmasttab_path_DL = path[0]
            print(path)

    def open_patmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData", "*.xlsx")

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

        text = ["Projectname: " + self.ui.project_name_DL.text(),
                "SMT path: " + os.path.basename(self.slidmasttab_path_DL),
                "PMT path: " + os.path.basename(self.patmasttab_path_DL),
                "Folder path: " + self.folderpath_path_DL,
                "Chosen target(s): " + str([str(x.text()) for x in self.ui.choosetarg_DL.selectedItems()]),
                "Max epochs: " + str(self.ui.max_epochs_DL.text()),
                "Batch size: " + str(self.ui.batch_size_DL.text()),
                "Max tile num: " + str(self.ui.maxTileNum_DL.text()),
                "GPU Num: " +str(self.ui.GPU_num_DL.text()),
                "Mode: " +str(self.ui.choosemode_DL.currentText()),
                "Train/test ratio: " +str(self.ui.traintestratio_DL.value()),
                "K-folds: " +str(self.ui.kfolds_DL.text()),
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
            try:
                #  try run function
                #print(1 / 0)  # to simulate error
                print("try to  run")
            except:
                # if not working raise dialog
                QtWidgets.QMessageBox.critical(self, "Error","Oh no!  \n Something went wrong ")

            finally:
                print("cont'd")

    def resetDL_click(self):
        self.ui.project_name_DL.clear()
        self.slidmasttab_path_DL = " "
        self.patmasttab_path_DL = " "
        self.folderpath_path_DL = " "
        self.ui.choosetarg_DL.clear()
        self.ui.kfolds_DL.setEnabled(False)
        self.ui.traintestratio_DL.setEnabled(True)
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(True)
        self.ui.max_epochs_DL.setProperty("value", 4)  # hardcoded
        self.ui.batch_size_DL.setProperty("value", 0)  # hardcoded
        self.ui.maxTileNum_DL.setProperty("value", 0)  # hardcoded
        self.cohortlist = []

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
            self.ui.cohort_list_DL.addItem(f"Cohort {n_items}")
            self.cohortlist_DL.append([os.path.basename(self.slidmasttab_path_DL),os.path.basename(self.patmasttab_path_DL),self.tilepath_DL])
    def delete_list_clicked_DL(self):
        self.ui.cohort_list_DL.clear()
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
                #  try run deploy function
                #print(1 / 0)  # to simulate error
                print("try to  run")
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

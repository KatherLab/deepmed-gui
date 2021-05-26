import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from package.mainwindow import Ui_gui_histo_main
from package.advanced_settings import Ui_advanced_settings
import os
import pandas as pd
import numpy as np

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

        self.ui.slide_masttab_DL.clicked.connect(self.open_slidmasttab)
        self.ui.clini_table_DL.clicked.connect(self.open_patmasttab)
        self.ui.savingpath_DL.clicked.connect(self.open_savingpath)
        self.ui.tilespath_DL.clicked.connect(self.open_tile_path)
        self.ui.run_DL.clicked.connect(self.runDL_click)
        self.ui.reset_DL.clicked.connect(self.resetDL_click)
        self.ui.advanced_sets_DL.clicked.connect(self.open_DL_dialog)
        self.ui.choosemode_DL.currentIndexChanged.connect(self.mode_chosen)
        ###########


        # Events Deploy
        self.cohort_path_deploy = ""  # empty values
        self.tile_dir_deploy = ""  # empty values
        self.model_path_deploy = ""  # empty values
        self.project_dir_open = ""  # empty values
        self.patmasttab_path_deploy = " "  # empty values

        self.ui.projectdir_Deploy.clicked.connect(self.open_project_dir_Deploy)
        self.ui.choose_cohort_Deploy.clicked.connect(self.open_cohort_Deploy)
        self.ui.choose_tiledir_Deploy.clicked.connect(self.open_tile_path)
        self.ui.choose_model_Deploy.clicked.connect(self.open_model_path_Deploy)
        self.ui.run_Deploy.clicked.connect(self.run_Deploy_click)
        self.ui.reset_Deploy.clicked.connect(self.reset_Deploy_click)
        self.ui.advanced_Deploy.clicked.connect(self.advanced_Deploy_click)
        self.ui.clini_table_Deploy.clicked.connect(self.open_patmasttab_deploy)
        ###########
        # Events Visualize
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

        t1 = "Projectname: " + self.ui.project_name_DL.text()
        t2 = "SMT path: " + os.path.basename(self.slidmasttab_path_DL)
        t3 = "PMT path: " + os.path.basename(self.patmasttab_path_DL)
        t4 = "folderpath: " + self.folderpath_path_DL
        t5 = "chosen target(s): " + str([str(x.text()) for x in self.ui.choosetarg_DL.selectedItems()])
        t6 = "max epochs: " + str(self.ui.max_epochs_DL.text())
        t7 = "batch size: " + str(self.ui.batch_size_DL.text())
        t8 = "max tile num: " + str(self.ui.maxTileNum_DL.text())
        t9 = "GPU Num: " +str(self.ui.GPU_num_DL.text())
        t10 = "mode: " +str(self.ui.choosemode_DL.currentText())
        t11 = "train/test ratio: " +str(self.ui.traintestratio_DL.value())
        t12 = "k-folds: " +str(self.ui.kfolds_DL.text())
        t13 = "tile path: " + self.tilepath_DL

        text1 = t1 + "\n\n" + t2 + "\n\n" + t3 + "\n\n" + t4 + "\n\n" + t5 + "\n\n" + t6 + "\n\n" + t7 + "\n\n" + t8
        text2 = t9 + "\n\n" + t10 + "\n\n" + t11 + "\n\n" + t12 + "\n\n" + t13 + "\n\n"

        t31 = "gpu num: " + str(self.advanced_values[0])
        t32 = "binarize quantil: " + str(self.advanced_values[1])
        text3 = "advanced settings: " + "\n\n" + t31 + "\n\n" + t32
        print(text1+text2+text3)

        try:
            #  try run function
            print(1 / 1)  # to simulate error
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
        self.ui.traintestratio_DL.setEnabled(False)
        self.ui.label_5.setEnabled(False)
        self.ui.label_4.setEnabled(False)
        self.ui.max_epochs_DL.setProperty("value", 4)  # hardcoded
        self.ui.batch_size_DL.setProperty("value", 0)  # hardcoded
        self.ui.maxTileNum_DL.setProperty("value", 0)  # hardcoded

    def open_DL_dialog(self):
        """open advanced settings for Deep Learn"""
        my_dialog = MyDialog()
        execval = my_dialog.exec_()
        if execval == True:
            self.advanced_values = my_dialog.save_advanced()  # values from dialog window
        print(self.advanced_values)


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

    def open_cohort_Deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cohorts", "*.txt")
        if path != ('', ''):
            self.cohort_path_deploy = path[0]
            print(path)

    def open_tile_dir_Deploy(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "\home")
        if path != ('', ''):
            self.tile_dir_deploy = path

    def open_model_path_Deploy(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/models", "*.csv")
        if path != ('', ''):
            self.cohort_path_deploy = path[0]
            print(path)

    def run_Deploy_click(self):
        print("run")
        t1 = "Project dir: " + str(self.project_dir_open)
        t2 = "batch size: " + str(self.ui.batchsize_Deploy.text())
        t3 = "max tile num: " + str(self.ui.maxtilenum_Deploy.text())
        t4 = "cohort: " + str(self.cohort_path_deploy)
        t5 = "tile directory: " + str(self.tile_dir_deploy)
        t6 = "model path: " + str(self.cohort_path_deploy)
        t7 = "target evaluator" + str("yes")
        t8 = "chosen target(s): " + str([str(x.text()) for x in self.ui.targetlabels_Deploy.selectedItems()])
        text=t1 + "\n\n" + t2 + "\n\n" + t3 + "\n\n" + t4 + "\n\n" + t5 + "\n\n" + t6 + "\n\n" + t7 + "\n\n" + t8
        print(text)
    def reset_Deploy_click(self):
        self.cohort_path_deploy = ""
        self.tile_dir_deploy = ""
        self.model_path_deploy = ""
        self.project_dir_open = ""
        self.ui.targetlabels_Deploy.clear()
        self.ui.batchsize_Deploy.setProperty("value",64)

        print("reset")
    def advanced_Deploy_click(self):
        print("advanced settings")

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

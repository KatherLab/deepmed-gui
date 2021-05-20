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
        self.slidmasttab_path = " " #empty values
        self.patmasttab_path = " " #empty values
        self.folderpath_path = " " #empty values
        self.plotter() # open function to plot graphics


        self.ui.slide_masttab.clicked.connect(self.open_slidmasttab)
        self.ui.clini_table.clicked.connect(self.open_patmasttab)
        self.ui.choosepath.clicked.connect(self.open_folderpath)
        self.ui.run_DL.clicked.connect(self.runDL_click)
        self.ui.reset_DL.clicked.connect(self.resetDL_click)
        self.ui.advanced_sets_DL.clicked.connect(self.open_DL_dialog)
        ###########



        # Events Deploy
        ###########
        # Events Visualize
        ###########



    def plotter(self):
        print("hi")
        self.scene = QtWidgets.QGraphicsScene()
        plt.style.use('classic')
        figure = Figure()
        axes = figure.gca()
        axes.set_title("Training Plot")
        x=np.linspace(0,20,100)
        y=0.9-np.exp(-x)+0.03*np.random.random(len(x))
        y2 = 0.7 - np.exp(-x) + 0.01 * np.random.random(len(x))
        axes.plot(x,y,label="train")
        axes.plot(x, y2,"-.",label="test")
        axes.set_xlabel("epochs")

        axes.grid()
        axes.legend()
        canvas = FigureCanvas(figure)
        canvas.setGeometry(0, 0, 440, 500)
        self.scene.addWidget(canvas)

        self.ui.graph_autoDL.setScene(self.scene)
        self.ui.graph_autoDL.show()


    def open_slidmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData",
                                                "*.csv")
        if path != ('', ''):
            self.slidmasttab_path = path[0]
            print(path)

    def open_patmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData",
                                                "*.xlsx")

        if path != ('', ''):
            self.patmasttab_path = path[0]

        if path[0]!="":
            df = pd.read_excel(path[0])
            print(list(df))
            self.ui.choosetarg.clear()
            self.ui.choosetarg.addItems(list(df))


        print("hello")

    def open_folderpath(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self,"\home")
        if path != ('', ''):
            self.folderpath_path = path

    def runDL_click(self):

        t1 = "Projectname: " + self.ui.project_name.text()
        t2= "SMT path: " + os.path.basename(self.slidmasttab_path)
        t3= "PMT path: " + os.path.basename(self.patmasttab_path)
        t4 = "folderpath: " + self.folderpath_path
        t5 = "chosen target(s): " + str([str(x.text()) for x in self.ui.choosetarg.selectedItems()])
        t6= "max epochs: " + str(self.ui.max_epochs.text())
        t7= "batch size: " + str(self.ui.batch_size.text())
        t8= "max tile num: " + str(self.ui.maxTileNum.text())
        text= t1 + "\n\n" + t2 + "\n\n" + t3 + "\n\n" + t4 + "\n\n" + t5 + "\n\n" + t6 + "\n\n" + t7 + "\n\n" + t8
        t9="gpu num: "+str()
        t10="binarize quantil: "+str()
        text2 = t9 + "\n\n" + t10
        print(text)
        print(text2)




    def resetDL_click(self):
        self.ui.project_name.clear()
        self.slidmasttab_path = " "
        self.patmasttab_path = " "
        self.folderpath_path = " "
        self.ui.choosetarg.clear()


    def testbutton_click(self):
        """artifact"""
        codename=self.ui.projectname.text() + "-generated"

        text={"ProjectName":self.ui.projectname.text(),"folderName":{"Temp":self.folderpath_path},"codename":codename,"allTargets":[str(x.text()) for x in self.ui.choosetarg.selectedItems()]}
        a=os.path.exists("experiments/"+codename+".txt")
        if a==True:
            QtWidgets.QMessageBox.critical(self, "File already exists", "File already exists  \n please choose another projectname")

        else:
            # "no experiment file with same name, can safe text as "experiments/"+codename+".txt" in folder
            filename="experiments/"+codename+".txt"
            text=str(text).replace(" ","")
            text=text.replace("\'","\"")
            f = open(filename, "w")
            f.write(text)
            f.close()

    def open_DL_dialog(self, checked=None):
        if checked == None: return
        my_dialog = MyDialog()
        my_dialog.exec_()


class MyDialog(QtWidgets.QDialog):
    """"advanced settings dialog for Deep Learn"""
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.ui = Ui_advanced_settings()
        self.ui.setupUi(self)



        self.ui.cancel_advancedDL.clicked.connect(self.cancel_advanced)
        self.ui.save_advancedDL.clicked.connect(self.save_advanced)

    def cancel_advanced(self):
        print("Closing Dialog Window...")
        self.close()

    def save_advanced(self):
        print("Closing Dialog Window...")
        self.neu="works"
    def gpus(self):
        a=self.ui.GPUnum.text()
        return a

app = QtWidgets.QApplication(sys.argv)
widget = Mainwindow_con()
widget.show()

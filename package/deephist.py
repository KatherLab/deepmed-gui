import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from package.mainwindow import Ui_gui_histo_main
import os
import pandas as pd


class Mainwindow_con(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_gui_histo_main()
        self.ui.setupUi(self)


        #Events Experiment Generator
        self.slidmasttab_path = "-"
        self.patmasttab_path = "-"
        self.folderpath_path = "-"

        self.ui.slidmasttab.clicked.connect(self.open_slidmasttab)
        self.ui.patmasttab.clicked.connect(self.open_patmasttab)
        self.ui.folderpath.clicked.connect(self.open_folderpath)
        self.ui.testbutton.clicked.connect(self.testbutton_click)
        self.ui.reset_expgen.clicked.connect(self.resetbutton_click)
        ###########

        #Events autoDeeplearn
        ###########
        # Events autoDeploy
        ###########
        # Events autoVisualize
        ###########

    def open_slidmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData",
                                                "*.csv")
        if path != ('', ''):
            self.slidmasttab_path = path[0]
            print(path)
        self.testbutton_click()
    def open_patmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData",
                                                "*.xlsx")

        if path != ('', ''):
            self.patmasttab_path = path[0]

        self.testbutton_click()
        df = pd.read_excel(path[0])
        print(list(df))
        self.ui.choosetarg.clear()
        self.ui.choosetarg.addItems(list(df))



    def open_folderpath(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self,"\home")
        if path != ('', ''):
            self.folderpath_path = path
        self.testbutton_click()
    def testbutton_click(self):
        """testbutton on first page, if clicked, shows the File Example"""

        t1 = "Projectname: " + self.ui.projectname.text()
        t2= "SMT path: " + os.path.basename(self.slidmasttab_path)
        t3= "PMT path: " + os.path.basename(self.patmasttab_path)
        t4 = "folderpath: " + self.folderpath_path
        t5 = "chosen target(s): " + str([str(x.text()) for x in self.ui.choosetarg.selectedItems()])

        text= t1 + "\n \n" + t2 + "\n \n" + t3 + "\n \n" + t4 + "\n \n" + t5
        self.ui.fileexample.setText(text)

    def resetbutton_click(self):
        self.ui.projectname.clear()
        self.slidmasttab_path = "-"
        self.patmasttab_path = "-"
        self.folderpath_path = "-"
        self.ui.choosetarg.clear()
        self.testbutton_click()
app = QtWidgets.QApplication(sys.argv)
widget = Mainwindow_con()
widget.show()

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from package.mainwindow import Ui_gui_histo_main

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
        self.ui.testbutton.clicked.connect(self.testbutton)
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

    def open_patmasttab(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open a file', "/GUI_deephist_python/cliniData",
                                                "*.xlsx")
        if path != ('', ''):
            self.patmasttab_path = path[0]

    def open_folderpath(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self,"\home")
        if path != ('', ''):
            self.folderpath_path = path

    def testbutton(self):
        """testbutton on first page, if clicked, shows the File Example"""

        t1 = "Projectname =" + self.ui.projectname.text()
        t2= "SMT path= " + self.slidmasttab_path
        t3= "PMT path= " + self.patmasttab_path
        t4 = "folderpath= " + self.folderpath_path
        text= t1 + "\n" + t2 + "\n" + t3 + "\n" + t4
        self.ui.fileexample.setText(text)

app = QtWidgets.QApplication(sys.argv)
widget = Mainwindow_con()
widget.show()

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from package.mainwindow import Ui_gui_histo_main
from package.advanced_settings import Ui_advanced_settings
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


        self.ui.advanced_sets.clicked.connect(self.advanced_sets_clicked)
        ###########

        #Events autoDeeplearn
        ###########
        # Events autoDeploy
        ###########
        # Events autoVisualize
        ###########

    def advanced_sets_clicked(self, checked=None):
        if checked == None: return
        dialog = QtWidgets.QDialog()
        dialog.ui = Ui_advanced_settings()
        dialog.ui.setupUi(dialog)
        dialog.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        dialog.exec_()


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

    def runbutton_click(self):
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


app = QtWidgets.QApplication(sys.argv)
widget = Mainwindow_con()
widget.show()

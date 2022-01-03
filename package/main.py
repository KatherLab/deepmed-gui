# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader


class gui_histo_main(QMainWindow):
    def __init__(self):
        super(gui_histo_main, self).__init__()
        #self.setWindowTitle("My App")
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self).show()
        ui_file.close()

        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "cohortwindow.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self).show()
        ui_file.close()

        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "addtarget.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self).show()
        ui_file.close()

        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "advanced_settings.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self).show()
        ui_file.close()



if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    widget = gui_histo_main()
    #widget.show() instead loader gets .show()
    sys.exit(app.exec_())


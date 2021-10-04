from PyQt5 import QtWidgets
from package.deephist import Mainwindow_con
import sys


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = Mainwindow_con()
    widget.show()
    sys.exit(app.exec_())



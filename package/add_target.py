# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtarget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_add_target(object):
    def setupUi(self, Ui_add_target):
        Ui_add_target.setObjectName("Ui_add_target")
        Ui_add_target.resize(375, 401)
        self.verticalLayoutWidget = QtWidgets.QWidget(Ui_add_target)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 354, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 3, 1, 1)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 6)
        self.groups = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.groups.setObjectName("groups")
        self.gridLayout.addWidget(self.groups, 5, 0, 1, 6)
        self.min_val = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.min_val.setEnabled(False)
        self.min_val.setObjectName("min_val")
        self.gridLayout.addWidget(self.min_val, 9, 2, 1, 1)
        self.threshold_value = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.threshold_value.setEnabled(False)
        self.threshold_value.setObjectName("threshold_value")
        self.gridLayout.addWidget(self.threshold_value, 10, 2, 1, 3)
        self.threshold_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.threshold_label.setEnabled(False)
        self.threshold_label.setObjectName("threshold_label")
        self.gridLayout.addWidget(self.threshold_label, 10, 0, 1, 2)
        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 12, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 7)
        self.min_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.min_label.setEnabled(False)
        self.min_label.setObjectName("min_label")
        self.gridLayout.addWidget(self.min_label, 9, 0, 1, 2)
        self.max_val = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.max_val.setEnabled(False)
        self.max_val.setObjectName("max_val")
        self.gridLayout.addWidget(self.max_val, 9, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 5, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 12, 4, 1, 1)
        self.max_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.max_label.setEnabled(False)
        self.max_label.setObjectName("max_label")
        self.gridLayout.addWidget(self.max_label, 9, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 11, 0, 1, 1)
        self.newname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.newname.setObjectName("newname")
        self.gridLayout.addWidget(self.newname, 11, 2, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Ui_add_target)
        QtCore.QMetaObject.connectSlotsByName(Ui_add_target)

    def retranslateUi(self, Ui_add_target):
        _translate = QtCore.QCoreApplication.translate
        Ui_add_target.setWindowTitle(_translate("Ui_add_target", "Add Target"))
        self.min_val.setText(_translate("Ui_add_target", "-"))
        self.threshold_label.setText(_translate("Ui_add_target", "threshold:"))
        self.cancel_button.setText(_translate("Ui_add_target", "Cancel"))
        self.label_6.setText(_translate("Ui_add_target", "Binary Categorisation :"))
        self.label_4.setText(_translate("Ui_add_target", "Creat binary feature from discrete features"))
        self.min_label.setText(_translate("Ui_add_target", "min:"))
        self.max_val.setText(_translate("Ui_add_target", "-"))
        self.save_button.setText(_translate("Ui_add_target", "Save"))
        self.max_label.setText(_translate("Ui_add_target", "max:"))
        self.label.setText(_translate("Ui_add_target", "Categories:"))
        self.label_2.setText(_translate("Ui_add_target", "new target name:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_add_target = QtWidgets.QDialog()
    ui = Ui_Ui_add_target()
    ui.setupUi(Ui_add_target)
    Ui_add_target.show()
    sys.exit(app.exec_())


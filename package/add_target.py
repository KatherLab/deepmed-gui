# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtarget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cohort_settings(object):
    def setupUi(self, cohort_settings):
        cohort_settings.setObjectName("cohort_settings")
        cohort_settings.resize(605, 369)
        self.verticalLayoutWidget = QtWidgets.QWidget(cohort_settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
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
        self.threshold_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.threshold_label.setEnabled(False)
        self.threshold_label.setObjectName("threshold_label")
        self.gridLayout.addWidget(self.threshold_label, 10, 0, 1, 2)
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
        self.threshold_value = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.threshold_value.setEnabled(False)
        self.threshold_value.setObjectName("threshold_value")
        self.gridLayout.addWidget(self.threshold_value, 10, 2, 1, 1)
        self.max_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.max_label.setEnabled(False)
        self.max_label.setObjectName("max_label")
        self.gridLayout.addWidget(self.max_label, 9, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 9, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 7, 5, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.verticalLayout.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayout.addWidget(self.cancel_button)

        self.retranslateUi(cohort_settings)
        QtCore.QMetaObject.connectSlotsByName(cohort_settings)

    def retranslateUi(self, cohort_settings):
        _translate = QtCore.QCoreApplication.translate
        cohort_settings.setWindowTitle(_translate("cohort_settings", "Cohort Subgrouping"))
        self.min_val.setText(_translate("cohort_settings", "-"))
        self.threshold_label.setText(_translate("cohort_settings", "threshold:"))
        self.label_6.setText(_translate("cohort_settings", "Binary Categorisation :"))
        self.label_4.setText(_translate("cohort_settings", "Creat binary feature from discrete features"))
        self.min_label.setText(_translate("cohort_settings", "min:"))
        self.max_val.setText(_translate("cohort_settings", "-"))
        self.max_label.setText(_translate("cohort_settings", "max:"))
        self.label.setText(_translate("cohort_settings", "Categories:"))
        self.save_button.setText(_translate("cohort_settings", "Save"))
        self.cancel_button.setText(_translate("cohort_settings", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    cohort_settings = QtWidgets.QDialog()
    ui = Ui_cohort_settings()
    ui.setupUi(cohort_settings)
    cohort_settings.show()
    sys.exit(app.exec_())


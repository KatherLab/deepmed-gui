# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cohortwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_cohort_settings(object):
    def setupUi(self, cohort_settings):
        cohort_settings.setObjectName("cohort_settings")
        cohort_settings.resize(622, 547)
        self.verticalLayoutWidget = QtWidgets.QWidget(cohort_settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 607, 533))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.max_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.max_label.setEnabled(False)
        self.max_label.setObjectName("max_label")
        self.gridLayout.addWidget(self.max_label, 11, 3, 1, 1)
        self.or_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.or_button.setObjectName("or_button")
        self.gridLayout.addWidget(self.or_button, 6, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)
        self.threshold_value = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.threshold_value.setEnabled(False)
        self.threshold_value.setObjectName("threshold_value")
        self.gridLayout.addWidget(self.threshold_value, 13, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 12, 0, 1, 1)
        self.min_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.min_label.setEnabled(False)
        self.min_label.setObjectName("min_label")
        self.gridLayout.addWidget(self.min_label, 11, 0, 1, 2)
        self.threshold_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.threshold_label.setEnabled(False)
        self.threshold_label.setObjectName("threshold_label")
        self.gridLayout.addWidget(self.threshold_label, 13, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 6)
        self.min_val = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.min_val.setEnabled(False)
        self.min_val.setObjectName("min_val")
        self.gridLayout.addWidget(self.min_val, 11, 2, 1, 1)
        self.querybox = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.querybox.setObjectName("querybox")
        self.gridLayout.addWidget(self.querybox, 18, 0, 1, 5)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 15, 0, 1, 1)
        self.groups = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.groups.setObjectName("groups")
        self.gridLayout.addWidget(self.groups, 5, 0, 1, 5)
        self.subgroups = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.subgroups.setEnabled(False)
        self.subgroups.setObjectName("subgroups")
        self.gridLayout.addWidget(self.subgroups, 7, 0, 1, 5)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.and_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.and_button.setObjectName("and_button")
        self.gridLayout.addWidget(self.and_button, 5, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 16, 0, 1, 1)
        self.max_val = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.max_val.setEnabled(False)
        self.max_val.setObjectName("max_val")
        self.gridLayout.addWidget(self.max_val, 11, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 7, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 17, 0, 1, 5)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 8, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 13, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.save_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.cancel_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(cohort_settings)
        QtCore.QMetaObject.connectSlotsByName(cohort_settings)

    def retranslateUi(self, cohort_settings):
        _translate = QtCore.QCoreApplication.translate
        cohort_settings.setWindowTitle(_translate("cohort_settings", "Cohort Subgrouping"))
        self.max_label.setText(_translate("cohort_settings", "max"))
        self.or_button.setText(_translate("cohort_settings", "or"))
        self.label_7.setText(_translate("cohort_settings", "Operator:"))
        self.min_label.setText(_translate("cohort_settings", "min"))
        self.threshold_label.setText(_translate("cohort_settings", "threshold"))
        self.label_4.setText(_translate("cohort_settings", "Creat subcategories"))
        self.min_val.setText(_translate("cohort_settings", "-"))
        self.label.setText(_translate("cohort_settings", "Categories:"))
        self.and_button.setText(_translate("cohort_settings", "and"))
        self.max_val.setText(_translate("cohort_settings", "-"))
        self.label_6.setText(_translate("cohort_settings", "Binary Categorisation of continous values:"))
        self.back_button.setText(_translate("cohort_settings", "back"))
        self.label_5.setText(_translate("cohort_settings", "Sub Categories:"))
        self.label_3.setText(_translate("cohort_settings", "Querybox"))
        self.pushButton.setText(_translate("cohort_settings", "<"))
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


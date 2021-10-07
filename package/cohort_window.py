# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cohortwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_cohort_settings(object):
    def setupUi(self, cohort_settings):
        cohort_settings.setObjectName("cohort_settings")
        cohort_settings.resize(492, 408)
        self.verticalLayoutWidget = QtWidgets.QWidget(cohort_settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 449, 390))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)
        self.query_box = QtWidgets.QListView(self.verticalLayoutWidget)
        self.query_box.setObjectName("query_box")
        self.gridLayout.addWidget(self.query_box, 10, 0, 1, 3)
        self.back_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 5, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.and_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.and_button.setObjectName("and_button")
        self.gridLayout.addWidget(self.and_button, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.groups = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.groups.setObjectName("groups")
        self.gridLayout.addWidget(self.groups, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 8, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 5, 0, 1, 1)
        self.or_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.or_button.setObjectName("or_button")
        self.gridLayout.addWidget(self.or_button, 4, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)
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
        self.label_4.setText(_translate("cohort_settings", "Creat subcategories"))
        self.back_button.setText(_translate("cohort_settings", "back"))
        self.label_3.setText(_translate("cohort_settings", "Querybox"))
        self.label_7.setText(_translate("cohort_settings", "Operator:"))
        self.label.setText(_translate("cohort_settings", "Categories:"))
        self.and_button.setText(_translate("cohort_settings", "and"))
        self.label_5.setText(_translate("cohort_settings", "Sub Categories:"))
        self.or_button.setText(_translate("cohort_settings", "or"))
        self.reset_button.setText(_translate("cohort_settings", "Reset"))
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

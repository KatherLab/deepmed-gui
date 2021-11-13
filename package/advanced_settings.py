# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advanced_settings.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_advanced_settings(object):
    def setupUi(self, advanced_settings):
        advanced_settings.setObjectName("advanced_settings")
        advanced_settings.resize(390, 391)
        self.verticalLayoutWidget = QtWidgets.QWidget(advanced_settings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 376))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.maxTileNum = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.maxTileNum.setMaximum(1000000000)
        self.maxTileNum.setProperty("value", 3)
        self.maxTileNum.setObjectName("maxTileNum")
        self.gridLayout.addWidget(self.maxTileNum, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.GPUnum = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.GPUnum.setProperty("value", 3)
        self.GPUnum.setObjectName("GPUnum")
        self.gridLayout.addWidget(self.GPUnum, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.batch_size = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.batch_size.setMaximum(100000000)
        self.batch_size.setProperty("value", 99)
        self.batch_size.setObjectName("batch_size")
        self.gridLayout.addWidget(self.batch_size, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.max_epochs = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.max_epochs.setProperty("value", 10)
        self.max_epochs.setObjectName("max_epochs")
        self.gridLayout.addWidget(self.max_epochs, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.workers = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.workers.setProperty("value", 8)
        self.workers.setObjectName("workers")
        self.gridLayout.addWidget(self.workers, 5, 1, 1, 1)
        self.conc_tasks = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.conc_tasks.setObjectName("conc_tasks")
        self.gridLayout.addWidget(self.conc_tasks, 6, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.na_settings = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.na_settings.setReadOnly(False)
        self.na_settings.setObjectName("na_settings")
        self.verticalLayout.addWidget(self.na_settings)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_advancedDL = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reset_advancedDL.setObjectName("reset_advancedDL")
        self.horizontalLayout.addWidget(self.reset_advancedDL)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.save_advancedDL = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save_advancedDL.setObjectName("save_advancedDL")
        self.horizontalLayout.addWidget(self.save_advancedDL)
        self.cancel_advancedDL = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.cancel_advancedDL.setObjectName("cancel_advancedDL")
        self.horizontalLayout.addWidget(self.cancel_advancedDL)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(advanced_settings)
        QtCore.QMetaObject.connectSlotsByName(advanced_settings)

    def retranslateUi(self, advanced_settings):
        _translate = QtCore.QCoreApplication.translate
        advanced_settings.setWindowTitle(_translate("advanced_settings", "Advanced Settings"))
        self.label_4.setText(_translate("advanced_settings", "max tile num "))
        self.label.setText(_translate("advanced_settings", "Advanced Settings"))
        self.label_3.setText(_translate("advanced_settings", "Number of GPUs"))
        self.label_2.setText(_translate("advanced_settings", "batch size "))
        self.label_6.setText(_translate("advanced_settings", "max epochs"))
        self.label_5.setText(_translate("advanced_settings", "number of workers"))
        self.label_7.setText(_translate("advanced_settings", "concurrent tasks"))
        self.label_8.setText(_translate("advanced_settings", "Exclude values:"))
        self.na_settings.setHtml(_translate("advanced_settings", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'JetBrains Mono\',\'monospace\'; color:#a9b7c6;\">[\'NA\', \'Not Available\', \'Equivocal\', \'Not Performed\', \'unknown\']</span></p></body></html>"))
        self.reset_advancedDL.setText(_translate("advanced_settings", "Reset"))
        self.save_advancedDL.setText(_translate("advanced_settings", "Save"))
        self.cancel_advancedDL.setText(_translate("advanced_settings", "Cancel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    advanced_settings = QtWidgets.QDialog()
    ui = Ui_advanced_settings()
    ui.setupUi(advanced_settings)
    advanced_settings.show()
    sys.exit(app.exec_())


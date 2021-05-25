# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advanced_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


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
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 7, 1, 1, 1)
        self.GPUnum = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.GPUnum.setObjectName("GPUnum")
        self.gridLayout.addWidget(self.GPUnum, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout.addWidget(self.doubleSpinBox, 5, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.verticalLayoutWidget)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 6, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 0, 1, 1)
        self.binarize_quantile = QtWidgets.QSlider(self.verticalLayoutWidget)
        self.binarize_quantile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.binarize_quantile.setAutoFillBackground(False)
        self.binarize_quantile.setInputMethodHints(QtCore.Qt.ImhNone)
        self.binarize_quantile.setProperty("value", 80)
        self.binarize_quantile.setSliderPosition(80)
        self.binarize_quantile.setTracking(True)
        self.binarize_quantile.setOrientation(QtCore.Qt.Horizontal)
        self.binarize_quantile.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.binarize_quantile.setTickInterval(10)
        self.binarize_quantile.setObjectName("binarize_quantile")
        self.gridLayout.addWidget(self.binarize_quantile, 2, 1, 1, 1)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setProperty("value", 3)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout.addWidget(self.spinBox, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reset_advancedDL = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.reset_advancedDL.setObjectName("reset_advancedDL")
        self.horizontalLayout.addWidget(self.reset_advancedDL)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
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
        advanced_settings.setWindowTitle(_translate("advanced_settings", "Dialog"))
        self.label.setText(_translate("advanced_settings", "Advanced Settings"))
        self.radioButton.setText(_translate("advanced_settings", "RadioButton"))
        self.label_7.setText(_translate("advanced_settings", "more sets"))
        self.label_2.setText(_translate("advanced_settings", "train/test ratio"))
        self.checkBox.setText(_translate("advanced_settings", "cross validation"))
        self.label_3.setText(_translate("advanced_settings", "Number of GPUs"))
        self.label_6.setText(_translate("advanced_settings", "more sets"))
        self.label_5.setText(_translate("advanced_settings", "more sets"))
        self.textBrowser.setHtml(_translate("advanced_settings", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Welcome to the advance settings.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p></body></html>"))
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

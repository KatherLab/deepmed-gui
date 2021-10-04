# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_gui_histo_main(object):
    def setupUi(self, gui_histo_main):
        gui_histo_main.setObjectName("gui_histo_main")
        gui_histo_main.resize(916, 696)
        gui_histo_main.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(gui_histo_main)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setKerning(False)
        self.Tabs.setFont(font)
        self.Tabs.setToolTip("")
        self.Tabs.setIconSize(QtCore.QSize(16, 16))
        self.Tabs.setObjectName("Tabs")
        self.Deeplearn = QtWidgets.QWidget()
        self.Deeplearn.setAccessibleName("")
        self.Deeplearn.setAutoFillBackground(False)
        self.Deeplearn.setObjectName("Deeplearn")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Deeplearn)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.Deeplearn)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 19, 0, 1, 1)
        self.kfolds_DL = QtWidgets.QSpinBox(self.Deeplearn)
        self.kfolds_DL.setEnabled(False)
        self.kfolds_DL.setProperty("value", 3)
        self.kfolds_DL.setObjectName("kfolds_DL")
        self.gridLayout.addWidget(self.kfolds_DL, 9, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.Deeplearn)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 12, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.Deeplearn)
        self.label_5.setEnabled(False)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 3, 1, 1)
        self.advanced_sets_DL = QtWidgets.QPushButton(self.Deeplearn)
        self.advanced_sets_DL.setObjectName("advanced_sets_DL")
        self.gridLayout.addWidget(self.advanced_sets_DL, 21, 4, 1, 1)
        self.reset_DL = QtWidgets.QPushButton(self.Deeplearn)
        self.reset_DL.setObjectName("reset_DL")
        self.gridLayout.addWidget(self.reset_DL, 21, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Deeplearn)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.Deeplearn)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 13, 0, 1, 1)
        self.GPU_num_DL = QtWidgets.QSpinBox(self.Deeplearn)
        self.GPU_num_DL.setProperty("value", 3)
        self.GPU_num_DL.setObjectName("GPU_num_DL")
        self.gridLayout.addWidget(self.GPU_num_DL, 3, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.Deeplearn)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 2, 0, 1, 1)
        self.batch_size_DL = QtWidgets.QSpinBox(self.Deeplearn)
        self.batch_size_DL.setMaximum(99999)
        self.batch_size_DL.setProperty("value", 64)
        self.batch_size_DL.setObjectName("batch_size_DL")
        self.gridLayout.addWidget(self.batch_size_DL, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.Deeplearn)
        self.label_4.setEnabled(True)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 3, 1, 1)
        self.tilespath_DL = QtWidgets.QPushButton(self.Deeplearn)
        self.tilespath_DL.setObjectName("tilespath_DL")
        self.gridLayout.addWidget(self.tilespath_DL, 14, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.Deeplearn)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.Deeplearn)
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 4, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.Deeplearn)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 16, 0, 1, 1)
        self.gpunum_label = QtWidgets.QLabel(self.Deeplearn)
        self.gpunum_label.setObjectName("gpunum_label")
        self.gridLayout.addWidget(self.gpunum_label, 3, 3, 1, 1)
        self.project_name_DL = QtWidgets.QLineEdit(self.Deeplearn)
        self.project_name_DL.setObjectName("project_name_DL")
        self.gridLayout.addWidget(self.project_name_DL, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.Deeplearn)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 3, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.Deeplearn)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 11, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.Deeplearn)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 14, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.Deeplearn)
        self.label_15.setToolTip("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.Deeplearn)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 11, 4, 1, 1)
        self.run_DL = QtWidgets.QPushButton(self.Deeplearn)
        self.run_DL.setObjectName("run_DL")
        self.gridLayout.addWidget(self.run_DL, 21, 1, 1, 1)
        self.maxTileNum_DL = QtWidgets.QSpinBox(self.Deeplearn)
        self.maxTileNum_DL.setMaximum(99999)
        self.maxTileNum_DL.setProperty("value", 20)
        self.maxTileNum_DL.setObjectName("maxTileNum_DL")
        self.gridLayout.addWidget(self.maxTileNum_DL, 3, 1, 1, 1)
        self.savingpath_DL = QtWidgets.QPushButton(self.Deeplearn)
        self.savingpath_DL.setObjectName("savingpath_DL")
        self.gridLayout.addWidget(self.savingpath_DL, 19, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.Deeplearn)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 10, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.Deeplearn)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 3, 0, 1, 1)
        self.clini_table_DL = QtWidgets.QPushButton(self.Deeplearn)
        self.clini_table_DL.setObjectName("clini_table_DL")
        self.gridLayout.addWidget(self.clini_table_DL, 13, 1, 1, 1)
        self.slide_masttab_DL = QtWidgets.QPushButton(self.Deeplearn)
        self.slide_masttab_DL.setObjectName("slide_masttab_DL")
        self.gridLayout.addWidget(self.slide_masttab_DL, 12, 1, 1, 1)
        self.label_settings = QtWidgets.QLabel(self.Deeplearn)
        self.label_settings.setObjectName("label_settings")
        self.gridLayout.addWidget(self.label_settings, 0, 0, 1, 1)
        self.max_epochs_DL = QtWidgets.QSpinBox(self.Deeplearn)
        self.max_epochs_DL.setMinimum(2)
        self.max_epochs_DL.setMaximum(1030)
        self.max_epochs_DL.setProperty("value", 13)
        self.max_epochs_DL.setObjectName("max_epochs_DL")
        self.gridLayout.addWidget(self.max_epochs_DL, 2, 4, 1, 1)
        self.choosemode_DL = QtWidgets.QComboBox(self.Deeplearn)
        self.choosemode_DL.setObjectName("choosemode_DL")
        self.choosemode_DL.addItem("")
        self.choosemode_DL.addItem("")
        self.gridLayout.addWidget(self.choosemode_DL, 7, 1, 1, 1)
        self.traintestratio_DL = QtWidgets.QSlider(self.Deeplearn)
        self.traintestratio_DL.setEnabled(True)
        self.traintestratio_DL.setProperty("value", 80)
        self.traintestratio_DL.setOrientation(QtCore.Qt.Horizontal)
        self.traintestratio_DL.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.traintestratio_DL.setObjectName("traintestratio_DL")
        self.gridLayout.addWidget(self.traintestratio_DL, 7, 4, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.Deeplearn)
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 15, 0, 1, 1)
        self.choosetarg_DL = QtWidgets.QListWidget(self.Deeplearn)
        self.choosetarg_DL.setEnabled(False)
        self.choosetarg_DL.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.choosetarg_DL.setObjectName("choosetarg_DL")
        self.gridLayout.addWidget(self.choosetarg_DL, 16, 1, 2, 1)
        self.trainfull_DL = QtWidgets.QCheckBox(self.Deeplearn)
        self.trainfull_DL.setObjectName("trainfull_DL")
        self.gridLayout.addWidget(self.trainfull_DL, 9, 1, 1, 1)
        self.cohort_list_DL = QtWidgets.QListWidget(self.Deeplearn)
        self.cohort_list_DL.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.cohort_list_DL.setObjectName("cohort_list_DL")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled)
        self.cohort_list_DL.addItem(item)
        self.gridLayout.addWidget(self.cohort_list_DL, 12, 4, 3, 1)
        self.addcohortlist_DL = QtWidgets.QPushButton(self.Deeplearn)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/right-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addcohortlist_DL.setIcon(icon)
        self.addcohortlist_DL.setObjectName("addcohortlist_DL")
        self.gridLayout.addWidget(self.addcohortlist_DL, 13, 2, 1, 2)
        self.del_list_DL = QtWidgets.QPushButton(self.Deeplearn)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_list_DL.setIcon(icon1)
        self.del_list_DL.setIconSize(QtCore.QSize(13, 13))
        self.del_list_DL.setObjectName("del_list_DL")
        self.gridLayout.addWidget(self.del_list_DL, 14, 2, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 12, 2, 1, 1)
        self.test_dl = QtWidgets.QPushButton(self.Deeplearn)
        self.test_dl.setObjectName("test_dl")
        self.gridLayout.addWidget(self.test_dl, 19, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.Tabs.addTab(self.Deeplearn, "")
        self.Deploy = QtWidgets.QWidget()
        self.Deploy.setObjectName("Deploy")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Deploy)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.choose_slidetable_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.choose_slidetable_Deploy.setObjectName("choose_slidetable_Deploy")
        self.gridLayout_2.addWidget(self.choose_slidetable_Deploy, 9, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.Deploy)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 3, 0, 1, 1)
        self.projectdir_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.projectdir_Deploy.setObjectName("projectdir_Deploy")
        self.gridLayout_2.addWidget(self.projectdir_Deploy, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.Deploy)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 11, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.Deploy)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 0, 1, 1)
        self.run_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.run_Deploy.setObjectName("run_Deploy")
        self.gridLayout_2.addWidget(self.run_Deploy, 16, 1, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.Deploy)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 7, 0, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.Deploy)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 4, 0, 1, 1)
        self.maxtilenum_Deploy = QtWidgets.QSpinBox(self.Deploy)
        self.maxtilenum_Deploy.setMaximum(99999)
        self.maxtilenum_Deploy.setProperty("value", 20)
        self.maxtilenum_Deploy.setObjectName("maxtilenum_Deploy")
        self.gridLayout_2.addWidget(self.maxtilenum_Deploy, 4, 1, 1, 1)
        self.targetlabels2_Deploy = QtWidgets.QListWidget(self.Deploy)
        self.targetlabels2_Deploy.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.targetlabels2_Deploy.setObjectName("targetlabels2_Deploy")
        self.gridLayout_2.addWidget(self.targetlabels2_Deploy, 15, 1, 1, 1)
        self.groups_Deploy = QtWidgets.QCheckBox(self.Deploy)
        self.groups_Deploy.setObjectName("groups_Deploy")
        self.gridLayout_2.addWidget(self.groups_Deploy, 14, 0, 1, 1)
        self.clini_table_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.clini_table_Deploy.setObjectName("clini_table_Deploy")
        self.gridLayout_2.addWidget(self.clini_table_Deploy, 10, 1, 1, 1)
        self.targetlabels_Deploy = QtWidgets.QListWidget(self.Deploy)
        self.targetlabels_Deploy.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.targetlabels_Deploy.setObjectName("targetlabels_Deploy")
        self.gridLayout_2.addWidget(self.targetlabels_Deploy, 15, 0, 1, 1)
        self.del_list_deploy = QtWidgets.QPushButton(self.Deploy)
        self.del_list_deploy.setIcon(icon1)
        self.del_list_deploy.setIconSize(QtCore.QSize(13, 13))
        self.del_list_deploy.setObjectName("del_list_deploy")
        self.gridLayout_2.addWidget(self.del_list_deploy, 11, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 2, 1, 1)
        self.batchsize_Deploy = QtWidgets.QSpinBox(self.Deploy)
        self.batchsize_Deploy.setMaximum(99999)
        self.batchsize_Deploy.setProperty("value", 64)
        self.batchsize_Deploy.setObjectName("batchsize_Deploy")
        self.gridLayout_2.addWidget(self.batchsize_Deploy, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 15, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.Deploy)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 7, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.Deploy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 10, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.Deploy)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 13, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.Deploy)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)
        self.cohortlist_Deploy = QtWidgets.QListWidget(self.Deploy)
        self.cohortlist_Deploy.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.cohortlist_Deploy.setObjectName("cohortlist_Deploy")
        self.gridLayout_2.addWidget(self.cohortlist_Deploy, 9, 3, 3, 1)
        self.choose_tiledir_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.choose_tiledir_Deploy.setObjectName("choose_tiledir_Deploy")
        self.gridLayout_2.addWidget(self.choose_tiledir_Deploy, 11, 1, 1, 1)
        self.choose_model_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.choose_model_Deploy.setObjectName("choose_model_Deploy")
        self.gridLayout_2.addWidget(self.choose_model_Deploy, 5, 1, 1, 1)
        self.addlist_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.addlist_Deploy.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addlist_Deploy.sizePolicy().hasHeightForWidth())
        self.addlist_Deploy.setSizePolicy(sizePolicy)
        self.addlist_Deploy.setMinimumSize(QtCore.QSize(0, 32))
        self.addlist_Deploy.setStyleSheet("")
        self.addlist_Deploy.setIcon(icon)
        self.addlist_Deploy.setObjectName("addlist_Deploy")
        self.gridLayout_2.addWidget(self.addlist_Deploy, 10, 2, 1, 1)
        self.reset_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.reset_Deploy.setObjectName("reset_Deploy")
        self.gridLayout_2.addWidget(self.reset_Deploy, 16, 0, 1, 1)
        self.subgroups_Deploy = QtWidgets.QCheckBox(self.Deploy)
        self.subgroups_Deploy.setObjectName("subgroups_Deploy")
        self.gridLayout_2.addWidget(self.subgroups_Deploy, 14, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.Deploy)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 9, 0, 1, 1)
        self.advanced_Deploy = QtWidgets.QPushButton(self.Deploy)
        self.advanced_Deploy.setObjectName("advanced_Deploy")
        self.gridLayout_2.addWidget(self.advanced_Deploy, 16, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.Deploy)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 5, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 6, 1, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_2)
        self.Tabs.addTab(self.Deploy, "")
        self.Visualize = QtWidgets.QWidget()
        self.Visualize.setObjectName("Visualize")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.Visualize)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_16 = QtWidgets.QLabel(self.Visualize)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.Visualize)
        self.tabWidget.setObjectName("tabWidget")
        self.vis_plots = QtWidgets.QWidget()
        self.vis_plots.setObjectName("vis_plots")
        self.gridLayoutWidget = QtWidgets.QWidget(self.vis_plots)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-1, -21, 841, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 2, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 2, 1, 1, 1)
        self.listIm_Vis = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.listIm_Vis.setObjectName("listIm_Vis")
        self.gridLayout_4.addWidget(self.listIm_Vis, 2, 3, 1, 1)
        self.openFolder_Vis = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openFolder_Vis.setObjectName("openFolder_Vis")
        self.gridLayout_4.addWidget(self.openFolder_Vis, 1, 3, 1, 1)
        self.nextIm_Vis = QtWidgets.QPushButton(self.gridLayoutWidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/r_arr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nextIm_Vis.setIcon(icon2)
        self.nextIm_Vis.setObjectName("nextIm_Vis")
        self.gridLayout_4.addWidget(self.nextIm_Vis, 1, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)
        self.imgcounter_Vis = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.imgcounter_Vis.setFrameShape(QtWidgets.QFrame.Box)
        self.imgcounter_Vis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgcounter_Vis.setDigitCount(5)
        self.imgcounter_Vis.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.imgcounter_Vis.setProperty("value", 0.0)
        self.imgcounter_Vis.setProperty("intValue", 0)
        self.imgcounter_Vis.setObjectName("imgcounter_Vis")
        self.gridLayout_4.addWidget(self.imgcounter_Vis, 2, 0, 1, 1)
        self.prevIm_Vis = QtWidgets.QPushButton(self.gridLayoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/l_arr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.prevIm_Vis.setIcon(icon3)
        self.prevIm_Vis.setObjectName("prevIm_Vis")
        self.gridLayout_4.addWidget(self.prevIm_Vis, 1, 1, 1, 1)
        self.imglist_Vis = QtWidgets.QListView(self.gridLayoutWidget)
        self.imglist_Vis.setObjectName("imglist_Vis")
        self.gridLayout_4.addWidget(self.imglist_Vis, 3, 3, 1, 1)
        self.imgwindow_Vis = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.imgwindow_Vis.setObjectName("imgwindow_Vis")
        self.gridLayout_4.addWidget(self.imgwindow_Vis, 3, 0, 1, 3)
        self.label_17 = QtWidgets.QLabel(self.vis_plots)
        self.label_17.setGeometry(QtCore.QRect(19, 450, 111, 20))
        self.label_17.setObjectName("label_17")
        self.shortcutlabel = QtWidgets.QLabel(self.vis_plots)
        self.shortcutlabel.setGeometry(QtCore.QRect(100, 450, 731, 20))
        self.shortcutlabel.setObjectName("shortcutlabel")
        self.tabWidget.addTab(self.vis_plots, "")
        self.vis_tables = QtWidgets.QWidget()
        self.vis_tables.setObjectName("vis_tables")
        self.table_Vis = QtWidgets.QTableView(self.vis_tables)
        self.table_Vis.setGeometry(QtCore.QRect(-5, 41, 851, 431))
        self.table_Vis.setObjectName("table_Vis")
        self.choosetable_Vis = QtWidgets.QPushButton(self.vis_tables)
        self.choosetable_Vis.setGeometry(QtCore.QRect(720, 0, 113, 32))
        self.choosetable_Vis.setObjectName("choosetable_Vis")
        self.tabWidget.addTab(self.vis_tables, "")
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 3)
        self.fldrpth_Vis = QtWidgets.QPushButton(self.Visualize)
        self.fldrpth_Vis.setObjectName("fldrpth_Vis")
        self.gridLayout_3.addWidget(self.fldrpth_Vis, 2, 1, 1, 1)
        self.format_Vis = QtWidgets.QComboBox(self.Visualize)
        self.format_Vis.setObjectName("format_Vis")
        self.format_Vis.addItem("")
        self.format_Vis.addItem("")
        self.format_Vis.addItem("")
        self.gridLayout_3.addWidget(self.format_Vis, 1, 2, 1, 1)
        self.save_all_Vis = QtWidgets.QCheckBox(self.Visualize)
        self.save_all_Vis.setObjectName("save_all_Vis")
        self.gridLayout_3.addWidget(self.save_all_Vis, 1, 0, 1, 1)
        self.save_Vis = QtWidgets.QPushButton(self.Visualize)
        self.save_Vis.setObjectName("save_Vis")
        self.gridLayout_3.addWidget(self.save_Vis, 2, 2, 1, 1)
        self.horizontalLayout_7.addLayout(self.gridLayout_3)
        self.Tabs.addTab(self.Visualize, "")
        self.horizontalLayout_2.addWidget(self.Tabs)
        gui_histo_main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(gui_histo_main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 916, 22))
        self.menubar.setObjectName("menubar")
        self.menuhello = QtWidgets.QMenu(self.menubar)
        self.menuhello.setObjectName("menuhello")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        gui_histo_main.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(gui_histo_main)
        self.toolBar.setObjectName("toolBar")
        gui_histo_main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit_Deep_Histology = QtWidgets.QAction(gui_histo_main)
        self.actionQuit_Deep_Histology.setObjectName("actionQuit_Deep_Histology")
        self.actionPreferences = QtWidgets.QAction(gui_histo_main)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionNew_Experiment = QtWidgets.QAction(gui_histo_main)
        self.actionNew_Experiment.setObjectName("actionNew_Experiment")
        self.actionOpen_Experiment = QtWidgets.QAction(gui_histo_main)
        self.actionOpen_Experiment.setObjectName("actionOpen_Experiment")
        self.actionMenu = QtWidgets.QAction(gui_histo_main)
        self.actionMenu.setObjectName("actionMenu")
        self.actionGithub_Documentation = QtWidgets.QAction(gui_histo_main)
        self.actionGithub_Documentation.setObjectName("actionGithub_Documentation")
        self.actionTutorial = QtWidgets.QAction(gui_histo_main)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionarr = QtWidgets.QAction(gui_histo_main)
        self.actionarr.setObjectName("actionarr")
        self.menuhello.addSeparator()
        self.menuhello.addAction(self.actionPreferences)
        self.menuhello.addAction(self.actionQuit_Deep_Histology)
        self.menuFile.addAction(self.actionNew_Experiment)
        self.menuFile.addAction(self.actionOpen_Experiment)
        self.menuEdit.addAction(self.actionMenu)
        self.menuHelp.addAction(self.actionGithub_Documentation)
        self.menuHelp.addAction(self.actionTutorial)
        self.menubar.addAction(self.menuhello.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(gui_histo_main)
        self.Tabs.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(gui_histo_main)

    def retranslateUi(self, gui_histo_main):
        _translate = QtCore.QCoreApplication.translate
        gui_histo_main.setWindowTitle(_translate("gui_histo_main", "Deep Histology v1.0"))
        self.label_12.setText(_translate("gui_histo_main", "saving path"))
        self.label_8.setText(_translate("gui_histo_main", "slide table"))
        self.label_5.setText(_translate("gui_histo_main", "k-folds"))
        self.advanced_sets_DL.setText(_translate("gui_histo_main", "advanced settings"))
        self.reset_DL.setText(_translate("gui_histo_main", "reset"))
        self.label_6.setText(_translate("gui_histo_main", "Mode Settings:"))
        self.label_9.setText(_translate("gui_histo_main", "clini table"))
        self.label_18.setText(_translate("gui_histo_main", "batch size"))
        self.label_4.setText(_translate("gui_histo_main", "validation ratio"))
        self.tilespath_DL.setText(_translate("gui_histo_main", "choose path"))
        self.label_3.setText(_translate("gui_histo_main", "mode"))
        self.label_19.setText(_translate("gui_histo_main", "Choose targets:"))
        self.gpunum_label.setText(_translate("gui_histo_main", "GPU num"))
        self.project_name_DL.setToolTip(_translate("gui_histo_main", "pick a project name."))
        self.label_10.setText(_translate("gui_histo_main", "max epochs"))
        self.label_25.setText(_translate("gui_histo_main", "Cohort settings:"))
        self.label_2.setText(_translate("gui_histo_main", "tiles path"))
        self.label_15.setText(_translate("gui_histo_main", "Project name"))
        self.label_28.setText(_translate("gui_histo_main", "Cohort list:"))
        self.run_DL.setText(_translate("gui_histo_main", "run"))
        self.savingpath_DL.setText(_translate("gui_histo_main", "choose path"))
        self.label_20.setText(_translate("gui_histo_main", "max tile num"))
        self.clini_table_DL.setText(_translate("gui_histo_main", "choose file"))
        self.slide_masttab_DL.setToolTip(_translate("gui_histo_main", "choose a slide table"))
        self.slide_masttab_DL.setText(_translate("gui_histo_main", "choose file"))
        self.label_settings.setText(_translate("gui_histo_main", "Settings:"))
        self.choosemode_DL.setItemText(0, _translate("gui_histo_main", "test/train"))
        self.choosemode_DL.setItemText(1, _translate("gui_histo_main", "k-fold cross validation"))
        self.trainfull_DL.setText(_translate("gui_histo_main", "train full dataset"))
        self.cohort_list_DL.setSortingEnabled(True)
        __sortingEnabled = self.cohort_list_DL.isSortingEnabled()
        self.cohort_list_DL.setSortingEnabled(False)
        item = self.cohort_list_DL.item(0)
        item.setText(_translate("gui_histo_main", "Neues Element"))
        self.cohort_list_DL.setSortingEnabled(__sortingEnabled)
        self.addcohortlist_DL.setText(_translate("gui_histo_main", "add to list"))
        self.del_list_DL.setText(_translate("gui_histo_main", "delete list"))
        self.test_dl.setText(_translate("gui_histo_main", "Test"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Deeplearn), _translate("gui_histo_main", "Deep Learn"))
        self.choose_slidetable_Deploy.setText(_translate("gui_histo_main", "choose file"))
        self.label_26.setText(_translate("gui_histo_main", "batch size"))
        self.projectdir_Deploy.setText(_translate("gui_histo_main", "choose folder"))
        self.label_22.setText(_translate("gui_histo_main", "tile directory"))
        self.label_11.setText(_translate("gui_histo_main", "project directory"))
        self.run_Deploy.setText(_translate("gui_histo_main", "run"))
        self.label_29.setText(_translate("gui_histo_main", "Cohort settings:"))
        self.label_27.setText(_translate("gui_histo_main", "max tile num"))
        self.groups_Deploy.setText(_translate("gui_histo_main", "groups:"))
        self.clini_table_Deploy.setText(_translate("gui_histo_main", "choose file"))
        self.del_list_deploy.setText(_translate("gui_histo_main", "delete list"))
        self.label_23.setText(_translate("gui_histo_main", "cohort list:"))
        self.label.setText(_translate("gui_histo_main", "clini table"))
        self.label_30.setText(_translate("gui_histo_main", "Group Evaluation:"))
        self.label_7.setText(_translate("gui_histo_main", "Settings:"))
        self.choose_tiledir_Deploy.setText(_translate("gui_histo_main", "choose folder"))
        self.choose_model_Deploy.setText(_translate("gui_histo_main", "choose file"))
        self.addlist_Deploy.setText(_translate("gui_histo_main", "add to list"))
        self.reset_Deploy.setText(_translate("gui_histo_main", "reset"))
        self.subgroups_Deploy.setText(_translate("gui_histo_main", "subgroups:"))
        self.label_21.setText(_translate("gui_histo_main", "slide table"))
        self.advanced_Deploy.setText(_translate("gui_histo_main", "advanced settings"))
        self.label_24.setText(_translate("gui_histo_main", "model path"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Deploy), _translate("gui_histo_main", "Deploy"))
        self.label_16.setText(_translate("gui_histo_main", "                                           format:"))
        self.label_13.setText(_translate("gui_histo_main", "TextLabel"))
        self.listIm_Vis.setText(_translate("gui_histo_main", "List of Images"))
        self.openFolder_Vis.setText(_translate("gui_histo_main", "Open Folder"))
        self.nextIm_Vis.setText(_translate("gui_histo_main", "Next Image"))
        self.label_14.setText(_translate("gui_histo_main", "Current Image:"))
        self.prevIm_Vis.setText(_translate("gui_histo_main", "Previous Image"))
        self.label_17.setText(_translate("gui_histo_main", "Shortcuts:"))
        self.shortcutlabel.setText(_translate("gui_histo_main", "1-resection tumor; 2-biopsy tumor; 3-healthy tissues;4-fat;5-lymph-node;6-other;7-unsure;8-TMA;9-excluded"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vis_plots), _translate("gui_histo_main", "Images"))
        self.choosetable_Vis.setText(_translate("gui_histo_main", "choose table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.vis_tables), _translate("gui_histo_main", "Table"))
        self.fldrpth_Vis.setText(_translate("gui_histo_main", "choose folderpath"))
        self.format_Vis.setItemText(0, _translate("gui_histo_main", ".png"))
        self.format_Vis.setItemText(1, _translate("gui_histo_main", ".pdf"))
        self.format_Vis.setItemText(2, _translate("gui_histo_main", ".jpg"))
        self.save_all_Vis.setText(_translate("gui_histo_main", "save all"))
        self.save_Vis.setText(_translate("gui_histo_main", "save"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.Visualize), _translate("gui_histo_main", "Visualize"))
        self.menuhello.setTitle(_translate("gui_histo_main", "Deep Histology"))
        self.menuFile.setTitle(_translate("gui_histo_main", "File"))
        self.menuEdit.setTitle(_translate("gui_histo_main", "Edit"))
        self.menuView.setTitle(_translate("gui_histo_main", "View"))
        self.menuHelp.setTitle(_translate("gui_histo_main", "Help"))
        self.toolBar.setWindowTitle(_translate("gui_histo_main", "toolBar"))
        self.actionQuit_Deep_Histology.setText(_translate("gui_histo_main", "Quit Deep Histology"))
        self.actionPreferences.setText(_translate("gui_histo_main", "Preferences"))
        self.actionNew_Experiment.setText(_translate("gui_histo_main", "New Experiment"))
        self.actionOpen_Experiment.setText(_translate("gui_histo_main", "Open Experiment"))
        self.actionMenu.setText(_translate("gui_histo_main", "Menu"))
        self.actionGithub_Documentation.setText(_translate("gui_histo_main", "Github Documentation"))
        self.actionTutorial.setText(_translate("gui_histo_main", "Tutorial"))
        self.actionarr.setText(_translate("gui_histo_main", "arr"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui_histo_main = QtWidgets.QMainWindow()
    ui = Ui_gui_histo_main()
    ui.setupUi(gui_histo_main)
    gui_histo_main.show()
    sys.exit(app.exec_())

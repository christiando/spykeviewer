# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rob/Code/Spyke/viewer/spykeviewer/ui/main.ui'
#
# Created: Mon Sep 24 12:23:22 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(819, 867)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(790, 580))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("QGroupBox {\n"
"     border: 1px solid gray;\n"
"     border-radius: 5px;\n"
"     margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top left; /* position at the top center */\n"
"     padding: 0 2px;\n"
"     left: 10px;\n"
"}"))
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtGui.QMainWindow.AllowNestedDocks|QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setMargin(4)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainMenu = QtGui.QMenuBar(MainWindow)
        self.mainMenu.setGeometry(QtCore.QRect(0, 0, 819, 25))
        self.mainMenu.setObjectName(_fromUtf8("mainMenu"))
        self.menuFile = QtGui.QMenu(self.mainMenu)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.mainMenu)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuSelections = QtGui.QMenu(self.mainMenu)
        self.menuSelections.setObjectName(_fromUtf8("menuSelections"))
        self.menuPlugins = QtGui.QMenu(self.mainMenu)
        self.menuPlugins.setObjectName(_fromUtf8("menuPlugins"))
        self.menuFilter = QtGui.QMenu(self.mainMenu)
        self.menuFilter.setObjectName(_fromUtf8("menuFilter"))
        MainWindow.setMenuBar(self.mainMenu)
        self.consoleDock = QtGui.QDockWidget(MainWindow)
        self.consoleDock.setObjectName(_fromUtf8("consoleDock"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.verticalLayout_19 = QtGui.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_19.setObjectName(_fromUtf8("verticalLayout_19"))
        self.consoleDock.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.consoleDock)
        self.variableExplorerDock = QtGui.QDockWidget(MainWindow)
        self.variableExplorerDock.setObjectName(_fromUtf8("variableExplorerDock"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.variableExplorerDock.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.variableExplorerDock)
        self.historyDock = QtGui.QDockWidget(MainWindow)
        self.historyDock.setObjectName(_fromUtf8("historyDock"))
        self.dockWidgetContents_3 = QtGui.QWidget()
        self.dockWidgetContents_3.setObjectName(_fromUtf8("dockWidgetContents_3"))
        self.historyDock.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.historyDock)
        self.filterDock = QtGui.QDockWidget(MainWindow)
        self.filterDock.setObjectName(_fromUtf8("filterDock"))
        self.dockWidgetContents_5 = QtGui.QWidget()
        self.dockWidgetContents_5.setObjectName(_fromUtf8("dockWidgetContents_5"))
        self.gridLayout_5 = QtGui.QGridLayout(self.dockWidgetContents_5)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.filterTreeWidget = QtGui.QTreeWidget(self.dockWidgetContents_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.filterTreeWidget.sizePolicy().hasHeightForWidth())
        self.filterTreeWidget.setSizePolicy(sizePolicy)
        self.filterTreeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.filterTreeWidget.setDragEnabled(True)
        self.filterTreeWidget.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.filterTreeWidget.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.filterTreeWidget.setAlternatingRowColors(False)
        self.filterTreeWidget.setUniformRowHeights(False)
        self.filterTreeWidget.setObjectName(_fromUtf8("filterTreeWidget"))
        self.filterTreeWidget.header().setVisible(False)
        self.gridLayout_5.addWidget(self.filterTreeWidget, 0, 0, 1, 2)
        self.filterDock.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.filterDock)
        self.analysisDock = QtGui.QDockWidget(MainWindow)
        self.analysisDock.setObjectName(_fromUtf8("analysisDock"))
        self.dockWidgetContents_6 = QtGui.QWidget()
        self.dockWidgetContents_6.setObjectName(_fromUtf8("dockWidgetContents_6"))
        self.gridLayout_11 = QtGui.QGridLayout(self.dockWidgetContents_6)
        self.gridLayout_11.setObjectName(_fromUtf8("gridLayout_11"))
        self.neoAnalysesTreeView = QtGui.QTreeView(self.dockWidgetContents_6)
        self.neoAnalysesTreeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.neoAnalysesTreeView.setUniformRowHeights(True)
        self.neoAnalysesTreeView.setHeaderHidden(True)
        self.neoAnalysesTreeView.setObjectName(_fromUtf8("neoAnalysesTreeView"))
        self.neoAnalysesTreeView.header().setVisible(False)
        self.neoAnalysesTreeView.header().setDefaultSectionSize(0)
        self.gridLayout_11.addWidget(self.neoAnalysesTreeView, 0, 0, 1, 2)
        self.analysisDock.setWidget(self.dockWidgetContents_6)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.analysisDock)
        self.navigationNeoDock = QtGui.QDockWidget(MainWindow)
        self.navigationNeoDock.setObjectName(_fromUtf8("navigationNeoDock"))
        self.dockWidgetContents_12 = QtGui.QWidget()
        self.dockWidgetContents_12.setObjectName(_fromUtf8("dockWidgetContents_12"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents_12)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_31 = QtGui.QVBoxLayout()
        self.verticalLayout_31.setObjectName(_fromUtf8("verticalLayout_31"))
        self.label_34 = QtGui.QLabel(self.dockWidgetContents_12)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.verticalLayout_31.addWidget(self.label_34)
        self.neoBlockList = QtGui.QListWidget(self.dockWidgetContents_12)
        self.neoBlockList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.neoBlockList.setObjectName(_fromUtf8("neoBlockList"))
        self.verticalLayout_31.addWidget(self.neoBlockList)
        self.label_36 = QtGui.QLabel(self.dockWidgetContents_12)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.verticalLayout_31.addWidget(self.label_36)
        self.neoChannelGroupList = QtGui.QListWidget(self.dockWidgetContents_12)
        self.neoChannelGroupList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.neoChannelGroupList.setObjectName(_fromUtf8("neoChannelGroupList"))
        self.verticalLayout_31.addWidget(self.neoChannelGroupList)
        self.label_37 = QtGui.QLabel(self.dockWidgetContents_12)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.verticalLayout_31.addWidget(self.label_37)
        self.neoChannelList = QtGui.QListWidget(self.dockWidgetContents_12)
        self.neoChannelList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.neoChannelList.setObjectName(_fromUtf8("neoChannelList"))
        self.verticalLayout_31.addWidget(self.neoChannelList)
        self.horizontalLayout.addLayout(self.verticalLayout_31)
        self.verticalLayout_29 = QtGui.QVBoxLayout()
        self.verticalLayout_29.setObjectName(_fromUtf8("verticalLayout_29"))
        self.label_35 = QtGui.QLabel(self.dockWidgetContents_12)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.verticalLayout_29.addWidget(self.label_35)
        self.neoSegmentList = QtGui.QListWidget(self.dockWidgetContents_12)
        self.neoSegmentList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.neoSegmentList.setObjectName(_fromUtf8("neoSegmentList"))
        self.verticalLayout_29.addWidget(self.neoSegmentList)
        self.label_38 = QtGui.QLabel(self.dockWidgetContents_12)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.verticalLayout_29.addWidget(self.label_38)
        self.neoUnitList = QtGui.QListWidget(self.dockWidgetContents_12)
        self.neoUnitList.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.neoUnitList.setObjectName(_fromUtf8("neoUnitList"))
        self.verticalLayout_29.addWidget(self.neoUnitList)
        self.horizontalLayout.addLayout(self.verticalLayout_29)
        self.navigationNeoDock.setWidget(self.dockWidgetContents_12)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.navigationNeoDock)
        self.neoFilesDock = QtGui.QDockWidget(MainWindow)
        self.neoFilesDock.setObjectName(_fromUtf8("neoFilesDock"))
        self.dockWidgetContents_8 = QtGui.QWidget()
        self.dockWidgetContents_8.setObjectName(_fromUtf8("dockWidgetContents_8"))
        self.gridLayout_6 = QtGui.QGridLayout(self.dockWidgetContents_8)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.fileTreeView = QtGui.QTreeView(self.dockWidgetContents_8)
        self.fileTreeView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.fileTreeView.setUniformRowHeights(True)
        self.fileTreeView.setHeaderHidden(True)
        self.fileTreeView.setObjectName(_fromUtf8("fileTreeView"))
        self.fileTreeView.header().setVisible(False)
        self.fileTreeView.header().setCascadingSectionResizes(False)
        self.fileTreeView.header().setStretchLastSection(False)
        self.gridLayout_6.addWidget(self.fileTreeView, 0, 0, 1, 1)
        self.neoLoadFilesButton = QtGui.QPushButton(self.dockWidgetContents_8)
        self.neoLoadFilesButton.setObjectName(_fromUtf8("neoLoadFilesButton"))
        self.gridLayout_6.addWidget(self.neoLoadFilesButton, 1, 0, 1, 1)
        self.neoFilesDock.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.neoFilesDock)
        self.filterToolbar = QtGui.QToolBar(MainWindow)
        self.filterToolbar.setObjectName(_fromUtf8("filterToolbar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.filterToolbar)
        self.pluginToolBar = QtGui.QToolBar(MainWindow)
        self.pluginToolBar.setObjectName(_fromUtf8("pluginToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.pluginToolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setMenuRole(QtGui.QAction.QuitRole)
        self.actionExit.setIconVisibleInMenu(False)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSave_selection = QtGui.QAction(MainWindow)
        self.actionSave_selection.setObjectName(_fromUtf8("actionSave_selection"))
        self.actionLoad_selection = QtGui.QAction(MainWindow)
        self.actionLoad_selection.setObjectName(_fromUtf8("actionLoad_selection"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSwitch_Modes = QtGui.QAction(MainWindow)
        self.actionSwitch_Modes.setVisible(False)
        self.actionSwitch_Modes.setObjectName(_fromUtf8("actionSwitch_Modes"))
        self.actionNewSelection = QtGui.QAction(MainWindow)
        self.actionNewSelection.setObjectName(_fromUtf8("actionNewSelection"))
        self.actionClearCache = QtGui.QAction(MainWindow)
        self.actionClearCache.setVisible(True)
        self.actionClearCache.setObjectName(_fromUtf8("actionClearCache"))
        self.actionSave_data = QtGui.QAction(MainWindow)
        self.actionSave_data.setObjectName(_fromUtf8("actionSave_data"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionClearSelections = QtGui.QAction(MainWindow)
        self.actionClearSelections.setObjectName(_fromUtf8("actionClearSelections"))
        self.actionNewPlugin = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Analyses/New")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewPlugin.setIcon(icon)
        self.actionNewPlugin.setObjectName(_fromUtf8("actionNewPlugin"))
        self.actionEditPlugin = QtGui.QAction(MainWindow)
        self.actionEditPlugin.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Analyses/Edit")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditPlugin.setIcon(icon1)
        self.actionEditPlugin.setObjectName(_fromUtf8("actionEditPlugin"))
        self.actionRefreshPlugins = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Analyses/Reload")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefreshPlugins.setIcon(icon2)
        self.actionRefreshPlugins.setObjectName(_fromUtf8("actionRefreshPlugins"))
        self.actionSavePlugin = QtGui.QAction(MainWindow)
        self.actionSavePlugin.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/Analyses/Save")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSavePlugin.setIcon(icon3)
        self.actionSavePlugin.setObjectName(_fromUtf8("actionSavePlugin"))
        self.actionConfigurePlugin = QtGui.QAction(MainWindow)
        self.actionConfigurePlugin.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/Analyses/Config")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionConfigurePlugin.setIcon(icon4)
        self.actionConfigurePlugin.setObjectName(_fromUtf8("actionConfigurePlugin"))
        self.actionRunPlugin = QtGui.QAction(MainWindow)
        self.actionRunPlugin.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/Analyses/Run")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRunPlugin.setIcon(icon5)
        self.actionRunPlugin.setObjectName(_fromUtf8("actionRunPlugin"))
        self.actionRemotePlugin = QtGui.QAction(MainWindow)
        self.actionRemotePlugin.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/Analyses/Remote")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemotePlugin.setIcon(icon6)
        self.actionRemotePlugin.setObjectName(_fromUtf8("actionRemotePlugin"))
        self.actionNewFilter = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/Filter/New Filter")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFilter.setIcon(icon7)
        self.actionNewFilter.setObjectName(_fromUtf8("actionNewFilter"))
        self.actionCopyFilter = QtGui.QAction(MainWindow)
        self.actionCopyFilter.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/Filter/Copy Filter")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopyFilter.setIcon(icon8)
        self.actionCopyFilter.setObjectName(_fromUtf8("actionCopyFilter"))
        self.actionEditFilter = QtGui.QAction(MainWindow)
        self.actionEditFilter.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/Filter/Edit Filter")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditFilter.setIcon(icon9)
        self.actionEditFilter.setObjectName(_fromUtf8("actionEditFilter"))
        self.actionDeleteFilter = QtGui.QAction(MainWindow)
        self.actionDeleteFilter.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/Filter/Remove Filter")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteFilter.setIcon(icon10)
        self.actionDeleteFilter.setObjectName(_fromUtf8("actionDeleteFilter"))
        self.actionNewFilterGroup = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/Filter/New Filter Group")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFilterGroup.setIcon(icon11)
        self.actionNewFilterGroup.setObjectName(_fromUtf8("actionNewFilterGroup"))
        self.menuFile.addAction(self.actionSave_selection)
        self.menuFile.addAction(self.actionLoad_selection)
        self.menuFile.addAction(self.actionSwitch_Modes)
        self.menuFile.addAction(self.actionClearCache)
        self.menuFile.addAction(self.actionSave_data)
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSelections.addAction(self.actionNewSelection)
        self.menuSelections.addAction(self.actionClearSelections)
        self.menuSelections.addSeparator()
        self.menuPlugins.addAction(self.actionRunPlugin)
        self.menuPlugins.addAction(self.actionConfigurePlugin)
        self.menuPlugins.addAction(self.actionNewPlugin)
        self.menuPlugins.addAction(self.actionEditPlugin)
        self.menuPlugins.addAction(self.actionSavePlugin)
        self.menuPlugins.addAction(self.actionRefreshPlugins)
        self.menuPlugins.addAction(self.actionRemotePlugin)
        self.menuFilter.addAction(self.actionNewFilter)
        self.menuFilter.addAction(self.actionNewFilterGroup)
        self.menuFilter.addAction(self.actionCopyFilter)
        self.menuFilter.addAction(self.actionEditFilter)
        self.menuFilter.addAction(self.actionDeleteFilter)
        self.mainMenu.addAction(self.menuFile.menuAction())
        self.mainMenu.addAction(self.menuSelections.menuAction())
        self.mainMenu.addAction(self.menuFilter.menuAction())
        self.mainMenu.addAction(self.menuPlugins.menuAction())
        self.mainMenu.addAction(self.menuHelp.menuAction())
        self.filterToolbar.addAction(self.actionNewFilter)
        self.filterToolbar.addAction(self.actionNewFilterGroup)
        self.filterToolbar.addAction(self.actionCopyFilter)
        self.filterToolbar.addAction(self.actionEditFilter)
        self.filterToolbar.addAction(self.actionDeleteFilter)
        self.pluginToolBar.addAction(self.actionNewPlugin)
        self.pluginToolBar.addAction(self.actionEditPlugin)
        self.pluginToolBar.addAction(self.actionSavePlugin)
        self.pluginToolBar.addAction(self.actionRefreshPlugins)
        self.pluginToolBar.addAction(self.actionConfigurePlugin)
        self.pluginToolBar.addAction(self.actionRunPlugin)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Spyke Viewer", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuSelections.setTitle(QtGui.QApplication.translate("MainWindow", "Selections", None, QtGui.QApplication.UnicodeUTF8))
        self.menuPlugins.setTitle(QtGui.QApplication.translate("MainWindow", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFilter.setTitle(QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.consoleDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Console", None, QtGui.QApplication.UnicodeUTF8))
        self.variableExplorerDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Variable Explorer", None, QtGui.QApplication.UnicodeUTF8))
        self.historyDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Command History", None, QtGui.QApplication.UnicodeUTF8))
        self.filterDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.filterTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.analysisDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.navigationNeoDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Navigation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(QtGui.QApplication.translate("MainWindow", "Block:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("MainWindow", "Channel Groups:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(QtGui.QApplication.translate("MainWindow", "Channels:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_35.setText(QtGui.QApplication.translate("MainWindow", "Segment:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(QtGui.QApplication.translate("MainWindow", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.neoFilesDock.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Files", None, QtGui.QApplication.UnicodeUTF8))
        self.neoLoadFilesButton.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.filterToolbar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Filter Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pluginToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Analysis Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_selection.setText(QtGui.QApplication.translate("MainWindow", "Save Selection Set...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLoad_selection.setText(QtGui.QApplication.translate("MainWindow", "Load Selection Set...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSwitch_Modes.setText(QtGui.QApplication.translate("MainWindow", "Switch Modes", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewSelection.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearCache.setText(QtGui.QApplication.translate("MainWindow", "Clear NEO object cache", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave_data.setText(QtGui.QApplication.translate("MainWindow", "Save Selected Data as...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClearSelections.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewPlugin.setText(QtGui.QApplication.translate("MainWindow", "New Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewPlugin.setToolTip(QtGui.QApplication.translate("MainWindow", "Create a new plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewPlugin.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+N", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditPlugin.setText(QtGui.QApplication.translate("MainWindow", "Edit Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditPlugin.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefreshPlugins.setText(QtGui.QApplication.translate("MainWindow", "Refresh Plugins", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefreshPlugins.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+R", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavePlugin.setText(QtGui.QApplication.translate("MainWindow", "Save Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSavePlugin.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurePlugin.setText(QtGui.QApplication.translate("MainWindow", "Configure Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConfigurePlugin.setShortcut(QtGui.QApplication.translate("MainWindow", "F6", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunPlugin.setText(QtGui.QApplication.translate("MainWindow", "Run Plugin", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRunPlugin.setShortcut(QtGui.QApplication.translate("MainWindow", "F5", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemotePlugin.setText(QtGui.QApplication.translate("MainWindow", "Start with Remote Script", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemotePlugin.setShortcut(QtGui.QApplication.translate("MainWindow", "F9", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFilter.setText(QtGui.QApplication.translate("MainWindow", "New Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCopyFilter.setText(QtGui.QApplication.translate("MainWindow", "Copy Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditFilter.setText(QtGui.QApplication.translate("MainWindow", "Edit Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteFilter.setText(QtGui.QApplication.translate("MainWindow", "Delete Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNewFilterGroup.setText(QtGui.QApplication.translate("MainWindow", "New Filter Group", None, QtGui.QApplication.UnicodeUTF8))

import icons_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/DMT-git/src/ui/ui_main_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(869, 502)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layMessage = QtWidgets.QHBoxLayout()
        self.layMessage.setContentsMargins(0, -1, -1, 0)
        self.layMessage.setSpacing(0)
        self.layMessage.setObjectName("layMessage")
        self.lblMessage = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMessage.sizePolicy().hasHeightForWidth())
        self.lblMessage.setSizePolicy(sizePolicy)
        self.lblMessage.setText("")
        self.lblMessage.setWordWrap(True)
        self.lblMessage.setOpenExternalLinks(True)
        self.lblMessage.setObjectName("lblMessage")
        self.layMessage.addWidget(self.lblMessage)
        self.verticalLayout.addLayout(self.layMessage)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(3)
        self.gridLayout_2.setVerticalSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cboMasternodes = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboMasternodes.sizePolicy().hasHeightForWidth())
        self.cboMasternodes.setSizePolicy(sizePolicy)
        self.cboMasternodes.setMinimumSize(QtCore.QSize(140, 0))
        self.cboMasternodes.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboMasternodes.setEditable(False)
        self.cboMasternodes.setObjectName("cboMasternodes")
        self.horizontalLayout_4.addWidget(self.cboMasternodes)
        self.btnNewMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewMn.sizePolicy().hasHeightForWidth())
        self.btnNewMn.setSizePolicy(sizePolicy)
        self.btnNewMn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnNewMn.setObjectName("btnNewMn")
        self.horizontalLayout_4.addWidget(self.btnNewMn)
        self.btnDuplicateMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDuplicateMn.sizePolicy().hasHeightForWidth())
        self.btnDuplicateMn.setSizePolicy(sizePolicy)
        self.btnDuplicateMn.setObjectName("btnDuplicateMn")
        self.horizontalLayout_4.addWidget(self.btnDuplicateMn)
        self.btnDeleteMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDeleteMn.sizePolicy().hasHeightForWidth())
        self.btnDeleteMn.setSizePolicy(sizePolicy)
        self.btnDeleteMn.setObjectName("btnDeleteMn")
        self.horizontalLayout_4.addWidget(self.btnDeleteMn)
        self.btnEditMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEditMn.sizePolicy().hasHeightForWidth())
        self.btnEditMn.setSizePolicy(sizePolicy)
        self.btnEditMn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btnEditMn.setObjectName("btnEditMn")
        self.horizontalLayout_4.addWidget(self.btnEditMn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.setStretch(0, 3)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.edtMnIp = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnIp.sizePolicy().hasHeightForWidth())
        self.edtMnIp.setSizePolicy(sizePolicy)
        self.edtMnIp.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnIp.setMaximumSize(QtCore.QSize(150, 16777215))
        self.edtMnIp.setObjectName("edtMnIp")
        self.horizontalLayout_3.addWidget(self.edtMnIp)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.edtMnPort = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnPort.sizePolicy().hasHeightForWidth())
        self.edtMnPort.setSizePolicy(sizePolicy)
        self.edtMnPort.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnPort.setMaximumSize(QtCore.QSize(70, 16777215))
        self.edtMnPort.setObjectName("edtMnPort")
        self.horizontalLayout_3.addWidget(self.edtMnPort)
        self.chbUseDefaultProtocolVersion = QtWidgets.QCheckBox(self.groupBox_3)
        self.chbUseDefaultProtocolVersion.setObjectName("chbUseDefaultProtocolVersion")
        self.horizontalLayout_3.addWidget(self.chbUseDefaultProtocolVersion)
        self.edtMnProtocolVersion = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtMnProtocolVersion.setMaximumSize(QtCore.QSize(80, 16777215))
        self.edtMnProtocolVersion.setStatusTip("")
        self.edtMnProtocolVersion.setInputMask("")
        self.edtMnProtocolVersion.setObjectName("edtMnProtocolVersion")
        self.horizontalLayout_3.addWidget(self.edtMnProtocolVersion)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(8)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.edtMnCollateralTx = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralTx.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralTx.setSizePolicy(sizePolicy)
        self.edtMnCollateralTx.setMinimumSize(QtCore.QSize(300, 0))
        self.edtMnCollateralTx.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralTx.setText("")
        self.edtMnCollateralTx.setObjectName("edtMnCollateralTx")
        self.horizontalLayout_7.addWidget(self.edtMnCollateralTx)
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.edtMnCollateralTxIndex = QtWidgets.QLineEdit(self.groupBox_3)
        self.edtMnCollateralTxIndex.setMaximumSize(QtCore.QSize(25, 16777215))
        self.edtMnCollateralTxIndex.setObjectName("edtMnCollateralTxIndex")
        self.horizontalLayout_7.addWidget(self.edtMnCollateralTxIndex)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)
        self.layCollateral = QtWidgets.QHBoxLayout()
        self.layCollateral.setContentsMargins(-1, 0, -1, 0)
        self.layCollateral.setSpacing(0)
        self.layCollateral.setObjectName("layCollateral")
        self.edtMnCollateralAddress = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralAddress.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralAddress.setSizePolicy(sizePolicy)
        self.edtMnCollateralAddress.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnCollateralAddress.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralAddress.setReadOnly(False)
        self.edtMnCollateralAddress.setObjectName("edtMnCollateralAddress")
        self.layCollateral.addWidget(self.edtMnCollateralAddress)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(3, -1, 3, -1)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnHwAddressToBip32 = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHwAddressToBip32.sizePolicy().hasHeightForWidth())
        self.btnHwAddressToBip32.setSizePolicy(sizePolicy)
        self.btnHwAddressToBip32.setMinimumSize(QtCore.QSize(30, 0))
        self.btnHwAddressToBip32.setMaximumSize(QtCore.QSize(10000, 1000000))
        self.btnHwAddressToBip32.setText("")
        self.btnHwAddressToBip32.setIconSize(QtCore.QSize(16, 16))
        self.btnHwAddressToBip32.setObjectName("btnHwAddressToBip32")
        self.horizontalLayout_2.addWidget(self.btnHwAddressToBip32)
        self.btnHwBip32ToAddress = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnHwBip32ToAddress.sizePolicy().hasHeightForWidth())
        self.btnHwBip32ToAddress.setSizePolicy(sizePolicy)
        self.btnHwBip32ToAddress.setMinimumSize(QtCore.QSize(30, 0))
        self.btnHwBip32ToAddress.setMaximumSize(QtCore.QSize(10000000, 10000000))
        self.btnHwBip32ToAddress.setText("")
        self.btnHwBip32ToAddress.setIconSize(QtCore.QSize(16, 16))
        self.btnHwBip32ToAddress.setObjectName("btnHwBip32ToAddress")
        self.horizontalLayout_2.addWidget(self.btnHwBip32ToAddress)
        self.layCollateral.addLayout(self.horizontalLayout_2)
        self.edtMnCollateralBip32Path = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnCollateralBip32Path.sizePolicy().hasHeightForWidth())
        self.edtMnCollateralBip32Path.setSizePolicy(sizePolicy)
        self.edtMnCollateralBip32Path.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnCollateralBip32Path.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnCollateralBip32Path.setObjectName("edtMnCollateralBip32Path")
        self.layCollateral.addWidget(self.edtMnCollateralBip32Path, 0, QtCore.Qt.AlignVCenter)
        self.layCollateral.setStretch(0, 1)
        self.gridLayout_2.addLayout(self.layCollateral, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_2.addWidget(self.label_12, 1, 0, 1, 1)
        self.edtMnName = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnName.sizePolicy().hasHeightForWidth())
        self.edtMnName.setSizePolicy(sizePolicy)
        self.edtMnName.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnName.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnName.setObjectName("edtMnName")
        self.gridLayout_2.addWidget(self.edtMnName, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 5, 0, 1, 1)
        self.btnGenerateMNPrivateKey = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnGenerateMNPrivateKey.sizePolicy().hasHeightForWidth())
        self.btnGenerateMNPrivateKey.setSizePolicy(sizePolicy)
        self.btnGenerateMNPrivateKey.setMinimumSize(QtCore.QSize(110, 0))
        self.btnGenerateMNPrivateKey.setMaximumSize(QtCore.QSize(400, 16777215))
        self.btnGenerateMNPrivateKey.setObjectName("btnGenerateMNPrivateKey")
        self.gridLayout_2.addWidget(self.btnGenerateMNPrivateKey, 3, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 2, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 7, 0, 1, 1)
        self.edtMnPrivateKey = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtMnPrivateKey.sizePolicy().hasHeightForWidth())
        self.edtMnPrivateKey.setSizePolicy(sizePolicy)
        self.edtMnPrivateKey.setMinimumSize(QtCore.QSize(0, 0))
        self.edtMnPrivateKey.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edtMnPrivateKey.setObjectName("edtMnPrivateKey")
        self.gridLayout_2.addWidget(self.edtMnPrivateKey, 3, 1, 1, 1)
        self.btnRefreshMnStatus = QtWidgets.QPushButton(self.groupBox_3)
        self.btnRefreshMnStatus.setObjectName("btnRefreshMnStatus")
        self.gridLayout_2.addWidget(self.btnRefreshMnStatus, 6, 3, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSpacing(2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.btnBroadcastMn = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBroadcastMn.sizePolicy().hasHeightForWidth())
        self.btnBroadcastMn.setSizePolicy(sizePolicy)
        self.btnBroadcastMn.setMinimumSize(QtCore.QSize(0, 0))
        self.btnBroadcastMn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.btnBroadcastMn.setStyleSheet("")
        self.btnBroadcastMn.setObjectName("btnBroadcastMn")
        self.horizontalLayout_12.addWidget(self.btnBroadcastMn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.horizontalLayout_12.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_12)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 7, 1, 1, 1)
        self.btnFindCollateral = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnFindCollateral.sizePolicy().hasHeightForWidth())
        self.btnFindCollateral.setSizePolicy(sizePolicy)
        self.btnFindCollateral.setMinimumSize(QtCore.QSize(0, 0))
        self.btnFindCollateral.setObjectName("btnFindCollateral")
        self.gridLayout_2.addWidget(self.btnFindCollateral, 5, 3, 1, 1)
        self.lblMnStatus = QtWidgets.QLabel(self.groupBox_3)
        self.lblMnStatus.setFrameShape(QtWidgets.QFrame.Panel)
        self.lblMnStatus.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lblMnStatus.setLineWidth(1)
        self.lblMnStatus.setText("")
        self.lblMnStatus.setWordWrap(True)
        self.lblMnStatus.setObjectName("lblMnStatus")
        self.gridLayout_2.addWidget(self.lblMnStatus, 6, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 869, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuTools = QtWidgets.QMenu(self.menuBar)
        self.menuTools.setObjectName("menuTools")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.action_open_recent_files = QtWidgets.QMenu(self.menuFile)
        self.action_open_recent_files.setObjectName("action_open_recent_files")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_transfer_funds_for_cur_mn = QtWidgets.QAction(MainWindow)
        self.action_transfer_funds_for_cur_mn.setObjectName("action_transfer_funds_for_cur_mn")
        self.action_transfer_funds_for_all_mns = QtWidgets.QAction(MainWindow)
        self.action_transfer_funds_for_all_mns.setObjectName("action_transfer_funds_for_all_mns")
        self.action_transfer_funds_for_any_address = QtWidgets.QAction(MainWindow)
        self.action_transfer_funds_for_any_address.setObjectName("action_transfer_funds_for_any_address")
        self.action_sign_message_for_cur_mn = QtWidgets.QAction(MainWindow)
        self.action_sign_message_for_cur_mn.setObjectName("action_sign_message_for_cur_mn")
        self.action_hw_configuration = QtWidgets.QAction(MainWindow)
        self.action_hw_configuration.setObjectName("action_hw_configuration")
        self.action_load_config_file = QtWidgets.QAction(MainWindow)
        self.action_load_config_file.setObjectName("action_load_config_file")
        self.action_save_config_file_as = QtWidgets.QAction(MainWindow)
        self.action_save_config_file_as.setObjectName("action_save_config_file_as")
        self.action_save_config_file = QtWidgets.QAction(MainWindow)
        self.action_save_config_file.setObjectName("action_save_config_file")
        self.action_check_network_connection = QtWidgets.QAction(MainWindow)
        self.action_check_network_connection.setObjectName("action_check_network_connection")
        self.action_open_settings_window = QtWidgets.QAction(MainWindow)
        self.action_open_settings_window.setMenuRole(QtWidgets.QAction.PreferencesRole)
        self.action_open_settings_window.setObjectName("action_open_settings_window")
        self.action_open_proposals_window = QtWidgets.QAction(MainWindow)
        self.action_open_proposals_window.setObjectName("action_open_proposals_window")
        self.action_test_hw_connection = QtWidgets.QAction(MainWindow)
        self.action_test_hw_connection.setObjectName("action_test_hw_connection")
        self.action_disconnect_hw = QtWidgets.QAction(MainWindow)
        self.action_disconnect_hw.setObjectName("action_disconnect_hw")
        self.action_hw_initialization_recovery = QtWidgets.QAction(MainWindow)
        self.action_hw_initialization_recovery.setObjectName("action_hw_initialization_recovery")
        self.action_check_for_updates = QtWidgets.QAction(MainWindow)
        self.action_check_for_updates.setObjectName("action_check_for_updates")
        self.action_open_log_file = QtWidgets.QAction(MainWindow)
        self.action_open_log_file.setObjectName("action_open_log_file")
        self.action_about_app = QtWidgets.QAction(MainWindow)
        self.action_about_app.setMenuRole(QtWidgets.QAction.AboutRole)
        self.action_about_app.setObjectName("action_about_app")
        self.action_import_masternode_conf = QtWidgets.QAction(MainWindow)
        self.action_import_masternode_conf.setObjectName("action_import_masternode_conf")
        self.action_about_qt = QtWidgets.QAction(MainWindow)
        self.action_about_qt.setMenuRole(QtWidgets.QAction.AboutQtRole)
        self.action_about_qt.setObjectName("action_about_qt")
        self.action_gen_mn_priv_key_compressed = QtWidgets.QAction(MainWindow)
        self.action_gen_mn_priv_key_compressed.setObjectName("action_gen_mn_priv_key_compressed")
        self.action_gen_mn_priv_key_uncompressed = QtWidgets.QAction(MainWindow)
        self.action_gen_mn_priv_key_uncompressed.setObjectName("action_gen_mn_priv_key_uncompressed")
        self.action_command_console = QtWidgets.QAction(MainWindow)
        self.action_command_console.setObjectName("action_command_console")
        self.menuTools.addAction(self.action_transfer_funds_for_cur_mn)
        self.menuTools.addAction(self.action_transfer_funds_for_all_mns)
        self.menuTools.addAction(self.action_transfer_funds_for_any_address)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_sign_message_for_cur_mn)
        self.menuTools.addAction(self.action_hw_configuration)
        self.menuTools.addAction(self.action_hw_initialization_recovery)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_import_masternode_conf)
        self.menuTools.addSeparator()
        self.menuTools.addAction(self.action_check_for_updates)
        self.menuTools.addAction(self.action_command_console)
        self.menuTools.addAction(self.action_open_log_file)
        self.menuFile.addAction(self.action_load_config_file)
        self.menuFile.addAction(self.action_open_recent_files.menuAction())
        self.menuFile.addAction(self.action_save_config_file)
        self.menuFile.addAction(self.action_save_config_file_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_open_settings_window)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_about_app)
        self.menuFile.addAction(self.action_about_qt)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuTools.menuAction())
        self.toolBar.addAction(self.action_open_settings_window)
        self.toolBar.addAction(self.action_save_config_file)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_check_network_connection)
        self.toolBar.addAction(self.action_test_hw_connection)
        self.toolBar.addAction(self.action_disconnect_hw)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_open_proposals_window)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_transfer_funds_for_any_address)
        self.toolBar.addAction(self.action_transfer_funds_for_cur_mn)
        self.toolBar.addAction(self.action_transfer_funds_for_all_mns)
        self.toolBar.addAction(self.action_sign_message_for_cur_mn)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cboMasternodes, self.edtMnName)
        MainWindow.setTabOrder(self.edtMnName, self.edtMnIp)
        MainWindow.setTabOrder(self.edtMnIp, self.edtMnPort)
        MainWindow.setTabOrder(self.edtMnPort, self.edtMnPrivateKey)
        MainWindow.setTabOrder(self.edtMnPrivateKey, self.edtMnCollateralAddress)
        MainWindow.setTabOrder(self.edtMnCollateralAddress, self.edtMnCollateralBip32Path)
        MainWindow.setTabOrder(self.edtMnCollateralBip32Path, self.edtMnCollateralTx)
        MainWindow.setTabOrder(self.edtMnCollateralTx, self.edtMnCollateralTxIndex)
        MainWindow.setTabOrder(self.edtMnCollateralTxIndex, self.btnNewMn)
        MainWindow.setTabOrder(self.btnNewMn, self.btnEditMn)
        MainWindow.setTabOrder(self.btnEditMn, self.btnHwAddressToBip32)
        MainWindow.setTabOrder(self.btnHwAddressToBip32, self.btnHwBip32ToAddress)
        MainWindow.setTabOrder(self.btnHwBip32ToAddress, self.btnDeleteMn)
        MainWindow.setTabOrder(self.btnDeleteMn, self.btnGenerateMNPrivateKey)
        MainWindow.setTabOrder(self.btnGenerateMNPrivateKey, self.btnRefreshMnStatus)
        MainWindow.setTabOrder(self.btnRefreshMnStatus, self.btnBroadcastMn)
        MainWindow.setTabOrder(self.btnBroadcastMn, self.btnFindCollateral)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Masternode"))
        self.cboMasternodes.setToolTip(_translate("MainWindow", "List of configured masternodes"))
        self.btnNewMn.setToolTip(_translate("MainWindow", "Create a new Masternode configuration"))
        self.btnNewMn.setText(_translate("MainWindow", "New"))
        self.btnDuplicateMn.setToolTip(_translate("MainWindow", "Duplicate masternode entry"))
        self.btnDuplicateMn.setText(_translate("MainWindow", "Duplicate"))
        self.btnDeleteMn.setToolTip(_translate("MainWindow", "Delete current Masternode configuration"))
        self.btnDeleteMn.setText(_translate("MainWindow", "Delete"))
        self.btnEditMn.setToolTip(_translate("MainWindow", "Enable editing"))
        self.btnEditMn.setText(_translate("MainWindow", "Edit"))
        self.edtMnIp.setToolTip(_translate("MainWindow", "The Masternode\'s IP address for incoming communication with other nodes"))
        self.label_11.setText(_translate("MainWindow", "port:"))
        self.edtMnPort.setToolTip(_translate("MainWindow", "The Masternode\'s TCP port number for incoming communication with other nodes"))
        self.chbUseDefaultProtocolVersion.setToolTip(_translate("MainWindow", "Use the default protocol version when starting masternode"))
        self.chbUseDefaultProtocolVersion.setText(_translate("MainWindow", "Use default protocol version"))
        self.edtMnProtocolVersion.setToolTip(_translate("MainWindow", "The protocol version number to be sent at masternode start time"))
        self.edtMnProtocolVersion.setPlaceholderText(_translate("MainWindow", "default"))
        self.edtMnCollateralTx.setToolTip(_translate("MainWindow", "The collateral transaction hash from the 1000 Dash deposit"))
        self.label_7.setText(_translate("MainWindow", "TX index:"))
        self.edtMnCollateralTxIndex.setToolTip(_translate("MainWindow", "The collateral transaction\'s (unspent) output index with the 1000 Dash deposit (usally 0)"))
        self.edtMnCollateralAddress.setToolTip(_translate("MainWindow", "Dash address of the masternode 1000 Dash collateral"))
        self.edtMnCollateralAddress.setPlaceholderText(_translate("MainWindow", "Dash address"))
        self.btnHwAddressToBip32.setToolTip(_translate("MainWindow", "Convert Dash address to BIP32 path using hardware wallet"))
        self.btnHwBip32ToAddress.setToolTip(_translate("MainWindow", "Convert BIP32 path to Dash address using hardware wallet"))
        self.edtMnCollateralBip32Path.setToolTip(_translate("MainWindow", "BIP32 path of the 1000 Dash collateral (e.g. 44\'/5\'/0\'/0/0)"))
        self.edtMnCollateralBip32Path.setPlaceholderText(_translate("MainWindow", "BIP32 path"))
        self.label_4.setText(_translate("MainWindow", "Collateral:"))
        self.label_9.setText(_translate("MainWindow", "MN private key:"))
        self.label_8.setText(_translate("MainWindow", "Masternode status:"))
        self.label_12.setText(_translate("MainWindow", "Name:"))
        self.edtMnName.setToolTip(_translate("MainWindow", "The Masternode\'s configuration name"))
        self.label_6.setText(_translate("MainWindow", "Collateral TX ID:"))
        self.btnGenerateMNPrivateKey.setToolTip(_translate("MainWindow", "Generate a new private key"))
        self.btnGenerateMNPrivateKey.setText(_translate("MainWindow", "Generate new"))
        self.label_5.setText(_translate("MainWindow", "Masternodes:"))
        self.label_10.setText(_translate("MainWindow", "IP:"))
        self.edtMnPrivateKey.setToolTip(_translate("MainWindow", "Masternode\'s private key. Use your own or click the button <Generate new> to create a new and random private key with the use of \'bitcoin\' library"))
        self.btnRefreshMnStatus.setToolTip(_translate("MainWindow", "Get Masternode\'s status"))
        self.btnRefreshMnStatus.setText(_translate("MainWindow", "Get status"))
        self.btnBroadcastMn.setToolTip(_translate("MainWindow", "Broadcast information about the Masternode"))
        self.btnBroadcastMn.setText(_translate("MainWindow", "Start Masternode using hardware wallet"))
        self.btnFindCollateral.setToolTip(_translate("MainWindow", "Find collateral transaction"))
        self.btnFindCollateral.setText(_translate("MainWindow", "Lookup"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.action_open_recent_files.setTitle(_translate("MainWindow", "Recent Configuration Files"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.action_transfer_funds_for_cur_mn.setText(_translate("MainWindow", "Transfer Funds for Current Masternode..."))
        self.action_transfer_funds_for_all_mns.setText(_translate("MainWindow", "Transfer Funds for All Masternodes"))
        self.action_transfer_funds_for_any_address.setText(_translate("MainWindow", "Transfer Funds for Any Address"))
        self.action_sign_message_for_cur_mn.setText(_translate("MainWindow", "Sign Message for Current Masternode..."))
        self.action_hw_configuration.setText(_translate("MainWindow", "Hardware Wallet PIN/passphrase Configuration..."))
        self.action_load_config_file.setText(_translate("MainWindow", "Open Configuration File..."))
        self.action_load_config_file.setToolTip(_translate("MainWindow", "Open configuration file"))
        self.action_save_config_file_as.setText(_translate("MainWindow", "Save Configuration As..."))
        self.action_save_config_file.setText(_translate("MainWindow", "Save Configuration"))
        self.action_check_network_connection.setText(_translate("MainWindow", "Check Network Connection"))
        self.action_check_network_connection.setToolTip(_translate("MainWindow", "Check Dash Network Connection"))
        self.action_open_settings_window.setText(_translate("MainWindow", "Settings"))
        self.action_open_settings_window.setToolTip(_translate("MainWindow", "Settings"))
        self.action_open_proposals_window.setText(_translate("MainWindow", "Proposals"))
        self.action_open_proposals_window.setToolTip(_translate("MainWindow", "Proposals"))
        self.action_test_hw_connection.setText(_translate("MainWindow", "Test Hardware Wallet Connection"))
        self.action_disconnect_hw.setText(_translate("MainWindow", "Disconnect Hardware Wallet"))
        self.action_hw_initialization_recovery.setText(_translate("MainWindow", "Hardware Wallet Initialization/Recovery..."))
        self.action_check_for_updates.setText(_translate("MainWindow", "Check For Updates"))
        self.action_open_log_file.setText(_translate("MainWindow", "Open Log File"))
        self.action_open_log_file.setShortcut(_translate("MainWindow", "Meta+Alt+L"))
        self.action_about_app.setText(_translate("MainWindow", "About DashMasternodeTool..."))
        self.action_import_masternode_conf.setText(_translate("MainWindow", "Import masternodes from the masternode.conf file..."))
        self.action_about_qt.setText(_translate("MainWindow", "About Qt..."))
        self.action_about_qt.setToolTip(_translate("MainWindow", "About Qt"))
        self.action_gen_mn_priv_key_compressed.setText(_translate("MainWindow", "Generate masternode private key (compressed)"))
        self.action_gen_mn_priv_key_compressed.setShortcut(_translate("MainWindow", "Ctrl+Alt+C"))
        self.action_gen_mn_priv_key_uncompressed.setText(_translate("MainWindow", "Generate masternode private key (uncompressed)"))
        self.action_gen_mn_priv_key_uncompressed.setToolTip(_translate("MainWindow", "Generate masternode private key (uncompressed)"))
        self.action_gen_mn_priv_key_uncompressed.setShortcut(_translate("MainWindow", "Ctrl+Alt+U"))
        self.action_command_console.setText(_translate("MainWindow", "Command Console"))
        self.action_command_console.setShortcut(_translate("MainWindow", "Meta+Alt+C"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/HMT-git/src/ui/ui_wallet_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WalletDlg(object):
    def setupUi(self, WalletDlg):
        WalletDlg.setObjectName("WalletDlg")
        WalletDlg.resize(862, 625)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WalletDlg.sizePolicy().hasHeightForWidth())
        WalletDlg.setSizePolicy(sizePolicy)
        WalletDlg.setSizeGripEnabled(True)
        WalletDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(WalletDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pnl_input = QtWidgets.QWidget(WalletDlg)
        self.pnl_input.setObjectName("pnl_input")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pnl_input)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lay_input = QtWidgets.QHBoxLayout()
        self.lay_input.setSpacing(8)
        self.lay_input.setObjectName("lay_input")
        self.lblHW = QtWidgets.QLabel(self.pnl_input)
        self.lblHW.setText("")
        self.lblHW.setObjectName("lblHW")
        self.lay_input.addWidget(self.lblHW)
        self.btnSetHwIdentityLabel = QtWidgets.QToolButton(self.pnl_input)
        self.btnSetHwIdentityLabel.setObjectName("btnSetHwIdentityLabel")
        self.lay_input.addWidget(self.btnSetHwIdentityLabel)
        self.btnPurgeHwIdentity = QtWidgets.QToolButton(self.pnl_input)
        self.btnPurgeHwIdentity.setObjectName("btnPurgeHwIdentity")
        self.lay_input.addWidget(self.btnPurgeHwIdentity)
        self.btnFetchTransactions = QtWidgets.QToolButton(self.pnl_input)
        self.btnFetchTransactions.setObjectName("btnFetchTransactions")
        self.lay_input.addWidget(self.btnFetchTransactions)
        self.wdgSpinner = QtWidgets.QWidget(self.pnl_input)
        self.wdgSpinner.setMinimumSize(QtCore.QSize(32, 0))
        self.wdgSpinner.setObjectName("wdgSpinner")
        self.lay_input.addWidget(self.wdgSpinner)
        self.lbl_message = QtWidgets.QLabel(self.pnl_input)
        self.lbl_message.setStyleSheet("")
        self.lbl_message.setText("")
        self.lbl_message.setWordWrap(False)
        self.lbl_message.setOpenExternalLinks(True)
        self.lbl_message.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.lbl_message.setObjectName("lbl_message")
        self.lay_input.addWidget(self.lbl_message)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lay_input.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.lay_input)
        self.verticalLayout.addWidget(self.pnl_input)
        self.widget = QtWidgets.QWidget(WalletDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.splitterMain = QtWidgets.QSplitter(self.widget)
        self.splitterMain.setOrientation(QtCore.Qt.Horizontal)
        self.splitterMain.setOpaqueResize(True)
        self.splitterMain.setChildrenCollapsible(True)
        self.splitterMain.setObjectName("splitterMain")
        self.wdgLeftPanel = QtWidgets.QWidget(self.splitterMain)
        self.wdgLeftPanel.setObjectName("wdgLeftPanel")
        self.vlayoutViewMode = QtWidgets.QVBoxLayout(self.wdgLeftPanel)
        self.vlayoutViewMode.setContentsMargins(0, 0, 0, 0)
        self.vlayoutViewMode.setObjectName("vlayoutViewMode")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cboAddressSourceMode = QtWidgets.QComboBox(self.wdgLeftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cboAddressSourceMode.sizePolicy().hasHeightForWidth())
        self.cboAddressSourceMode.setSizePolicy(sizePolicy)
        self.cboAddressSourceMode.setMinimumSize(QtCore.QSize(0, 0))
        self.cboAddressSourceMode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cboAddressSourceMode.setObjectName("cboAddressSourceMode")
        self.cboAddressSourceMode.addItem("")
        self.cboAddressSourceMode.addItem("")
        self.horizontalLayout.addWidget(self.cboAddressSourceMode)
        self.btnViewModeOptions = QtWidgets.QToolButton(self.wdgLeftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnViewModeOptions.sizePolicy().hasHeightForWidth())
        self.btnViewModeOptions.setSizePolicy(sizePolicy)
        self.btnViewModeOptions.setCheckable(True)
        self.btnViewModeOptions.setObjectName("btnViewModeOptions")
        self.horizontalLayout.addWidget(self.btnViewModeOptions)
        self.lblViewModeOptions = QtWidgets.QLabel(self.wdgLeftPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblViewModeOptions.sizePolicy().hasHeightForWidth())
        self.lblViewModeOptions.setSizePolicy(sizePolicy)
        self.lblViewModeOptions.setText("")
        self.lblViewModeOptions.setObjectName("lblViewModeOptions")
        self.horizontalLayout.addWidget(self.lblViewModeOptions)
        self.vlayoutViewMode.addLayout(self.horizontalLayout)
        self.swAddressSource = QtWidgets.QStackedWidget(self.wdgLeftPanel)
        self.swAddressSource.setObjectName("swAddressSource")
        self.pageAccountsListView = QtWidgets.QWidget()
        self.pageAccountsListView.setObjectName("pageAccountsListView")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pageAccountsListView)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.accountsListView = QtWidgets.QTreeView(self.pageAccountsListView)
        self.accountsListView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.accountsListView.setObjectName("accountsListView")
        self.accountsListView.header().setVisible(False)
        self.verticalLayout_8.addWidget(self.accountsListView)
        self.swAddressSource.addWidget(self.pageAccountsListView)
        self.pageMnListView = QtWidgets.QWidget()
        self.pageMnListView.setObjectName("pageMnListView")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.pageMnListView)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.widget_2 = QtWidgets.QWidget(self.pageMnListView)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.btnSelectAllMasternodes = QtWidgets.QToolButton(self.widget_2)
        self.btnSelectAllMasternodes.setObjectName("btnSelectAllMasternodes")
        self.verticalLayout_12.addWidget(self.btnSelectAllMasternodes)
        self.verticalLayout_10.addWidget(self.widget_2)
        self.mnListView = QtWidgets.QTableView(self.pageMnListView)
        self.mnListView.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mnListView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.mnListView.setShowGrid(False)
        self.mnListView.setObjectName("mnListView")
        self.mnListView.horizontalHeader().setVisible(False)
        self.mnListView.horizontalHeader().setStretchLastSection(True)
        self.mnListView.verticalHeader().setVisible(False)
        self.verticalLayout_10.addWidget(self.mnListView)
        self.swAddressSource.addWidget(self.pageMnListView)
        self.vlayoutViewMode.addWidget(self.swAddressSource)
        self.wdgRightPanel = QtWidgets.QWidget(self.splitterMain)
        self.wdgRightPanel.setObjectName("wdgRightPanel")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.wdgRightPanel)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.detailsTab = QtWidgets.QTabWidget(self.wdgRightPanel)
        self.detailsTab.setObjectName("detailsTab")
        self.tabSend = QtWidgets.QWidget()
        self.tabSend.setObjectName("tabSend")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabSend)
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.splitter = QtWidgets.QSplitter(self.tabSend)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.main_widget = QtWidgets.QWidget(self.splitter)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 8, -1, -1)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnCheckAll = QtWidgets.QToolButton(self.main_widget)
        self.btnCheckAll.setToolTip("")
        self.btnCheckAll.setIconSize(QtCore.QSize(12, 12))
        self.btnCheckAll.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnCheckAll.setObjectName("btnCheckAll")
        self.horizontalLayout_4.addWidget(self.btnCheckAll)
        self.btnUncheckAll = QtWidgets.QToolButton(self.main_widget)
        self.btnUncheckAll.setToolTip("")
        self.btnUncheckAll.setIconSize(QtCore.QSize(12, 12))
        self.btnUncheckAll.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.btnUncheckAll.setObjectName("btnUncheckAll")
        self.horizontalLayout_4.addWidget(self.btnUncheckAll)
        self.btnUtxoViewColumns = QtWidgets.QToolButton(self.main_widget)
        self.btnUtxoViewColumns.setObjectName("btnUtxoViewColumns")
        self.horizontalLayout_4.addWidget(self.btnUtxoViewColumns)
        self.chbHideCollateralTx = QtWidgets.QCheckBox(self.main_widget)
        self.chbHideCollateralTx.setStyleSheet("")
        self.chbHideCollateralTx.setObjectName("chbHideCollateralTx")
        self.horizontalLayout_4.addWidget(self.chbHideCollateralTx)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.utxoTableView = QtWidgets.QTableView(self.main_widget)
        self.utxoTableView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.utxoTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.utxoTableView.setShowGrid(True)
        self.utxoTableView.setSortingEnabled(False)
        self.utxoTableView.setObjectName("utxoTableView")
        self.utxoTableView.verticalHeader().setVisible(False)
        self.utxoTableView.verticalHeader().setCascadingSectionResizes(True)
        self.utxoTableView.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.utxoTableView)
        self.dest_widget1 = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dest_widget1.sizePolicy().hasHeightForWidth())
        self.dest_widget1.setSizePolicy(sizePolicy)
        self.dest_widget1.setObjectName("dest_widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dest_widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.dest_widget = QtWidgets.QFrame(self.dest_widget1)
        self.dest_widget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dest_widget.setObjectName("dest_widget")
        self.verticalLayout_3.addWidget(self.dest_widget)
        self.verticalLayout_5.addWidget(self.splitter)
        self.btnSend = QtWidgets.QPushButton(self.tabSend)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy)
        self.btnSend.setMinimumSize(QtCore.QSize(200, 0))
        self.btnSend.setMaximumSize(QtCore.QSize(200, 16777215))
        self.btnSend.setAutoDefault(False)
        self.btnSend.setObjectName("btnSend")
        self.verticalLayout_5.addWidget(self.btnSend)
        self.detailsTab.addTab(self.tabSend, "")
        self.tabTransactions = QtWidgets.QWidget()
        self.tabTransactions.setObjectName("tabTransactions")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.tabTransactions)
        self.verticalLayout_11.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnTxesViewColumns = QtWidgets.QToolButton(self.tabTransactions)
        self.btnTxesViewColumns.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btnTxesViewColumns.setObjectName("btnTxesViewColumns")
        self.horizontalLayout_2.addWidget(self.btnTxesViewColumns)
        self.btnTxesTabFilter = QtWidgets.QToolButton(self.tabTransactions)
        self.btnTxesTabFilter.setMaximumSize(QtCore.QSize(16777215, 22))
        self.btnTxesTabFilter.setCheckable(True)
        self.btnTxesTabFilter.setObjectName("btnTxesTabFilter")
        self.horizontalLayout_2.addWidget(self.btnTxesTabFilter)
        self.lblTxesTabFilterButton = QtWidgets.QLabel(self.tabTransactions)
        self.lblTxesTabFilterButton.setText("")
        self.lblTxesTabFilterButton.setObjectName("lblTxesTabFilterButton")
        self.horizontalLayout_2.addWidget(self.lblTxesTabFilterButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_2)
        self.txesTableView = QtWidgets.QTableView(self.tabTransactions)
        self.txesTableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.txesTableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.txesTableView.setObjectName("txesTableView")
        self.verticalLayout_11.addWidget(self.txesTableView)
        self.detailsTab.addTab(self.tabTransactions, "")
        self.tabDetails = QtWidgets.QWidget()
        self.tabDetails.setObjectName("tabDetails")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tabDetails)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.edtDetailsAddress = QtWidgets.QTextBrowser(self.tabDetails)
        self.edtDetailsAddress.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.edtDetailsAddress.setObjectName("edtDetailsAddress")
        self.verticalLayout_7.addWidget(self.edtDetailsAddress)
        self.detailsTab.addTab(self.tabDetails, "")
        self.verticalLayout_9.addWidget(self.detailsTab)
        self.verticalLayout_6.addWidget(self.splitterMain)
        self.verticalLayout.addWidget(self.widget)
        self.layStatusBar = QtWidgets.QHBoxLayout()
        self.layStatusBar.setSpacing(12)
        self.layStatusBar.setObjectName("layStatusBar")
        self.verticalLayout.addLayout(self.layStatusBar)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btnClose = QtWidgets.QPushButton(WalletDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClose.sizePolicy().hasHeightForWidth())
        self.btnClose.setSizePolicy(sizePolicy)
        self.btnClose.setMinimumSize(QtCore.QSize(0, 0))
        self.btnClose.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btnClose.setAutoDefault(False)
        self.btnClose.setObjectName("btnClose")
        self.horizontalLayout_3.addWidget(self.btnClose, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(WalletDlg)
        self.swAddressSource.setCurrentIndex(0)
        self.detailsTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(WalletDlg)

    def retranslateUi(self, WalletDlg):
        _translate = QtCore.QCoreApplication.translate
        WalletDlg.setWindowTitle(_translate("WalletDlg", "Dialog"))
        self.btnSetHwIdentityLabel.setToolTip(_translate("WalletDlg", "Set/change hw identity label"))
        self.btnSetHwIdentityLabel.setText(_translate("WalletDlg", "..."))
        self.btnPurgeHwIdentity.setToolTip(_translate("WalletDlg", "Purge this identity from cache"))
        self.btnPurgeHwIdentity.setText(_translate("WalletDlg", "..."))
        self.btnFetchTransactions.setToolTip(_translate("WalletDlg", "Force fetch transactions"))
        self.btnFetchTransactions.setText(_translate("WalletDlg", "..."))
        self.cboAddressSourceMode.setItemText(0, _translate("WalletDlg", "View As: Wallet Account"))
        self.cboAddressSourceMode.setItemText(1, _translate("WalletDlg", "View As: Masternode Address"))
        self.btnViewModeOptions.setToolTip(_translate("WalletDlg", "Options"))
        self.btnViewModeOptions.setText(_translate("WalletDlg", "..."))
        self.lblViewModeOptions.setToolTip(_translate("WalletDlg", "Options"))
        self.btnSelectAllMasternodes.setToolTip(_translate("WalletDlg", "Select all masternode addresses"))
        self.btnSelectAllMasternodes.setText(_translate("WalletDlg", "Select All"))
        self.btnCheckAll.setText(_translate("WalletDlg", "Select All"))
        self.btnUncheckAll.setText(_translate("WalletDlg", "Unselect All"))
        self.btnUtxoViewColumns.setText(_translate("WalletDlg", "Columns..."))
        self.chbHideCollateralTx.setText(_translate("WalletDlg", "Hide collateral utxos"))
        self.btnSend.setText(_translate("WalletDlg", "Prepare Transaction"))
        self.detailsTab.setTabText(self.detailsTab.indexOf(self.tabSend), _translate("WalletDlg", "Send"))
        self.btnTxesViewColumns.setText(_translate("WalletDlg", "Columns..."))
        self.btnTxesTabFilter.setText(_translate("WalletDlg", "."))
        self.lblTxesTabFilterButton.setToolTip(_translate("WalletDlg", "Filter conditions"))
        self.detailsTab.setTabText(self.detailsTab.indexOf(self.tabTransactions), _translate("WalletDlg", "Transactions"))
        self.detailsTab.setTabText(self.detailsTab.indexOf(self.tabDetails), _translate("WalletDlg", "Details"))
        self.btnClose.setText(_translate("WalletDlg", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WalletDlg = QtWidgets.QDialog()
    ui = Ui_WalletDlg()
    ui.setupUi(WalletDlg)
    WalletDlg.show()
    sys.exit(app.exec_())


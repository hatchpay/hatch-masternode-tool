# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/HMT-git/src/ui/ui_wallet_dlg_options1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WdgOptions1(object):
    def setupUi(self, WdgOptions1):
        WdgOptions1.setObjectName("WdgOptions1")
        WdgOptions1.resize(243, 76)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WdgOptions1.sizePolicy().hasHeightForWidth())
        WdgOptions1.setSizePolicy(sizePolicy)
        WdgOptions1.setStyleSheet("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(WdgOptions1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(WdgOptions1)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chbShowAddresses = QtWidgets.QCheckBox(self.frame)
        self.chbShowAddresses.setObjectName("chbShowAddresses")
        self.verticalLayout.addWidget(self.chbShowAddresses)
        self.chbShowZeroBalanceAddresses = QtWidgets.QCheckBox(self.frame)
        self.chbShowZeroBalanceAddresses.setObjectName("chbShowZeroBalanceAddresses")
        self.verticalLayout.addWidget(self.chbShowZeroBalanceAddresses)
        self.chbShowNotUsedAddresses = QtWidgets.QCheckBox(self.frame)
        self.chbShowNotUsedAddresses.setObjectName("chbShowNotUsedAddresses")
        self.verticalLayout.addWidget(self.chbShowNotUsedAddresses)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btnApply = QtWidgets.QToolButton(self.frame)
        self.btnApply.setObjectName("btnApply")
        self.horizontalLayout.addWidget(self.btnApply)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(WdgOptions1)
        QtCore.QMetaObject.connectSlotsByName(WdgOptions1)

    def retranslateUi(self, WdgOptions1):
        _translate = QtCore.QCoreApplication.translate
        WdgOptions1.setWindowTitle(_translate("WdgOptions1", "Form"))
        self.chbShowAddresses.setText(_translate("WdgOptions1", "Show individual addresses"))
        self.chbShowZeroBalanceAddresses.setText(_translate("WdgOptions1", "Show addresses with zero balance"))
        self.chbShowNotUsedAddresses.setText(_translate("WdgOptions1", "Show addresses not yet used"))
        self.btnApply.setText(_translate("WdgOptions1", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WdgOptions1 = QtWidgets.QWidget()
    ui = Ui_WdgOptions1()
    ui.setupUi(WdgOptions1)
    WdgOptions1.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/HMT-git/src/ui/ui_hw_word_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_HardwareWalletWordDlg(object):
    def setupUi(self, HardwareWalletWordDlg):
        HardwareWalletWordDlg.setObjectName("HardwareWalletWordDlg")
        HardwareWalletWordDlg.resize(334, 88)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HardwareWalletWordDlg.sizePolicy().hasHeightForWidth())
        HardwareWalletWordDlg.setSizePolicy(sizePolicy)
        HardwareWalletWordDlg.setMinimumSize(QtCore.QSize(0, 0))
        HardwareWalletWordDlg.setMaximumSize(QtCore.QSize(1000, 1000))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        HardwareWalletWordDlg.setFont(font)
        HardwareWalletWordDlg.setModal(True)
        self.verticalLayout = QtWidgets.QVBoxLayout(HardwareWalletWordDlg)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lblWord = QtWidgets.QLabel(HardwareWalletWordDlg)
        self.lblWord.setObjectName("lblWord")
        self.horizontalLayout_2.addWidget(self.lblWord)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.edtWord = QtWidgets.QLineEdit(HardwareWalletWordDlg)
        self.edtWord.setObjectName("edtWord")
        self.verticalLayout.addWidget(self.edtWord)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnEnter = QtWidgets.QPushButton(HardwareWalletWordDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEnter.sizePolicy().hasHeightForWidth())
        self.btnEnter.setSizePolicy(sizePolicy)
        self.btnEnter.setMinimumSize(QtCore.QSize(150, 0))
        self.btnEnter.setAutoRepeatDelay(36)
        self.btnEnter.setAutoDefault(False)
        self.btnEnter.setDefault(True)
        self.btnEnter.setObjectName("btnEnter")
        self.horizontalLayout.addWidget(self.btnEnter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(HardwareWalletWordDlg)
        QtCore.QMetaObject.connectSlotsByName(HardwareWalletWordDlg)

    def retranslateUi(self, HardwareWalletWordDlg):
        _translate = QtCore.QCoreApplication.translate
        HardwareWalletWordDlg.setWindowTitle(_translate("HardwareWalletWordDlg", "Dialog"))
        self.lblWord.setText(_translate("HardwareWalletWordDlg", "Word:"))
        self.btnEnter.setText(_translate("HardwareWalletWordDlg", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HardwareWalletWordDlg = QtWidgets.QDialog()
    ui = Ui_HardwareWalletWordDlg()
    ui.setupUi(HardwareWalletWordDlg)
    HardwareWalletWordDlg.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/HMT-git/src/ui/ui_conn_rpc_wdg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RpcConnection(object):
    def setupUi(self, RpcConnection):
        RpcConnection.setObjectName("RpcConnection")
        RpcConnection.resize(370, 159)
        self.verticalLayout = QtWidgets.QVBoxLayout(RpcConnection)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.edtRpcUsername = QtWidgets.QLineEdit(RpcConnection)
        self.edtRpcUsername.setObjectName("edtRpcUsername")
        self.gridLayout.addWidget(self.edtRpcUsername, 2, 1, 1, 1)
        self.chbRpcSSL = QtWidgets.QCheckBox(RpcConnection)
        self.chbRpcSSL.setObjectName("chbRpcSSL")
        self.gridLayout.addWidget(self.chbRpcSSL, 4, 0, 1, 2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.edtRpcPassword = QtWidgets.QLineEdit(RpcConnection)
        self.edtRpcPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.edtRpcPassword.setObjectName("edtRpcPassword")
        self.horizontalLayout_5.addWidget(self.edtRpcPassword)
        self.btnShowPassword = QtWidgets.QToolButton(RpcConnection)
        self.btnShowPassword.setObjectName("btnShowPassword")
        self.horizontalLayout_5.addWidget(self.btnShowPassword)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.lblRpcUsername = QtWidgets.QLabel(RpcConnection)
        self.lblRpcUsername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblRpcUsername.setObjectName("lblRpcUsername")
        self.gridLayout.addWidget(self.lblRpcUsername, 2, 0, 1, 1)
        self.lblRpcHost = QtWidgets.QLabel(RpcConnection)
        self.lblRpcHost.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblRpcHost.setObjectName("lblRpcHost")
        self.gridLayout.addWidget(self.lblRpcHost, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.edtRpcHost = QtWidgets.QLineEdit(RpcConnection)
        self.edtRpcHost.setObjectName("edtRpcHost")
        self.horizontalLayout.addWidget(self.edtRpcHost)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.lblRpcPassword = QtWidgets.QLabel(RpcConnection)
        self.lblRpcPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lblRpcPassword.setObjectName("lblRpcPassword")
        self.gridLayout.addWidget(self.lblRpcPassword, 3, 0, 1, 1)
        self.lblRpcPort = QtWidgets.QLabel(RpcConnection)
        self.lblRpcPort.setObjectName("lblRpcPort")
        self.gridLayout.addWidget(self.lblRpcPort, 1, 0, 1, 1)
        self.edtRpcPort = QtWidgets.QLineEdit(RpcConnection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edtRpcPort.sizePolicy().hasHeightForWidth())
        self.edtRpcPort.setSizePolicy(sizePolicy)
        self.edtRpcPort.setMaximumSize(QtCore.QSize(50, 16777215))
        self.edtRpcPort.setObjectName("edtRpcPort")
        self.gridLayout.addWidget(self.edtRpcPort, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(RpcConnection)
        QtCore.QMetaObject.connectSlotsByName(RpcConnection)
        RpcConnection.setTabOrder(self.edtRpcHost, self.edtRpcPort)
        RpcConnection.setTabOrder(self.edtRpcPort, self.edtRpcUsername)
        RpcConnection.setTabOrder(self.edtRpcUsername, self.edtRpcPassword)
        RpcConnection.setTabOrder(self.edtRpcPassword, self.chbRpcSSL)
        RpcConnection.setTabOrder(self.chbRpcSSL, self.btnShowPassword)

    def retranslateUi(self, RpcConnection):
        _translate = QtCore.QCoreApplication.translate
        RpcConnection.setWindowTitle(_translate("RpcConnection", "Form"))
        self.chbRpcSSL.setText(_translate("RpcConnection", "SSL"))
        self.btnShowPassword.setToolTip(_translate("RpcConnection", "Show password"))
        self.btnShowPassword.setText(_translate("RpcConnection", "..."))
        self.lblRpcUsername.setText(_translate("RpcConnection", "RPC username:"))
        self.lblRpcHost.setText(_translate("RpcConnection", "RPC host:"))
        self.lblRpcPassword.setText(_translate("RpcConnection", "RPC password:"))
        self.lblRpcPort.setText(_translate("RpcConnection", "RPC port:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RpcConnection = QtWidgets.QWidget()
    ui = Ui_RpcConnection()
    ui.setupUi(RpcConnection)
    RpcConnection.show()
    sys.exit(app.exec_())


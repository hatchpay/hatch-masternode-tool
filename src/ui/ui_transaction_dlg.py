# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/blogin/PycharmProjects/HMT-git/src/ui/ui_transaction_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TransactionDlg(object):
    def setupUi(self, TransactionDlg):
        TransactionDlg.setObjectName("TransactionDlg")
        TransactionDlg.resize(585, 316)
        self.verticalLayout = QtWidgets.QVBoxLayout(TransactionDlg)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stacket_widget = QtWidgets.QStackedWidget(TransactionDlg)
        self.stacket_widget.setObjectName("stacket_widget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.edt_recipients = QtWidgets.QTextBrowser(self.page)
        self.edt_recipients.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.edt_recipients.setStyleSheet("QTextBrowser {background-color: white;}")
        self.edt_recipients.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.edt_recipients.setOpenLinks(False)
        self.edt_recipients.setObjectName("edt_recipients")
        self.verticalLayout_4.addWidget(self.edt_recipients)
        self.stacket_widget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.edt_raw_transaction = QtWidgets.QPlainTextEdit(self.page_2)
        self.edt_raw_transaction.setStyleSheet("font: 13pt \"Courier New\";\n"
"\n"
"")
        self.edt_raw_transaction.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.edt_raw_transaction.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.edt_raw_transaction.setReadOnly(True)
        self.edt_raw_transaction.setObjectName("edt_raw_transaction")
        self.verticalLayout_5.addWidget(self.edt_raw_transaction)
        self.chb_word_wrap = QtWidgets.QCheckBox(self.page_2)
        self.chb_word_wrap.setObjectName("chb_word_wrap")
        self.verticalLayout_5.addWidget(self.chb_word_wrap)
        self.stacket_widget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stacket_widget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, 2, 6, 6)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_details = QtWidgets.QPushButton(TransactionDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_details.sizePolicy().hasHeightForWidth())
        self.btn_details.setSizePolicy(sizePolicy)
        self.btn_details.setAutoDefault(False)
        self.btn_details.setObjectName("btn_details")
        self.gridLayout.addWidget(self.btn_details, 0, 0, 1, 1)
        self.btn_close = QtWidgets.QPushButton(TransactionDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setAutoDefault(False)
        self.btn_close.setObjectName("btn_close")
        self.gridLayout.addWidget(self.btn_close, 0, 4, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.btn_broadcast = QtWidgets.QPushButton(TransactionDlg)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_broadcast.sizePolicy().hasHeightForWidth())
        self.btn_broadcast.setSizePolicy(sizePolicy)
        self.btn_broadcast.setMinimumSize(QtCore.QSize(0, 0))
        self.btn_broadcast.setAutoDefault(False)
        self.btn_broadcast.setObjectName("btn_broadcast")
        self.gridLayout.addWidget(self.btn_broadcast, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(TransactionDlg)
        self.stacket_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TransactionDlg)

    def retranslateUi(self, TransactionDlg):
        _translate = QtCore.QCoreApplication.translate
        TransactionDlg.setWindowTitle(_translate("TransactionDlg", "Dialog"))
        self.edt_recipients.setHtml(_translate("TransactionDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.chb_word_wrap.setText(_translate("TransactionDlg", "Word wrap"))
        self.btn_details.setText(_translate("TransactionDlg", "Show Details"))
        self.btn_close.setText(_translate("TransactionDlg", "Close"))
        self.btn_broadcast.setText(_translate("TransactionDlg", "Send Transaction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TransactionDlg = QtWidgets.QDialog()
    ui = Ui_TransactionDlg()
    ui.setupUi(TransactionDlg)
    TransactionDlg.show()
    sys.exit(app.exec_())


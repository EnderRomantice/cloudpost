# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cloudDemo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(882, 594)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftOut = QTextEdit(self.centralwidget)
        self.leftOut.setObjectName(u"leftOut")
        self.leftOut.setMinimumSize(QSize(130, 20))
        self.leftOut.setMaximumSize(QSize(16777215, 481))

        self.horizontalLayout.addWidget(self.leftOut, 0, Qt.AlignmentFlag.AlignLeft)

        self.rightOut = QTextEdit(self.centralwidget)
        self.rightOut.setObjectName(u"rightOut")
        self.rightOut.setMinimumSize(QSize(451, 312))

        self.horizontalLayout.addWidget(self.rightOut)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.logSave = QComboBox(self.centralwidget)
        self.logSave.addItem("")
        self.logSave.addItem("")
        self.logSave.setObjectName(u"logSave")
        self.logSave.setMinimumSize(QSize(101, 53))

        self.horizontalLayout_5.addWidget(self.logSave)

        self.outUse = QComboBox(self.centralwidget)
        self.outUse.addItem("")
        self.outUse.addItem("")
        self.outUse.setObjectName(u"outUse")
        self.outUse.setMinimumSize(QSize(101, 53))

        self.horizontalLayout_5.addWidget(self.outUse)

        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(101, 53))

        self.horizontalLayout_5.addWidget(self.startButton)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.reqMethod = QComboBox(self.centralwidget)
        self.reqMethod.addItem("")
        self.reqMethod.addItem("")
        self.reqMethod.addItem("")
        self.reqMethod.addItem("")
        self.reqMethod.setObjectName(u"reqMethod")
        self.reqMethod.setMinimumSize(QSize(101, 52))
        self.reqMethod.setStyleSheet(u"text-align: center;")

        self.horizontalLayout_2.addWidget(self.reqMethod)

        self.codeUse = QComboBox(self.centralwidget)
        self.codeUse.addItem("")
        self.codeUse.addItem("")
        self.codeUse.setObjectName(u"codeUse")
        self.codeUse.setMinimumSize(QSize(101, 53))

        self.horizontalLayout_2.addWidget(self.codeUse)

        self.urlInput = QLineEdit(self.centralwidget)
        self.urlInput.setObjectName(u"urlInput")
        self.urlInput.setMinimumSize(QSize(631, 51))

        self.horizontalLayout_2.addWidget(self.urlInput)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.postLabel = QLabel(self.centralwidget)
        self.postLabel.setObjectName(u"postLabel")

        self.horizontalLayout_3.addWidget(self.postLabel)

        self.postInput = QLineEdit(self.centralwidget)
        self.postInput.setObjectName(u"postInput")
        self.postInput.setMinimumSize(QSize(631, 51))

        self.horizontalLayout_3.addWidget(self.postInput)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"cloudpost", None))
        self.logSave.setItemText(0, QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.logSave.setItemText(1, QCoreApplication.translate("MainWindow", u"NO_SAVA", None))

        self.outUse.setItemText(0, QCoreApplication.translate("MainWindow", u"HTML", None))
        self.outUse.setItemText(1, QCoreApplication.translate("MainWindow", u"JSON", None))

        self.startButton.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.reqMethod.setItemText(0, QCoreApplication.translate("MainWindow", u"GET", None))
        self.reqMethod.setItemText(1, QCoreApplication.translate("MainWindow", u"POST", None))
        self.reqMethod.setItemText(2, QCoreApplication.translate("MainWindow", u"PUT", None))
        self.reqMethod.setItemText(3, QCoreApplication.translate("MainWindow", u"DELETE", None))

        self.codeUse.setItemText(0, QCoreApplication.translate("MainWindow", u"https://", None))
        self.codeUse.setItemText(1, QCoreApplication.translate("MainWindow", u"http://", None))

        self.postLabel.setText(QCoreApplication.translate("MainWindow", u"POST_DATA", None))
    # retranslateUi


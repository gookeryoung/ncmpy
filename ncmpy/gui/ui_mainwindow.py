# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from gui.droplistwidget import DropListWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 464)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(600, 450))
        font = QFont()
        font.setFamily(u"HarmonyOS Sans SC")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"HarmonyOS Sans SC\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.hlOutDir = QHBoxLayout()
        self.hlOutDir.setObjectName(u"hlOutDir")
        self.labelOutDir = QLabel(self.centralwidget)
        self.labelOutDir.setObjectName(u"labelOutDir")

        self.hlOutDir.addWidget(self.labelOutDir)

        self.cbOutDir = QComboBox(self.centralwidget)
        self.cbOutDir.setObjectName(u"cbOutDir")
        self.cbOutDir.setMinimumSize(QSize(400, 0))

        self.hlOutDir.addWidget(self.cbOutDir)

        self.pbOpenOutDir = QPushButton(self.centralwidget)
        self.pbOpenOutDir.setObjectName(u"pbOpenOutDir")

        self.hlOutDir.addWidget(self.pbOpenOutDir)


        self.verticalLayout.addLayout(self.hlOutDir)

        self.pbOpenFolder = QPushButton(self.centralwidget)
        self.pbOpenFolder.setObjectName(u"pbOpenFolder")

        self.verticalLayout.addWidget(self.pbOpenFolder)

        self.labelFiles = QLabel(self.centralwidget)
        self.labelFiles.setObjectName(u"labelFiles")
        self.labelFiles.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.labelFiles)

        self.lwFiles = DropListWidget(self.centralwidget)
        self.lwFiles.setObjectName(u"lwFiles")
        self.lwFiles.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lwFiles.setDragDropMode(QAbstractItemView.InternalMove)
        self.lwFiles.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.lwFiles)

        self.hlProcess = QHBoxLayout()
        self.hlProcess.setObjectName(u"hlProcess")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.hlProcess.addWidget(self.progressBar)

        self.pbProcess = QPushButton(self.centralwidget)
        self.pbProcess.setObjectName(u"pbProcess")

        self.hlProcess.addWidget(self.pbProcess)


        self.verticalLayout.addLayout(self.hlProcess)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ncmppGui", None))
        self.labelOutDir.setText(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u76ee\u5f55:", None))
        self.pbOpenOutDir.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u76ee\u5f55", None))
        self.pbOpenFolder.setText(QCoreApplication.translate("MainWindow", u"\u4ece\u6587\u4ef6\u5939\u5bfc\u5165ncm\u6587\u4ef6", None))
        self.labelFiles.setText(QCoreApplication.translate("MainWindow", u"\u5c06ncm\u6587\u4ef6\u62d6\u62fd\u81f3\u4e0b\u65b9", None))
        self.pbProcess.setText(QCoreApplication.translate("MainWindow", u"\u5904\u7406\u6587\u4ef6", None))
    # retranslateUi


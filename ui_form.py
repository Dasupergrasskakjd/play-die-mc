# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.startButton = QPushButton(self.centralwidget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(130, 80, 121, 51))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.startButton.setFont(font)
        self.button_quit = QPushButton(self.centralwidget)
        self.button_quit.setObjectName(u"button_quit")
        self.button_quit.setGeometry(QRect(320, 250, 80, 24))
        self.maintext = QLabel(self.centralwidget)
        self.maintext.setObjectName(u"maintext")
        self.maintext.setGeometry(QRect(82, 55, 201, 141))
        font1 = QFont()
        font1.setPointSize(12)
        self.maintext.setFont(font1)
        self.maintext.setAutoFillBackground(False)
        self.maintext.setStyleSheet(u"QLabel { background: white }")
        self.maintext.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(190, 220, 80, 24))
        self.nextButton = QPushButton(self.centralwidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setGeometry(QRect(280, 220, 80, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.button_quit.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"\u958b\u59cb\u6e38\u6232", None))
        self.button_quit.setText(QCoreApplication.translate("MainWindow", u"\u96e2\u958b", None))
        self.maintext.setText(QCoreApplication.translate("MainWindow", u"\u9810\u8a2d\u6587\u5b57", None))
        self.backButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u6b65", None))
        self.nextButton.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u6b65", None))
    # retranslateUi


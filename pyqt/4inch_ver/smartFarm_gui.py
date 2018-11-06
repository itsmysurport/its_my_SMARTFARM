# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\smartFarm_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 480, 320))
        self.background.setStyleSheet("background-color: rgb(35, 44, 53);")
        self.background.setObjectName("background")
        self.navigation_bar = QtWidgets.QWidget(self.background)
        self.navigation_bar.setGeometry(QtCore.QRect(0, 0, 480, 40))
        self.navigation_bar.setStyleSheet("background-color: rgb(128, 160, 193);")
        self.navigation_bar.setObjectName("navigation_bar")
        self.widget = QtWidgets.QWidget(self.navigation_bar)
        self.widget.setGeometry(QtCore.QRect(0, 0, 191, 40))
        self.widget.setStyleSheet("background-image: url(:/Texts/images_backup/title.png);")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.background)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 75, 30))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setStyleSheet("background-image: url(:/icon/images_backup/on.svg);\n"
"border: none;")
        self.pushButton.setText("")
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


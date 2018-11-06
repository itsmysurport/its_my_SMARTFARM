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
        MainWindow.resize(800, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.background.setStyleSheet("background-color: rgb(35, 44, 53);")
        self.background.setObjectName("background")
        self.navigation_bar = QtWidgets.QWidget(self.background)
        self.navigation_bar.setGeometry(QtCore.QRect(0, 0, 800, 67))
        self.navigation_bar.setStyleSheet("background-color: rgb(128, 160, 193);")
        self.navigation_bar.setObjectName("navigation_bar")
        self.widget = QtWidgets.QWidget(self.navigation_bar)
        self.widget.setGeometry(QtCore.QRect(12, 13, 441, 43))
        self.widget.setStyleSheet("background-image: url(:/Texts/images_backup/7inch_title.png);")
        self.widget.setObjectName("widget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.background)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 70, 800, 413))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.ui_widget = QtWidgets.QWidget(self.page)
        self.ui_widget.setGeometry(QtCore.QRect(210, 10, 553, 363))
        self.ui_widget.setStyleSheet("background-image:url(:/Widget/images_backup/fisrt_ui.png)")
        self.ui_widget.setObjectName("ui_widget")
        self.red_bulb = QtWidgets.QWidget(self.ui_widget)
        self.red_bulb.setGeometry(QtCore.QRect(251, 45, 67, 81))
        self.red_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_red_bulb.png);")
        self.red_bulb.setObjectName("red_bulb")
        self.green_bulb = QtWidgets.QWidget(self.ui_widget)
        self.green_bulb.setGeometry(QtCore.QRect(357, 45, 67, 81))
        self.green_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_green_bulb.png);")
        self.green_bulb.setObjectName("green_bulb")
        self.white_bulb = QtWidgets.QWidget(self.ui_widget)
        self.white_bulb.setGeometry(QtCore.QRect(462, 45, 67, 81))
        self.white_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_white_bulb.png);")
        self.white_bulb.setObjectName("white_bulb")
        self.redButton = QtWidgets.QPushButton(self.page)
        self.redButton.setGeometry(QtCore.QRect(95, 26, 117, 46))
        self.redButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.redButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
"border : none;")
        self.redButton.setText("")
        self.redButton.setFlat(False)
        self.redButton.setObjectName("redButton")
        self.greenButton = QtWidgets.QPushButton(self.page)
        self.greenButton.setGeometry(QtCore.QRect(95, 94, 117, 46))
        self.greenButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.greenButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
"border : none;")
        self.greenButton.setText("")
        self.greenButton.setFlat(False)
        self.greenButton.setObjectName("greenButton")
        self.whiteButton = QtWidgets.QPushButton(self.page)
        self.whiteButton.setGeometry(QtCore.QRect(95, 162, 117, 46))
        self.whiteButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.whiteButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
"border : none;")
        self.whiteButton.setText("")
        self.whiteButton.setFlat(False)
        self.whiteButton.setObjectName("whiteButton")
        self.humiLabel = QtWidgets.QLabel(self.page)
        self.humiLabel.setGeometry(QtCore.QRect(95, 295, 117, 33))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(31)
        self.humiLabel.setFont(font)
        self.humiLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.humiLabel.setTextFormat(QtCore.Qt.AutoText)
        self.humiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.humiLabel.setObjectName("humiLabel")
        self.tempLabel = QtWidgets.QLabel(self.page)
        self.tempLabel.setGeometry(QtCore.QRect(95, 348, 117, 33))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 Light")
        font.setPointSize(31)
        self.tempLabel.setFont(font)
        self.tempLabel.setStyleSheet("color: rgb(255, 255, 255);")
        self.tempLabel.setTextFormat(QtCore.Qt.AutoText)
        self.tempLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.tempLabel.setObjectName("tempLabel")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.humiLabel.setText(_translate("MainWindow", "99%"))
        self.tempLabel.setText(_translate("MainWindow", "99°C"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


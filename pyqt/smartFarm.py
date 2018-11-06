from PyQt5 import QtCore, QtGui, QtWidgets
from smartFarm_gui import *

red_status = 1
green_status = 1
white_status = 1

# define event in PyQt
def event(self):
    self.redButton.clicked.connect(self.red_onoff)
    self.greenButton.clicked.connect(self.green_onoff)
    self.whiteButton.clicked.connect(self.white_onoff)

def red_onoff(self):
    global red_status
    print('Clicked')
    if(red_status):
        self.redButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_off_button.png);\n"
        "border: none;")
        self.red_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_off_bulb.png);\n")
        # LED OFF CODE
        red_status=0
    else:
        self.redButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
        "border: none;")
        self.red_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_red_bulb.png);\n")
        # LED ON CODE
        red_status=1

def green_onoff(self):
    global green_status
    print('Clicked')
    if(green_status):
        self.greenButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_off_button.png);\n"
        "border: none;")
        self.green_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_off_bulb.png);\n")
        # LED OFF CODE
        green_status=0
    else:
        self.greenButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
        "border: none;")
        self.green_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_green_bulb.png);\n")
        # LED ON CODE
        green_status=1

def white_onoff(self):
    global white_status
    print('Clicked')
    if(white_status):
        self.whiteButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_off_button.png);\n"
        "border: none;")
        self.white_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_off_bulb.png);\n")
        # LED OFF CODE
        white_status=0
    else:
        self.whiteButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
        "border: none;")
        self.white_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_white_bulb.png);\n")
        # LED ON CODE
        white_status=1

Ui_MainWindow.event = event
Ui_MainWindow.red_onoff = red_onoff
Ui_MainWindow.green_onoff = green_onoff
Ui_MainWindow.white_onoff = white_onoff

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()

    sys.exit(app.exec_())

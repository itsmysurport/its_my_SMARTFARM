from PyQt5 import QtCore, QtGui, QtWidgets
from smartFarm_gui import *
led_status = 0

def event(self):
    self.pushButton.clicked.connect(self.debu_func)

def debu_func(self):
    global led_status
    print('Clicked')
    if(led_status):
        self.pushButton.setStyleSheet("background-image: url(:/icon/images_backup/on.svg);\n"
        "border: none;")
        # LED OFF CODE
        led_status=0
    else:
        self.pushButton.setStyleSheet("background-image: url(:/icon/images_backup/off.svg);\n"
        "border: none;")
        # LED ON CODE
        led_status=1

Ui_MainWindow.event = event
Ui_MainWindow.debu_func = debu_func

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.event()
    MainWindow.show()

    sys.exit(app.exec_())

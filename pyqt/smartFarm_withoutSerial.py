from smartFarm_gui import *
import pyqtgraph as pg
import threading
import time
import random

red_status = 1
green_status = 1
white_status = 1

# define event in PyQt
def event(self):
    self.redButton.clicked.connect(self.red_onoff)
    self.greenButton.clicked.connect(self.green_onoff)
    self.whiteButton.clicked.connect(self.white_onoff)

    self.controlMenu.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(0))
    self.dataMenu.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(1))
    self.graphMenu.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(2))
    self.cameraMenu.clicked.connect(lambda x:self.stackedWidget.setCurrentIndex(3))

    self.controlMenu.clicked.connect(self.update)
    self.dataMenu.clicked.connect(self.update)
    self.graphMenu.clicked.connect(self.update)
    self.cameraMenu.clicked.connect(self.update)

def red_onoff(self):
    global red_status, green_status, white_status
    red = '000'
    green = '000'
    white = '000'
    print('Clicked')

    # Control Device
    if(green_status):   green='255'
    if(white_status):   white='255'

    if(red_status):
        # Control GUI CODE
        self.redButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_off_button.png);\n"
        "border: none;")
        self.red_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_off_bulb.png);\n")

        # LED OFF CODE
        red_status=0
    else:
        # Control GUI CODE
        print('OFF')
        self.redButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
        "border: none;")
        self.red_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_red_bulb.png);\n")

        red = '255'

        # LED ON CODE
        red_status=1

    # run function
    message = '\x02' + 'L01' + 'F000' + 'R' + red + 'W' + white + 'B' + green + '\x03\r\n'
    # ser.write(bytes(message.encode()))
    print(message)

def green_onoff(self):
    global red_status, green_status, white_status
    red = '000'
    green = '000'
    white = '000'
    print('Clicked')

    # Control Device
    if(red_status):   red='255'
    if(white_status):   white='255'

    if(green_status):
        # Control GUI CODE
        self.greenButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_off_button.png);\n"
        "border: none;")
        self.green_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_off_bulb.png);\n")

        # LED OFF CODE
        green_status=0
    else:
        self.greenButton.setStyleSheet("background-image: url(:/icon/images_backup/117x46_on_button.png);\n"
        "border: none;")
        self.green_bulb.setStyleSheet("background-image: url(:/icon/images_backup/67x81_green_bulb.png);\n")

        green = '255'
        # LED ON CODE
        green_status=1

    # run function
    message = '\x02' + 'L01' + 'F000' + 'R' + red + 'W' + white + 'B' + green + '\x03\r\n'
    # ser.write(bytes(message.encode()))
    print(message)

def white_onoff(self):
    global red_status, green_status, white_status
    red = '000'
    green = '000'
    white = '000'
    print('Clicked')

    # Control Device
    if(red_status):   red='255'
    if(green_status):   green='255'

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

        white = '255'
        # LED ON CODE
        white_status=1

    # run function
    message = '\x02' + 'L01' + 'F000' + 'R' + red + 'W' + white + 'B' + green + '\x03\r\n'
    # ser.write(bytes(message.encode()))
    print(message)

def update(self):
    if (self.stackedWidget.currentIndex()) == 2:    # Is the selected current menu 'Graph'?
        self.onGraph = True
    else:
        self.onGraph = False

def updating(self):
    while True:
        if (self.stackedWidget.currentIndex()) == 2:
            self.plotting()
            print('count')
        else:
            pass

def plotting(self):
    if input():
        data = random.randrange(0,31)
        self.a.append(data)
        print(self.a)
        self.tempView.clear()
        self.tempView.plot(self.a, pen = pg.mkPen(color=(255, 100, 25)))

Ui_MainWindow.event = event
Ui_MainWindow.red_onoff = red_onoff
Ui_MainWindow.green_onoff = green_onoff
Ui_MainWindow.white_onoff = white_onoff
Ui_MainWindow.plotting = plotting
Ui_MainWindow.update = update
Ui_MainWindow.updating = updating
Ui_MainWindow.onGraph = False
Ui_MainWindow.a = []

if __name__=="__main__":
    import sys
    from PyQt5.QtCore import QUrl
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.stackedWidget.setCurrentIndex(0)
    ui.event()
    ui.widget_2.setUrl(QUrl("http://www.naver.com/"))
    t = threading.Thread(target=ui.updating, args=())
    t.start()
    # ser.write(bytes('\x02L01F000R255W255B255\x03\r\n'.encode()))    # Device __init__
    MainWindow.show()

    sys.exit(app.exec_())

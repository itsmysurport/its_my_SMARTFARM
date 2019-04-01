import serial
from smartFarm_gui import *


class ConnectHelper(object):
    def __init__(self, ui):
        self.ui = ui
        self.HelperEvent()

    def HelperEvent(self):
        self.ui.connectButton.clicked.connect(self.ConnectDevice)
        self.ui.restartButton.clicked.connect(self.ConnectDevice)

    def ConnectDevice(self):
        try:
            ser = serial.Serial(port='COM5',
                                baudrate=115200,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
            self.ui.loadnstart.setCurrentIndex(2)
            return
        except serial.serialutil.SerialException:
            self.ui.loadnstart.setCurrentIndex(1)
            print('ERROR: Invaild Connection')
            return

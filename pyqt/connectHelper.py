import serial
from smartFarm_gui import *

class connectHelper(object):
    def helperEvent(self):
        self.connectButton.clicked.connect()
        self.reconnectButton.clicked.connect()

    def connectDevice(self):
        try:
            ser = serial.Serial(port='COM5',
                                baudrate=115200,
                                parity=serial.PARITY_NONE,
                                stopbits=serial.STOPBITS_ONE,
                                bytesize=serial.EIGHTBITS,
                                timeout=1)
        except serial.serialutil.SerialException:
            self.

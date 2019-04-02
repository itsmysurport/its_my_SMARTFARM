import serial

class ConnectHelper(object):
    def __init__(self, ui):
        self.ui = ui

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

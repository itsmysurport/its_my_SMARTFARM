from smartFarm_gui import *

class DebugMode(object):
    def __init__(self, ui):
        self.status = 0
        self.ui = ui
        self.Mode1()

    def Mode1(self):
        self.ui.debugButton.clicked.connect(self.StatusStack)

    def StatusStack(self):
        self.status += 1
        print('If you want to connect to Debug Mode, Repeat %d times'%(10-self.status))
        if self.status >= 10:
            self.ui.loadnstart.setCurrentIndex(2)

class DebugMode(object):
    def __init__(self, ui):
        self.status = 0
        self.ui = ui


    def StatusStack(self):
        self.status += 1
        print('If you want to connect to Debug Mode, Repeat %d times'%(10-self.status))
        if self.status >= 10:
            self.ui.loadnstart.setCurrentIndex(2)

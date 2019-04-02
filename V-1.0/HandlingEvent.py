from startPage import *
from mainPage import *

class HandleEvent(object):
    def __init__(self, ui):
        self.ui = ui
        self.ConnectHelp = ConnectHelper.ConnectHelper(ui)
        self.DebugMode = Debug_pg.DebugMode(ui)
        self.controlPage = controlPage.Control(ui)
        self.event()

    def event(self):
        # Connection
        self.ui.connectButton.clicked.connect(self.ConnectHelp.ConnectDevice)
        self.ui.restartButton.clicked.connect(self.ConnectHelp.ConnectDevice)
        # Debug Mode
        self.ui.debugButton.clicked.connect(self.DebugMode.StatusStack)
        # Main Menu Bar
        self.ui.controlButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(0))
        self.ui.statusButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(1))
        self.ui.graphButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(2))
        self.ui.cameraButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(3))
        # Control Page
        self.ui.blueButton.clicked.connect(self.controlPage.test)

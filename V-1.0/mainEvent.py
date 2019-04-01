from smartFarm_gui import *

class smartFarmMain(object):
    def __init__(self, ui):
        self.ui = ui
        self.event()

    def event(self):
        self.ui.controlButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(0))
        self.ui.statusButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(1))
        self.ui.graphButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(2))
        self.ui.cameraButton.clicked.connect(lambda x: self.ui.mainFarm.setCurrentIndex(3))

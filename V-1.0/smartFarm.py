from smartFarm_gui import *
from ConnectHelper import *
from Debug_pg import *
from mainEvent import *

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    ConnectHelp = ConnectHelper(ui)
    DebugMode = DebugMode(ui)
    mainEvent = smartFarmMain(ui)

    MainWindow.show()
    sys.exit(app.exec_())

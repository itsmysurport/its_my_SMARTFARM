from smartFarm_gui import *
from ConnectHelper import *
from Debug_pg import *

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ch = ConnectHelper(ui)
    db = DebugMode(ui)
    
    MainWindow.show()
    sys.exit(app.exec_())

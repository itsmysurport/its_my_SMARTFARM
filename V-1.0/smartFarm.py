from smartFarm_gui import *
from HandlingEvent import *

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    HandleEvent = HandleEvent(ui)

    MainWindow.show()
    sys.exit(app.exec_())

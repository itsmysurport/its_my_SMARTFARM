from graph_gui import *
from PyQt5 import *
import pyqtgraph as pg
import random
import time
a = [30,21,10,5,7,8]

def plotting(self):
    data = random.randrange(0,31)
    self.a.append(data)
    self.graphicsView.clear()
    self.graphicsView.plot(a, pen = pg.mkPen(color=(255, 100, 25)))

def update(self):
    while True:
        if input() == 'a':
            self.plotting()
            print('DRAW GRAPH')

Ui_MainWindow.plotting = plotting
Ui_MainWindow.update = update
Ui_MainWindow.a = a

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.update()
    sys.exit(app.exec_())

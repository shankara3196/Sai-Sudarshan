

import sys
from PyQt4 import QtGui, QtCore

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("oil reserve estimator")
        self.setWindowIcon(QtGui.QIcon('pythonlogo.png'))
        self.home()

    def home(self):
        btn = QtGui.QPushButton("Quit", self)

        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(10,10)
       
        btn = QtGui.QPushButton("clear", self)

        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(40,40)

        btn = QtGui.QPushButton("estimate", self)

        btn.clicked.connect(self.close_application)
        btn.resize(btn.minimumSizeHint())
        btn.move(70,70)

       
        self.show()

    def close_application(self):
        sys.exit()
         
    
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


run()

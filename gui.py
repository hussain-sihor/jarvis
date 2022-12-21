from jarvis_ui import Ui_jarvisUi
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer ,  QTime, QDate
from PyQt5.uic import loadUiType
import main
import sys
class MainThread(QThread):

 def __init__(self):

        super(MainThread,self).__init__()

 def run(self): 

    main.Task_Gui()

startExe = MainThread()

class  Gui_Start(QMainWindow) :

     def __init__(self) :

        super().__init__()

        self.gui = Ui_jarvisUi()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)
        
     def startTask(self) :

        self.gui.label1 = QtGui.QMovie("..//..//Downloads//Q8i2.gif")
        self.gui.gif_left.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2 = QtGui.QMovie("..//..//Downloads//XjB8.gif")
        self.gui.gif_right.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3 = QtGui.QMovie("..//..//Downloads//VJl.gif")
        self.gui.label_2.setMovie(self.gui.label3)
        self.gui.label3.start()
        
        startExe.start()


GuiApp = QApplication(sys.argv)    
jarvis_gui = Gui_Start()
jarvis_gui.show()    
exit(GuiApp.exec_())

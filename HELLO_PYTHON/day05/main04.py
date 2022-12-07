import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main04.ui")[0]

class WindowClass(QMainWindow, from_class): 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
       
    #pb버튼이 눌리면 작동할 함수
    def myclick(self):
        a = self.leMine.text()
        
        b = random.random()
        print(b)
        com = ""
        
        if b >= 0.5 :
            com = "홀"
            self.leCom.setText(str(com))
        else:
            com ="짝"
            self.leCom.setText(str(com))
        
        result = ""
        if com == a:
            self.leResult.setText("이김")
        else:
            self.leResult.setText("짐")
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
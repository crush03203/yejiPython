import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

from_class = uic.loadUiType("main07.ui")[0]

class WindowClass(QMainWindow, from_class): 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
        self.le_Mine.returnPressed.connect(self.myclick)
       
    #pb버튼이 눌리면 작동할 함수
    def myclick(self):
        a = self.le_Mine.text()
        print(a)
        b = random.random()
        com = ""
        
        if b > 0.66 :
            com = "가위"
        elif b > 0.33 : 
            com = "바위"
        else:
            com = "보"
        self.le_Com.setText(com)
        
        result = ""
        if a == "주먹" and com =="가위" or a == "가위" and com =="보" or a == "보" and com =="주먹" :
            result = "이김"
        elif a == com :
            result = "비김"
        else :
            result = "짐" 
            
        self.le_Result.setText(result)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
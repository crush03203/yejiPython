import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random

from_class = uic.loadUiType("main06.ui")[0]

class WindowClass(QMainWindow, from_class): 
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.myclick)
       
    #pb버튼이 눌리면 작동할 함수
    def myclick(self):
        dan = self.le.text()
        idan = int(dan)
        txt = ""
        txt += f"{idan}*{1}={idan*1}\n"
        txt += f"{idan}*{2}={idan*2}\n"
        txt += f"{idan}*{3}={idan*3}\n"
        txt += f"{idan}*{4}={idan*4}\n"
        txt += f"{idan}*{5}={idan*5}\n"
        txt += f"{idan}*{6}={idan*6}\n"
        txt += f"{idan}*{7}={idan*7}\n"
        txt += f"{idan}*{8}={idan*8}\n"
        txt += f"{idan}*{9}={idan*9}\n"
        
        self.te.setText(txt)
       
       
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
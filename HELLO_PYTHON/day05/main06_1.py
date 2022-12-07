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
        txt = self.le.text()
        num = int(txt)
        form = ""
        for i in range(1,10):
            form += "%d * %d  = %d\n" %(num, i, num*i)

        
        self.te.setPlainText(form)
       
       
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
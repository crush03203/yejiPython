import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic
from random import random

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("main0X.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
        self.pb.clicked.connect(self.pbFunction)
        self.setComRandom()
    
    def setComRandom (self):
        arr9 = [ 1,2,3,4,5,6,7,8,9]
        print(arr9)
        for i in random.randrange(arr9):
            rnd = (int)(random.random()*9)

            a= arr9[0]
            b= arr9[rnd]
            arr9[0]=b
            arr9[rnd]=a


        
        com = arr9[0]+""+arr9[1]+""+arr9[2];
        print(com)
        
        
    #pb가 눌리면 작동할 함수
    def pbFunction(self) :
        self.lbl.setText("Good Evening")
        



if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
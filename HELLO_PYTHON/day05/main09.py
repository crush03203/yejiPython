import sys
from PyQt5.QtWidgets import*
from PyQt5 import uic
from skimage.filters._window import window

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("main09.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        #버튼에 기능을 연결하는 코드
        self.pb1.clicked.connect(self.myclick)
        self.pb2.clicked.connect(self.myclick)
        self.pb3.clicked.connect(self.myclick)
        self.pb4.clicked.connect(self.myclick)
        self.pb5.clicked.connect(self.myclick)
      
        self.pb6.clicked.connect(self.myclick)
        self.pb7.clicked.connect(self.myclick)
        self.pb8.clicked.connect(self.myclick)
        self.pb9.clicked.connect(self.myclick)
        self.pb0.clicked.connect(self.myclick)
        
        self.pbCall.clicked.connect(self.myCall)
        
    #pb가 눌리면 작동할 함수
    def myCall(self):
        str_tel = self.le.text()
        QMessageBox.question(None, "calling", str_tel, QMessageBox.Yes,QMessageBox.NoButton)
    
    def myclick(self) : 
        str_new = self.sender().text()
        str_old = self.le.text()
        
        self.le.setText(str_old+str_new)
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
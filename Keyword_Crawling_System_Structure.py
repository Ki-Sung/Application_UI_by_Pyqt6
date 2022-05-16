# 광고 Keyword Crawling System UI 구조

# 0. 필요한 패키지 모듈 import
import time  # 시간데이터를 다루기 위한 time 모듈 
from datetime import timedelta # 기간을 표현하기 위한 모듈 
from datetime import datetime  # 날짜와 시간을 동시에 표현하기 위한 모듈  

import random  # random 모듈 
import pandas as pd  # 판다스 모듈

from bs4 import BeautifulSoup   # BeautifulSoup 모듈 
from selenium import webdriver  # chromedriver 모듈
from webdriver_manager.chrome import ChromeDriverManager  # chromedirve manager 모듈 

import sys  # 인터프리터 제어 모듈 
import os   # 운영체제와의 상호작용을 돕는 모듈 
import re   # 정규식 연산을 위한 모듈 
import subprocess  # 프로세서의 입/출력 및 에러 결과에 대한 리턴값을 제어할 수 있는 모듈 
from tqdm import tqdm  # progressbar를 나타내는 모듈 
from PyQt6 import QtCore, QtGui, QtWidgets  # PyQt6 모듈 선언 
from PyQt6.QtWidgets import *  # PyQt6 위젯 중 모든 위젯 모듈 불러오기 
from PyQt6.QtGui import *      # PyQt6 GUI 중 모든 Gui 모듈 불러오기
from PySide6.QtGui import *    # PySide6 Gui 중 모든 모듈 불러오기 
from PyQt6.QtCore import QBasicTimer, QRect  # PyQt6에서 시간 체크를 위한 모듈

# 경고 표시 무시 
import warnings 
warnings.simplefilter("ignore")

# UI 윈도우 class 선언 - progressbarApp
class crawlingApp(QWidget):    # progressbarApp 클래스를 만드는데 QWidget 클래스를 상속 받음. 
    def __init__(self):           # 파이썬의 생성자명은 __init__ 고정, 첫 번째 고정값은 self로 들어가야 함
        super().__init__()        # Widget 클래스의 초기화 메서드 호출 - progressbarApp 클래스의 init 함수 실행시, 상위 클래스인 QWidget의 init도 실행.
        self.initUI()      # UI 설정 매서드 initUI 선언 
        
        
    def initUI(self):
        # window 타이틀 및  크기 조절
        self.setWindowTitle('Keyword Crawling System')  # UI title 설정
        self.setGeometry(610,500,600,300)       # UI 전체 크기 설정 - (창 위치 w, 창 위치 h, 창 크기 w, 창 크기 h)
        
        # Attention 문구 
        self.label1 = QLabel('Attention: 크롤링시 keyword 수는 2,000개 이하로 작업하실 것을 권장 드립니다.', self)  # 첫 번째 라벨 설정 
        self.label1.move(85,35)   # 첫 번째 라벨 위치 설정 
        
        # 엑셀파일 oepn 버튼 
        self.df = []   # 데이터 지정을 위한 리스트 지정 
        self.btn1 = QPushButton("File Open", self)  # File Open 버튼 지정
        self.btn1.setGeometry(110,150,150,55)     # File Open 버튼 크기 및 위치 설정 - (버튼 위치 w, 버튼 위치 h, 버튼 크기 w, 버튼 크기 h)
        self.btn1.clicked.connect(self.pushButtonClicked)  # 버튼 클릭시 event 지정 - 'pushButtonClicked' 매서드와 연결
        self.label2 = QLabel()  # 두 번쨰 라벨 
        
        # 크롤링 버튼 
        self.btn2 = QPushButton('Push Crawling Button', self)  # Push Crawling Button 버튼 지덩 
        self.btn2.setGeometry(340,150,150,55)                  # Push Crawling Button 버튼 위치 및 크기 설정 - (버튼 위치 w, 버튼 위치 h, 버튼 크기 w, 버튼 크기 h)
        self.btn2.clicked.connect(self.btnClicked)      # 버튼 클릭시 event 지정  - 'btnClicked' 매서드와 연결 
        
        # 라이센스 명 
        self.label3 = QLabel('Copyright ⓒ A1 Performance Factory Crawling System v.220509', self)  # UI 라벨 설정 - 라이센스 명 
        self.label3.move(110,250)   # UI 라벨 위치 (w, h) 
    
    # File Open event 메서드 
    def pushButtonClicked(self):
        fileNameTuple = QFileDialog.getOpenFileName(self, 'OpenFile',"", "Excel (*.xls *.xlsx)")  # 엑셀파일 오픈 
        fileName = fileNameTuple[0]        # 오픈한 엑셀파일 변수 지정 
        self.df = pd.read_excel(fileName)  # 엑셀파일 읽기 
        
    # 버튼 클릭 event 메서드 
    def btnClicked(self):     
        self.clickme()   # 버튼 숨기기 Event 메서드 받기
        self.button_clicked()   # 맨 아래 button_clicked 메서드 클릭시  
        self.close()            # 창 UI 창 닫기 
            
    # 버튼 숨기기 메서드         
    def clickme(self):  
        self.label1.hide()  # Attention 문구 숨기기 
        self.btn1.hide()    # 벼튼1 숨기기
        self.btn2.hide()    # 버튼2 숨기기 
        
        # 크롤링 코드 
        # keyword data load
        data = self.df  # 위 리스트 받기  - 엑셀파일을 열기 위한 
        
        #============================
        # 크롤링 코드 입력란 
        #============================
        
    # Messagebox로 작업 마침 알림 메서드 
    def button_clicked(self):   
        self.dlg = QMessageBox()           # QMessageBox 생성 
        self.dlg.setWindowTitle("We are Done!!")     # QMessageBox Window title 설정 
        self.dlg.setText("정기빈 구독과 좋아요 부탁드립니다 :)")  # QMessageBox 내 텍스트 설정 
        self.dlg.setStandardButtons(QMessageBox.StandardButton.Yes)  # QMessageBox 내 버튼 설정 
        self.button = self.dlg.exec()    # QMessageBox yes 버튼을 누르면 종료 
        
        if self.button == QMessageBox.StandardButton.Yes:   # 버튼을 누름면 실행 콘솔에 Done! 표시 
            print("Done!")


# 4. 설계한 UI 실행 및 종료          
if __name__ == '__main__':        # py 파일은 하나의 모듈형태로 만들어지기 때문에 누가 임포트하냐에 따라 __name__ 값이 달라짐 -> 쟈기가 직접 실행해야 함 
    
    app = QApplication(sys.argv)  # PyQt 어플리케이션 객체 생성 
    
    ex = crawlingApp()            # 생성자의 self는 progressbarApp을 전달받아 객체를 실행함 
    
    ex.show()                     # 실행한 객체 구현
    
    sys.exit(app.exec())         # app객체를 실행시키고, system의 x버튼을 누르면 실행되고 있는 App을 종료 
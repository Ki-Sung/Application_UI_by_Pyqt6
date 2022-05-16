# Crawling UI System - Beta version 

# 0. 필요한 패키지 모듈 import
import time  # 시간데이터를 다루기 위한 time 모듈 
from datetime import timedelta # 기간을 표현하기 위한 모듈 
from datetime import datetime  # 날짜와 시간을 동시에 표현하기 위한 모듈  

import random  # random 모듈 
import pandas as pd  # 판다스 모듈

from bs4 import BeautifulSoup   # BeautifulSoup 모듈 
from selenium import webdriver  # chromedriver 모듈
from webdriver_manager.chrome import ChromeDriverManager  # chromedirve manager 모듈 

import sys   # 인터프리터 제어 모듈 
from PyQt6.QtWidgets import *  # PyQt6 위젯중 모든 위젯 모듈 불러오기 
from PyQt6.QtCore import QBasicTimer  # PyQt6에서 시간 체크를 위한 모듈

# 경고 표시 무시 
import warnings 
warnings.simplefilter("ignore")

# 1. Pyqt6를 이용하여 UI 설정 

# UI 윈도우 class 선언 - progressbarApp
class progressbarApp(QWidget):    # progressbarApp 클래스를 만드는데 QWidget 클래스를 상속 받음. 
    def __init__(self):           # 파이썬의 생성자명은 __init__ 고정, 첫 번째 고정값은 self로 들어가야 함
        super().__init__()        # Widget 클래스의 초기화 메서드 호출 - progressbarApp 클래스의 init 함수 실행시, 상위 클래스인 QWidget의 init도 실행.
        self.initUI()     # UI 설정 매서드 initUI 선언 

    # UI 설정 메서드     
    def initUI(self):  
        self.btn = QPushButton('Push Crawling Button', self)  # button 생성 - 버튼명 'Push Crawling Button'
        self.btn.setGeometry(200,150,200,40)                  # 버튼 크기 설정 - (버튼 위치 w, 버튼 위치 h, 버튼 크기 w, 버튼 크기 h)
        self.btn.move(150,100)                                # 버튼 위치 설정 
        self.progressbar = QProgressBar(self)          # progressbar 생성 
        self.progressbar.setGeometry(50,60,400,25)     # Progressbar 크기 설정 - (바 위치 w, 바 위치 h, 바 크기 w, 바 크기 h)
        self.btn.clicked.connect(self.btnClicked)      # 버튼 클릭시 이벤트 설정  - 아래에 생성된 'btnClicked'를 받음 
        self.timer = QBasicTimer()              # UI 타이머 설정 
        self.step = 0                           # progressbar envent를 위한 숫자 설정 
        self.setWindowTitle('Crawling System')  # UI title 설정
        self.setGeometry(600,500,500,200)       # UI 전체 크기 설정 - (창 위치 w, 창 위치 h, 창 크기 w, 창 크기 h)
        self.label2 = QLabel('Copyright ⓒ A1 Performance Factory Crawling System beta ver.', self)  # UI 라벨 설정 - 라이센스 명 
        self.label2.move(55,170)   # UI 라벨 위치 (w, h) 
        self.show()     # UI 나타내기 

    # progressbar event 메서드 
    def timerEvent(self, e):    
        if self.step >= 100:        # 만약 step(숫자 설정)이 100보다 크거가 같으면 
            self.timer.stop()       # 시간 Stop 
            self.button_clicked()   # 맨 아래 button_clicked 메서드 클릭시  
            self.close()            # 창 UI 창 닫기 
            return          # event 설정 반환 
        self.step = self.step + 1   # progressbar 숫자 1씩 증가 
        self.progressbar.setValue(self.step)  # progressbar로 셋팅될 값 

    # 버튼 클릭 event 메서드 
    def btnClicked(self):     
        if self.timer.isActive():    # QBasicTimer가 작동중인지 체크 
            self.timer.stop()        # 만약 QBasicTimer 중지 되면 
            self.setText('Crawling..')  # 'Crawling'이라는 문구 출력 
        else:
            self.timer.start(100, self)   # 그외  QBasicTimer가 작동되면 
            self.clickme()           # Buttonbox를 숨기고 
            self.btn.setText('Saving to Excel Files')  # 'Saving to Excel Files'라는 문구 출력 
            self.label3 = QLabel('We are Done!', self)
            self.label3.move(55,150)
            
    # 버튼 숨기기 메서드         
    def clickme(self):   
        self.btn.hide()   # 버튼 숨기기 
        
        #=============================
        # 여기서부터 크롤링 코드 입력  
        # 꼭 함수 안에 작성해야함 
        #=============================
            
    # Messagebox로 작업 마침 알림 메서드 
    def button_clicked(self):   
        self.dlg = QMessageBox()         # QMessageBox 생성 
        self.dlg.setWindowTitle("Crawling System")   # QMessageBox Window title 설정 
        self.dlg.setText("Thank you! We are done!")  # QMessageBox 내 텍스트 설정 
        self.dlg.setStandardButtons(QMessageBox.StandardButton.Yes)  # QMessageBox 내 버튼 설정 
        self.button = self.dlg.exec()    # QMessageBox yes 버튼을 누르면 종료 

        if self.button == QMessageBox.StandardButton.Yes:  # 버튼을 누름면 실행 콘솔에 Done! 표시 
            print("Done!")


# 4. 설계한 UI 실행 및 종료          
if __name__ == '__main__':       # py 파일은 하나의 모듈형태로 만들어지기 때문에 누가 임포트하냐에 따라 __name__ 값이 달라짐 -> 쟈기가 직접 실행해야 함 
    app = QApplication(sys.argv) # PyQt 어플리케이션 객체 생성 
    
    ex = progressbarApp()        # 생성자의 self는 progressbarApp을 전달받아 객체를 실행함 
    
    sys.exit(app.exec())         # app객체를 실행시키고, system의 x버튼을 누르면 실행되고 있는 App을 종료 
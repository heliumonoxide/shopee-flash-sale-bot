from PyQt5 import QtCore, QtGui, QtWidgets
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pause
from datetime import datetime
import time
import json
import os
from functools import reduce
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import numpy as np
from backend import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 960)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 960))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 960))
        MainWindow.setSizeIncrement(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
        "background-color: #FF7A00;\n"
        "}")
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setAnimated(True)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(620, 750, 461, 71))
        self.startButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.startButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startButton.setAutoFillBackground(False)
        self.startButton.setStyleSheet("color: #FF7A00;")
        self.startButton.setIconSize(QtCore.QSize(20, 20))
        self.startButton.setCheckable(False)
        self.startButton.clicked.connect(self.start_clicked)
        self.startButton.setObjectName("startButton")


        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(620, 840, 461, 71))
        self.exitButton.setSizeIncrement(QtCore.QSize(0, 0))
        self.exitButton.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.exitButton.setAutoFillBackground(False)
        self.exitButton.setStyleSheet("color: #FF7A00;")
        self.exitButton.setIconSize(QtCore.QSize(20, 20))
        self.exitButton.setCheckable(False)
        self.exitButton.clicked.connect(lambda:sys.exit())
        self.exitButton.setObjectName("exitButton")


        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(530, 50, 541, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.judul.setFont(font)
        self.judul.setStyleSheet("color: white;")
        self.judul.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.judul.setObjectName("judul")


        self.human = QtWidgets.QLabel(self.centralwidget)
        self.human.setGeometry(QtCore.QRect(90, 20, 521, 621))
        self.human.setText("")
        self.human.setPixmap(QtGui.QPixmap(":/images/Group 69.png"))
        self.human.setObjectName("human")


        self.email = QtWidgets.QLabel(self.centralwidget)
        self.email.setGeometry(QtCore.QRect(440, 260, 421, 56))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.email.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.email.setStyleSheet("color: white;")
        self.email.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.email.setIndent(90)
        self.email.setObjectName("email")


        self.dateTimeInput = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeInput.setGeometry(QtCore.QRect(190, 680, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        self.dateTimeInput.setFont(font)
        self.dateTimeInput.setObjectName("dateTimeInput")


        self.shopeePayButton = QtWidgets.QRadioButton(self.centralwidget)
        self.shopeePayButton.setGeometry(QtCore.QRect(190, 830, 141, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.shopeePayButton.setFont(font)
        self.shopeePayButton.setStyleSheet("color:white;")
        self.shopeePayButton.setText("ShopeePay")
        self.shopeePayButton.setObjectName("shopeePayButton")


        self.mandiriButton = QtWidgets.QRadioButton(self.centralwidget)
        self.mandiriButton.setGeometry(QtCore.QRect(190, 790, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.mandiriButton.setFont(font)
        self.mandiriButton.setText("Mandiri")
        self.mandiriButton.setStyleSheet("color:white;")
        self.mandiriButton.setObjectName("mandiriButton")


        self.input_email = QtWidgets.QTextEdit(self.centralwidget)
        self.input_email.setGeometry(QtCore.QRect(530, 310, 374, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_email.sizePolicy().hasHeightForWidth())
        self.input_email.setSizePolicy(sizePolicy)
        self.input_email.setMaximumSize(QtCore.QSize(2000, 40))
        self.input_email.setBaseSize(QtCore.QSize(13, 11))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        self.input_email.setFont(font)
        self.input_email.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.input_email.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input_email.setLineWidth(2)
        self.input_email.setMidLineWidth(2)
        self.input_email.setObjectName("input_email")


        self.judul2 = QtWidgets.QLabel(self.centralwidget)
        self.judul2.setGeometry(QtCore.QRect(530, 110, 650, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.judul2.setFont(font)
        self.judul2.setStyleSheet("color: white;")
        self.judul2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.judul2.setObjectName("judul2")


        self.judul3 = QtWidgets.QLabel(self.centralwidget)
        self.judul3.setGeometry(QtCore.QRect(530, 180, 571, 81))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.judul3.setFont(font)
        self.judul3.setStyleSheet("color: white;")
        self.judul3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.judul3.setObjectName("judul3")


        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(440, 350, 421, 56))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.password.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.password.setStyleSheet("color: white;")
        self.password.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.password.setIndent(90)
        self.password.setObjectName("password")


        self.input_password = QtWidgets.QLineEdit(self.centralwidget)
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setGeometry(QtCore.QRect(530, 400, 374, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_password.sizePolicy().hasHeightForWidth())
        self.input_password.setSizePolicy(sizePolicy)
        self.input_password.setMaximumSize(QtCore.QSize(2000, 40))
        self.input_password.setBaseSize(QtCore.QSize(13, 11))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        self.input_password.setFont(font)
        self.input_password.setObjectName("input_password")


        self.shopee_link = QtWidgets.QLabel(self.centralwidget)
        self.shopee_link.setGeometry(QtCore.QRect(540, 620, 451, 56))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.shopee_link.setFont(font)
        self.shopee_link.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.shopee_link.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.shopee_link.setStyleSheet("color: white;")
        self.shopee_link.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.shopee_link.setIndent(90)
        self.shopee_link.setObjectName("shopee_link")


        self.date_time = QtWidgets.QLabel(self.centralwidget)
        self.date_time.setGeometry(QtCore.QRect(100, 620, 511, 56))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.date_time.setFont(font)
        self.date_time.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.date_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.date_time.setStyleSheet("color: white;")
        self.date_time.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.date_time.setIndent(90)
        self.date_time.setObjectName("date_time")


        self.input_link = QtWidgets.QTextEdit(self.centralwidget)
        self.input_link.setGeometry(QtCore.QRect(630, 680, 374, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_link.sizePolicy().hasHeightForWidth())
        self.input_link.setSizePolicy(sizePolicy)
        self.input_link.setMaximumSize(QtCore.QSize(2000, 40))
        self.input_link.setBaseSize(QtCore.QSize(13, 11))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        self.input_link.setFont(font)
        self.input_link.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.input_link.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input_link.setLineWidth(2)
        self.input_link.setMidLineWidth(2)
        self.input_link.setObjectName("input_link")


        self.methods = QtWidgets.QLabel(self.centralwidget)
        self.methods.setGeometry(QtCore.QRect(100, 730, 451, 56))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.methods.setFont(font)
        self.methods.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.methods.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.methods.setStyleSheet("color: white;")
        self.methods.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.methods.setIndent(90)
        self.methods.setObjectName("methods")


        self.pathFeatures = QtWidgets.QLabel(self.centralwidget)
        self.pathFeatures.setGeometry(QtCore.QRect(440, 450, 681, 56))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pathFeatures.setFont(font)
        self.pathFeatures.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pathFeatures.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pathFeatures.setStyleSheet("color: white;")
        self.pathFeatures.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pathFeatures.setIndent(90)
        self.pathFeatures.setObjectName("pathFeatures")


        self.input_pilihan = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_pilihan.setGeometry(QtCore.QRect(530, 500, 501, 91))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(9)
        self.input_pilihan.setFont(font)
        self.input_pilihan.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.input_pilihan.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input_pilihan.setLineWidth(2)
        self.input_pilihan.setMidLineWidth(2)
        self.input_pilihan.setObjectName("input_pilihan")


        self.BCAButton = QtWidgets.QRadioButton(self.centralwidget)
        self.BCAButton.setGeometry(QtCore.QRect(380, 790, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BCAButton.setFont(font)
        self.BCAButton.setText("BCA")
        self.BCAButton.setStyleSheet("color:white;")
        self.BCAButton.setObjectName("BCAButton")


        self.BNIButton = QtWidgets.QRadioButton(self.centralwidget)
        self.BNIButton.setGeometry(QtCore.QRect(380, 830, 191, 30))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.BNIButton.setFont(font)
        self.BNIButton.setText("BNI")
        self.BNIButton.setStyleSheet("color:white;")
        self.BNIButton.setObjectName("BNIButton")


        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(100, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon(':/icons/canva_pro.png'))
        MainWindow.setWindowTitle(_translate("MainWindow", "Shopee catalogue automator"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
        self.judul.setText(_translate("MainWindow", "WELCOME TO"))
        self.email.setText(_translate("MainWindow", "Email"))
        self.shopeePayButton.setText(_translate("MainWindow", "ShopeePay"))
        self.human.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/images/Group 69.png\"/></p></body></html>"))
        self.mandiriButton.setText(_translate("MainWindow", "Mandiri"))
        self.judul2.setText(_translate("MainWindow", "SHOPEE CATALOGUE"))
        self.judul3.setText(_translate("MainWindow", "AUTOMATOR"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.shopee_link.setText(_translate("MainWindow", "Paste Shopee link below!"))
        self.date_time.setText(_translate("MainWindow", "Input designated time below!"))
        self.methods.setText(_translate("MainWindow", "Payment Methods"))
        self.pathFeatures.setText(_translate("MainWindow", "Pilihan (use \",\" to split between menus)"))
        self.BCAButton.setText(_translate("MainWindow", "BCA"))
        self.BNIButton.setText(_translate("MainWindow", "BNI"))

    def start_clicked(self):
        email = str(self.input_email.toPlainText())
        password = str(self.input_password.text())
        link = str(self.input_link.toPlainText())
        pathFeatures = str(self.input_pilihan.toPlainText())
        pathFeatures = np.array(pathFeatures.split(','))
        dateTime = str(self.dateTimeInput.dateTime().toString('yyyy,M,d,h,m'))
        dateTime = np.array(dateTime.split(',')).astype(np.int)
        year  = dateTime[0]
        month  = dateTime[1]
        day   = dateTime[2]
        hour  = dateTime[3]
        minute = dateTime[4]
        
        if self.shopeePayButton.isChecked():
            metodebayar = 'ShopeePay'

        if self.mandiriButton.isChecked():
            metodebayar = 'Bank Mandiri'

        if self.BCAButton.isChecked():
            metodebayar = 'Bank BCA'
        
        if self.BNIButton.isChecked():
            metodebayar = 'Bank BNI'

        bayarvia = metodebayar

        metodePembayaranBank = "//div[contains(text(),'" + str(bayarvia) + "')]"

        driver = webdriver.Chrome(ChromeDriverManager().install())

        # Force Login
        driver.get(str(link))

        # Click Login
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Log In']")))
        driver.find_element(By.XPATH, "//a[normalize-space()='Log In']").click()
        # Login
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='No. Handphone/Username/Email']")))
        driver.find_element(By.XPATH, "//input[@placeholder='No. Handphone/Username/Email']").send_keys(email)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(Keys.RETURN)

        pause.until(datetime(year, month, day, hour, minute))
        time.sleep(1.5)

        print('1')
        # Click Buy and Features
        WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='beli sekarang']")))
        print('2')
        print(len(pathFeatures))
        for i in range(len(pathFeatures)):
            if pathFeatures[0] != '':
                driver.find_element(By.XPATH, "(//button[normalize-space()='" + pathFeatures[i] + "'])[1]").click()
                print('None is counted')
        print('3')
        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='beli sekarang']")))
        print('4')
        driver.find_element(By.XPATH, "//button[normalize-space()='beli sekarang']").click()
        print('5')
        #Checkout
        WebDriverWait(driver, 40).until(EC.presence_of_element_located(
            (By.XPATH, "//span[@class='kcsswk']")))
        driver.find_element(By.XPATH,
                            "//span[@class='kcsswk']").click()

        #Customize metode pembayaran

        if bayarvia == 'Bank BCA' or 'Bank BNI' or 'Bank Mandiri':
            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//button[normalize-space()='Transfer Bank']")))
            driver.find_element(By.XPATH,
                                "//button[normalize-space()='Transfer Bank']").click()
            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                            str(metodePembayaranBank))))
            driver.find_element(By.XPATH,
                                metodePembayaranBank).click()
            time.sleep(1.5)
            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//button[normalize-space()='Buat Pesanan']")))
            driver.find_element(By.XPATH,"//button[normalize-space()='Buat Pesanan']").click()
            print("Transfer Bank " + bayarvia + " Success")

        if bayarvia == 'ShopeePay':
            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                            "(//span[contains(text(),'ShopeePay')])[1]")))
            driver.find_element(By.XPATH,
                                "(//span[contains(text(),'ShopeePay')])[1]").click()
            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//button[normalize-space()='Buat Pesanan']")))
            driver.find_element(By.XPATH,
                                "//button[normalize-space()='Buat Pesanan']").click()
            time.sleep(1.5)
            WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.XPATH,
                                                                            "//div[@id='pay-button']")))
            driver.find_element(By.XPATH,"//div[@id='pay-button']").click()
            print("ShopeePay Success")

        time.sleep(10)
            
import satir_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
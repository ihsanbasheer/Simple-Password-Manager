
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui():
   
    
    def setupUi(self, MainWindow): # UI Setup (QT Elements and their styling)
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 659)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: #1a1a1a; color: white; font-style: bold")
        
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 0, 1021, 601))
        self.stackedWidget.setObjectName("stackedWidget")
        
        self.loginpage = QtWidgets.QWidget()
        self.loginpage.setObjectName("loginpage")
        
        self.userinputlogin = QtWidgets.QLineEdit(self.loginpage)
        self.userinputlogin.setGeometry(QtCore.QRect(340, 190, 331, 51))
        self.userinputlogin.setObjectName("userinputlogin")
        self.userinputlogin.setStyleSheet('font-size: 20px;')
        
        self.passinputlogin = QtWidgets.QLineEdit(self.loginpage)
        self.passinputlogin.setGeometry(QtCore.QRect(340, 290, 331, 51))
        self.passinputlogin.setObjectName("passinputlogin")
        self.passinputlogin.setStyleSheet('font-size: 20px;')
        
        self.loginbutton = QtWidgets.QPushButton(self.loginpage)
        self.loginbutton.setGeometry(QtCore.QRect(450, 390, 101, 31))
        self.loginbutton.setObjectName("loginbutton")
        self.loginbutton.setStyleSheet('''
                                        QPushButton {
                                            background-color: #0b1228;
                                            color: white;
                                            border: 2px solid white;
                                            border-radius: 5px;
                                            padding: 40px 20px;
                                            font-size: 16px;
                                        }
                                        QPushButton:hover {
                                            background-color: #23387b;
                                        }
                                    ''')
        
        self.userlabellogin = QtWidgets.QLabel(self.loginpage)
        self.userlabellogin.setGeometry(QtCore.QRect(230, 210, 101, 16))
        self.userlabellogin.setObjectName("userlabellogin")
        self.userlabellogin.setStyleSheet("QLabel { color: white; font-size: 16px;}")
        
        self.passlabellogin = QtWidgets.QLabel(self.loginpage)
        self.passlabellogin.setGeometry(QtCore.QRect(230, 310, 101, 16))
        self.passlabellogin.setObjectName("passlabellogin")
        self.passlabellogin.setStyleSheet("QLabel { color: white; font-size: 16px;}")
        
        self.loginpagetitle = QtWidgets.QLabel(self.loginpage)
        self.loginpagetitle.setGeometry(QtCore.QRect(440, 80, 131, 61))
        
        font = QtGui.QFont()
        font.setPointSize(26)
        
        self.loginpagetitle.setFont(font)
        self.loginpagetitle.setObjectName("loginpagetitle")
        
        self.stackedWidget.addWidget(self.loginpage)
        
        self.mainpage = QtWidgets.QWidget()
        self.mainpage.setObjectName("mainpage")
        
        self.titlelabel = QtWidgets.QLabel(self.mainpage)
        self.titlelabel.setGeometry(QtCore.QRect(70, 10, 261, 21))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        
        self.titlelabel.setFont(font)
        self.titlelabel.setObjectName("titlelabel")
        self.titlelabel.setStyleSheet("font-family: Tahoma, sans-serif;")
        
        self.tableview = QtWidgets.QTableWidget(self.mainpage)
        self.tableview.setColumnCount(2)
        vertical_header = self.tableview.verticalHeader()
        vertical_header.setStyleSheet("""
                                        background-color: grey;
                                        color: black;
                                        ;
                                        """)
        header = self.tableview.horizontalHeader()
        header.setStyleSheet("background-color:black; color: black;border: 2px solid black")
        header_labels = ["Username", "Password"]
        self.tableview.setHorizontalHeaderLabels(header_labels)
        
        self.tableview.setColumnWidth(0,300)
        self.tableview.setColumnWidth(1,325)
        self.tableview.setGeometry(QtCore.QRect(350, 100, 651, 471))
        self.tableview.setObjectName("tableview")
        self.tableview.setStyleSheet("""
                                    QTableWidget {
                                    background-color: black;
                                    selection-background-color: grey ;
                                    border: 2px solid white;}""")     
        self.tableview.setStyleSheet("""
                                    QTableWidget::item {
                                    border: 1.25px solid white;
                                    padding: 5px;
                                    }""")                    
        self.populate_table()
        
        self.passlabel = QtWidgets.QLabel(self.mainpage)
        self.passlabel.setGeometry(QtCore.QRect(40, 210, 71, 16))
        self.passlabel.setObjectName("passlabel")
        
        self.passinput = QtWidgets.QLineEdit(self.mainpage)
        self.passinput.setGeometry(QtCore.QRect(140, 200, 151, 31))
        self.passinput.setObjectName("passinput")
        
        
        self.userinput = QtWidgets.QLineEdit(self.mainpage)
        self.userinput.setGeometry(QtCore.QRect(140, 150, 151, 31))
        self.userinput.setObjectName("userinput")

        
        self.userlabel = QtWidgets.QLabel(self.mainpage)
        self.userlabel.setGeometry(QtCore.QRect(40, 160, 71, 16))
        self.userlabel.setObjectName("userlabel")
        
        self.addbutton = QtWidgets.QPushButton(self.mainpage)
        self.addbutton.setGeometry(QtCore.QRect(90, 300, 161, 51))
        self.addbutton.setObjectName("addbutton")
        self.addbutton.setStyleSheet('''
                                    QPushButton {
                                        background-color: #0b1228;
                                        color: white;
                                        border: 2px solid white;
                                        border-radius: 5px;
                                        padding: 10px 20px;
                                        font-size: 16px;
                                    }
                                    QPushButton:hover {
                                        background-color: #23387b;
                                    }
                                ''')
        
        self.removebutton = QtWidgets.QPushButton(self.mainpage)
        self.removebutton.setGeometry(QtCore.QRect(90, 370, 161, 51))
        self.removebutton.setObjectName("removebutton")
        self.removebutton.setStyleSheet('''
                                        QPushButton {
                                            background-color: #0b1228;
                                            color: white;
                                            border: 2px solid white;
                                            border-radius: 5px;
                                            padding: 10px 20px;
                                            font-size: 16px;
                                        }
                                        QPushButton:hover {
                                            background-color: #23387b;
                                        }
                                    ''')
        self.updatebutton = QtWidgets.QPushButton(self.mainpage)
        self.updatebutton.setGeometry(QtCore.QRect(90, 440, 161, 51))
        self.updatebutton.setObjectName("updatebutton")
        self.updatebutton.setStyleSheet('''
                                        QPushButton {
                                            background-color: #0b1228;
                                            color: white;
                                            border: 2px solid white;
                                            border-radius: 5px;
                                            padding: 10px 20px;
                                            font-size: 16px;
                                        }
                                        QPushButton:hover {
                                            background-color: #23387b;
                                        }
                                        ''')

        self.REFRESHbutton = QtWidgets.QPushButton(self.mainpage)
        self.REFRESHbutton.setGeometry(QtCore.QRect(900, 60, 101, 31))
        self.REFRESHbutton.setObjectName("REFRESHbutton")
        
        self.tablelabel = QtWidgets.QLabel(self.mainpage)
        self.tablelabel.setGeometry(QtCore.QRect(650, 60, 121, 16))
        self.tablelabel.setObjectName("tablelabel")
        
        self.stackedWidget.addWidget(self.mainpage)
        MainWindow.setCentralWidget(self.centralwidget)
        #self.button_features()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Password Manager"))
        self.loginbutton.setText(_translate("MainWindow", "SUBMIT"))
        self.userlabellogin.setText(_translate("MainWindow", "USERNAME"))
        self.passlabellogin.setText(_translate("MainWindow", "PASSWORD"))
        self.loginpagetitle.setText(_translate("MainWindow", "LOGIN"))
        self.titlelabel.setText(_translate("MainWindow", "PASSWORD MANAGER"))
        self.passlabel.setText(_translate("MainWindow", "PASSWORD"))
        self.removebutton.setText(_translate("MainWindow", "REMOVE"))
        self.userlabel.setText(_translate("MainWindow", "USERNAME"))
        self.addbutton.setText(_translate("MainWindow", "ADD"))
        self.updatebutton.setText(_translate("MainWindow", "UPDATE"))
        self.REFRESHbutton.setText(_translate("MainWindow", "REFRESH"))
        self.tablelabel.setText(_translate("MainWindow", "CREDENTIALS"))    
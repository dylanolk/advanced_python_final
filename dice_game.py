# Created by Brang Main

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton
from PyQt5.QtWidgets import QMenu, QMenuBar, QStatusBar
from PyQt5.QtWidgets import QAction, QFrame, QLineEdit
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import QCoreApplication,QRect, QSize, Qt, QMetaObject



class View_MainWindow(object):    
    def __init__(self):
        super().__init__()
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 714)
        MainWindow.setStyleSheet("font: 8pt \"Arial\";")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_title = QLabel(self.centralwidget)
        self.main_title.setGeometry(QRect(260, 100, 350, 75))
        self.main_title.setMinimumSize(QSize(300, 75))
        self.main_title.setStyleSheet("font: 75 20pt \"Arial\";")
        self.main_title.setAlignment(Qt.AlignCenter)
        self.main_title.setObjectName("main_title")

        self.name_label = QLabel(self.centralwidget)
        self.name_label.setGeometry(QRect(230, 290, 125, 40))
        self.name_label.setStyleSheet("font: 12pt \"Arial\";")
        self.name_label.setObjectName("name_label")

        self.name_field_1 = QTextEdit(self.centralwidget)
        self.name_field_1.setEnabled(True)
        self.name_field_1.setGeometry(QRect(360, 290, 300, 40))
        self.name_field_1.viewport().setProperty("cursor", QCursor(Qt.IBeamCursor))
        self.name_field_1.setAcceptDrops(False)
        self.name_field_1.setAutoFillBackground(False)
        self.name_field_1.setStyleSheet("font: 12pt \"Arial\";")
        self.name_field_1.setInputMethodHints(Qt.ImhNone)
        self.name_field_1.setFrameShape(QFrame.Box)
        self.name_field_1.setMidLineWidth(1)
        self.name_field_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.name_field_1.setLineWrapColumnOrWidth(1)
        self.name_field_1.setObjectName("name_field_1")
        
        self.enter_button = QPushButton(self.centralwidget)
        self.enter_button.setGeometry(QRect(340, 470, 200, 60))

        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("font: 12pt \"Arial\";")
        self.enter_button.setObjectName("enter_button")
       # MainWindow.setCentralWidget(self.centralwidget) # Check back

        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(230, 360, 125, 40))
        self.label.setStyleSheet("font: 75 12pt \"Arial\";")
        self.label.setObjectName("label")

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QRect(360, 360, 300, 40))
        self.textEdit.setStyleSheet("font: 75 12pt \"Arial\";")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 884, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DICE GAME"))
        self.main_title.setText(_translate("MainWindow", "DICE ROLLING GAME"))
        self.name_label.setText(_translate("MainWindow", "PLAYER 1"))
        self.name_field_1.setPlaceholderText(_translate("MainWindow", "TYPE NAME OF PLAYER 1"))
        self.enter_button.setText(_translate("MainWindow", "ENTER"))
        self.label.setText(_translate("MainWindow", "PLAYER 2"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "TYPE NAME OF PLAYER 2"))
        self.enter_button.setText(_translate("MainWindow", "ENTER"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))



def main():
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    view = View_MainWindow()
    view.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

    

if __name__ == '__main__':
    main()






# Created by Brang Main

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMenu
from PyQt5.QtWidgets import QMenuBar
from PyQt5.QtWidgets import QStatusBar
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5 import QtCore, QtGui


class View_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(884, 714)
        MainWindow.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";")

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.main_title = QLabel(self.centralwidget)
        self.main_title.setGeometry(QtCore.QRect(240, 50, 350, 75))
        self.main_title.setMinimumSize(QtCore.QSize(300, 75))
        self.main_title.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.main_title.setAlignment(QtCore.Qt.AlignCenter)
        self.main_title.setObjectName("main_title")

        self.name_label = QLabel(self.centralwidget)
        self.name_label.setGeometry(QtCore.QRect(170, 280, 200, 50))
        self.name_label.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.name_label.setObjectName("name_label")

        self.name_field = QTextEdit(self.centralwidget)
        self.name_field.setEnabled(True)
        self.name_field.setGeometry(QtCore.QRect(360, 290, 300, 35))
        self.name_field.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.name_field.setAcceptDrops(False)
        self.name_field.setAutoFillBackground(False)
        self.name_field.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.name_field.setFrameShape(QFrame.Box) # Check back
        self.name_field.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.name_field.setObjectName("name_field")

        self.enter_button = QPushButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(340, 390, 200, 50))

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.enter_button.setObjectName("enter_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 884, 22))
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.main_title.setText(_translate("MainWindow", "DICE ROLLING GAME"))
        self.name_label.setText(_translate("MainWindow", "ENTER YOUR NAME"))
        self.name_field.setPlaceholderText(_translate("MainWindow", "TYPE YOUR NAME HERE"))
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






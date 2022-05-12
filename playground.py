

# Created by Brang Main

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtWidgets import QWidget, QTextEdit, QPushButton
from PyQt5.QtWidgets import QMenu, QMenuBar, QStatusBar
from PyQt5.QtWidgets import QAction, QFrame, QLineEdit, QDialog
from PyQt5.QtGui import QCursor, QFont
from PyQt5.QtCore import QCoreApplication,QRect, QSize, Qt, QMetaObject


class Playground_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(726, 723)
        self.welcomeLabel = QLabel(Dialog)
        self.welcomeLabel.setGeometry(QRect(110, 40, 491, 51))
        self.welcomeLabel.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.welcomeLabel.setAlignment(Qt.AlignCenter)
        self.welcomeLabel.setObjectName("welcomeLabel")

        self.player_one = QLabel(Dialog)
        self.player_one.setGeometry(QRect(60, 140, 150, 25))
        self.player_one.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.player_one.setObjectName("player_one")

        self.label_2 = QLabel(Dialog)
        self.label_2.setGeometry(QRect(540, 140, 150, 25))
        self.label_2.setStyleSheet("font: 75 11pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setGeometry(QRect(170, 440, 100, 50))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setGeometry(QRect(290, 440, 100, 50))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setGeometry(QRect(410, 440, 100, 50))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setGeometry(QRect(170, 510, 100, 50))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setGeometry(QRect(290, 510, 100, 50))
        self.pushButton_5.setObjectName("pushButton_5")

        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setGeometry(QRect(410, 510, 100, 50))
        self.pushButton_6.setObjectName("pushButton_6")

        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setGeometry(QRect(270, 360, 150, 50))
        self.pushButton_7.setObjectName("pushButton_7")

        self.label = QLabel(Dialog)
        self.label.setGeometry(QRect(60, 200, 55, 16))
        self.label.setObjectName("label")

        self.label_3 = QLabel(Dialog)
        self.label_3.setGeometry(QRect(60, 240, 55, 16))
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel(Dialog)
        self.label_4.setGeometry(QRect(540, 190, 55, 16))
        self.label_4.setObjectName("label_4")

        self.label_5 = QLabel(Dialog)
        self.label_5.setGeometry(QRect(540, 240, 55, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QLabel(Dialog)
        self.label_6.setGeometry(QRect(60, 270, 55, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QLabel(Dialog)
        self.label_7.setGeometry(QRect(540, 270, 55, 16))
        self.label_7.setObjectName("label_7")

        self.retranslateUi(Dialog)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcomeLabel.setText(_translate("Dialog", "WELCOME TO DICE ROLLING GAME"))
        self.player_one.setText(_translate("Dialog", "PLAYER 1"))
        self.label_2.setText(_translate("Dialog", "PLAYER 2"))
        self.pushButton.setText(_translate("Dialog", "DICE 1"))
        self.pushButton_2.setText(_translate("Dialog", "DICE 2"))
        self.pushButton_3.setText(_translate("Dialog", "DICE 3"))
        self.pushButton_4.setText(_translate("Dialog", "DICE 4"))
        self.pushButton_5.setText(_translate("Dialog", "DICE 5"))
        self.pushButton_6.setText(_translate("Dialog", "DICE 6"))
        self.pushButton_7.setText(_translate("Dialog", "ROLL THE DICES"))
        self.label.setText(_translate("Dialog", "# 1"))
        self.label_3.setText(_translate("Dialog", "#5"))
        self.label_4.setText(_translate("Dialog", "# 1"))
        self.label_5.setText(_translate("Dialog", "# 5"))
        self.label_6.setText(_translate("Dialog", "Score"))
        self.label_7.setText(_translate("Dialog", "Score"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Playground_Ui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
import sys
from random import randrange

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class SettingsDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent=parent
        self.setWindowTitle("Settings")
        layout = QFormLayout()

        side_num = QComboBox(self)
        side_num.setEditable(True)
        side_num.setInsertPolicy(False)
        side_num.addItems(["4", "6", "8", "10", "12", "20"])
        side_num.currentTextChanged.connect(self.side_num_change)
        side_num.setCurrentText("6")
        layout.addRow("# of Sides", side_num)
      

        self.setLayout(layout)

    def side_num_change(self, value):
        if (value.isdigit()):
            self.parent.num_sides = int(value)
        


class MainWindow(QMainWindow):
    def __init__(self):
        #initializng window
        super().__init__()
        #settings
        self.num_sides=6


        self.setWindowTitle('Dice Game')
        self.resize(200,100)

        #ininitializing middle layout
        middle_widget = QWidget()
        middle_layout= QVBoxLayout()

        #result
        self.result = QLabel(middle_widget)
        self.result.setFont(QFont('Arial',20))
        middle_layout.addWidget(self.result, alignment= Qt.AlignHCenter)

        #button
        button1= QPushButton(middle_widget)
        button1.setText("Roll Die")
        button1.clicked.connect(self.refresh_die)
        middle_layout.addWidget(button1)
        middle_widget.setLayout(middle_layout)

        #initialize top bar
        top_widget= QWidget()
        top_layout= QHBoxLayout()

        #settings button
        settings_button= QPushButton(top_widget)
        settings_button.setText("Settings")
        settings_button.clicked.connect(self.settings_switch)

        top_layout.addWidget(settings_button, alignment=Qt.AlignRight)
        top_widget.setLayout(top_layout)

        #initialize final layout
        central_widget= QWidget()
        final_layout= QVBoxLayout()
        final_layout.addWidget(top_widget)
        final_layout.addWidget(middle_widget)
        central_widget.setLayout(final_layout)
        self.setCentralWidget(central_widget)

    def refresh_die(self):
        choice = str(randrange(self.num_sides)+1)
        self.result.setText(choice)
    
    def settings_switch(self):
        settings = SettingsDialog(self)
        settings.exec()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

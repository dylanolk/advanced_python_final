import sys
from random import randrange

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt


class SettingsDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        layout = QGridLayout()

        layout.addWidget(QComboBox(self))
        


class MainWindow(QMainWindow):
    def __init__(self):
        #initializng window
        super().__init__()
        self.setWindowTitle('Dice Game')
        self.resize(200,100)

        #ininitializing middle layout
        middle_widget = QWidget()
        middle_layout= QVBoxLayout()

        #result
        self.result = QLabel(middle_widget)
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
        self.result.setText(str(randrange(6)+1))
    
    def settings_switch(self):
        settings = SettingsDialog()
        settings.exec()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

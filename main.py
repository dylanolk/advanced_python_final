import sys
from random import randrange

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QSpacerItem
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *

class Player:
    def __init__(self):
        self.money= 100
        self.isHuman = False
        self.winningNumbers=[]
        self.widget = QWidget()


class HumanPlayer(Player):
    num_of_humans=0
    def __init__(self):
        HumanPlayer.num_of_humans+=1
        super().__init__()
        self.isHuman = True

        layout = QFormLayout()

        #name
        name= QLabel()
        name.setText(f"Human {self.num_of_humans}")
        name.setFont(QFont('Arial',9))
        layout.addWidget(name)

        #money label
        money = QLabel(f"Money:  ${str(self.money)}")
        layout.addWidget(money)

        #bet button
        bet_button= QPushButton()
        bet_button.setText("Place A Bet")
        bet_button.clicked.connect(self.bet_dialog)
        layout.addWidget(bet_button)

        self.widget.setLayout(layout)
    def bet_dialog():
        return

  

class BotPlayer(Player):
    num_of_bots=0
    def __init__(self):
        BotPlayer.num_of_bots+=1
        super().__init__()
        layout = QFormLayout()
        layout.addRow("Money", QLabel(str(self.money)))

        #name
        name= QLabel()
        name.setText(f"Bot {self.num_of_bots}")
        name.setFont(QFont('Arial',9))
        layout.addWidget(name)

        #money label
        money = QLabel(f"Money:  ${str(self.money)}")
        layout.addWidget(money)

        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.widget=main_widget

class SettingsDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent=parent
        self.setWindowTitle("Settings")
        layout = QFormLayout()

        #creating drop down menu
        side_num = QComboBox(self)
        side_num.setEditable(True)
        side_num.setInsertPolicy(False)
        side_num.addItems(["4", "6", "8", "10", "12", "20"])
        side_num.currentTextChanged.connect(self.side_num_change)
        side_num.setCurrentText("6")
        layout.addRow("# of Sides", side_num)

        #creating close button
        close_button=QPushButton(self)
        close_button.setText("Close")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)
      

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
        


        self.allWidgets=[]

        self.setWindowTitle('Dice Game')
        self.resize(400,100)

        #ininitializing main layout
        main_widget = QWidget()
        main_layout= QVBoxLayout()

        #settings button
        settings_button= QPushButton(main_widget)
        settings_button.setText("Settings")
        settings_button.clicked.connect(self.settings_switch)
        main_layout.addWidget(settings_button, alignment=Qt.AlignRight)

        #result
        self.result = QLabel(main_widget)
        self.result.setFont(QFont('Arial',20))
        main_layout.addWidget(self.result, alignment= Qt.AlignHCenter)

        #button
        button1= QPushButton(main_widget)
        button1.setText("Roll Die")
        button1.clicked.connect(self.refresh_die)
        main_layout.addWidget(button1)
        
        main_widget.setLayout(main_layout)

        #initialize human player
        player= HumanPlayer()

        #make bot buttons
        bot_adder=QWidget()
        adder_layout= QFormLayout()

        add_button = QPushButton()
        minus_button = QPushButton()
        add_button.setText("+")
        minus_button.setText("-")
        add_button.clicked.connect(self.add_bot)
        minus_button.clicked.connect(self.minus_bot)

        adder_layout.addWidget(add_button)
        adder_layout.addWidget(minus_button)
        bot_adder.setLayout(adder_layout)

        #initialize final layout
        self.allWidgets.append(player.widget)
        self.allWidgets.append(main_widget)
        self.allWidgets.append(bot_adder)
        self.render()

    def refresh_die(self):
        choice = str(randrange(self.num_sides)+1)
        self.result.setText(choice)
    
    def settings_switch(self):
        settings = SettingsDialog(self)
        settings.exec()

    def add_bot(self):
        newBot = BotPlayer()
        self.allWidgets.insert(len(self.allWidgets)-1,newBot.widget)
        self.render()
    
    def minus_bot(self):
        if(len(self.allWidgets)>3):
            self.allWidgets.pop(len(self.allWidgets)-2)
            self.render()
        
    def render(self):
        final_layout = QHBoxLayout()
        central_widget = QWidget()
        for widget in self.allWidgets:
            final_layout.addWidget(widget, alignment=Qt.AlignHCenter)
        central_widget.setLayout(final_layout)
        self.setCentralWidget(central_widget)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

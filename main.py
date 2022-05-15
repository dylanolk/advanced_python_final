import sys
import random
import re

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtWidgets import QLabel, QPushButton, QComboBox, QSpacerItem, QLineEdit
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout
from PyQt5.QtWidgets import QWidget, QFrame
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from matplotlib.style import available

def generate_random_bet(num_sides):
    temp= list(range(1,num_sides))
    random.shuffle(temp)
    return temp[:random.randrange(1,num_sides)]

class Player:
    def __init__(self):
        self.money= 100
        self.bet = 0
        self.isHuman = False
        self.winningNumbers=[]
        self.widget = QWidget()


class HumanPlayer(Player):
    num_of_humans=0
    def __init__(self,parent):
        HumanPlayer.num_of_humans+=1
        super().__init__()
        self.isHuman = True
        self.parent = parent

        layout = QFormLayout()

        #name
        name= QLabel()
        name.setText(f"Human Player {self.num_of_humans}")
        name.setFont(QFont('Arial',12))
        layout.addWidget(name)

        #money label
        self.money_label = QLabel(f"Account Balance:  ${str(self.money)}")
        layout.addWidget(self.money_label)

        #current bet
        self.bet_label = QLabel(f"Current Bet:  ${str(self.bet)}")
        layout.addWidget(self.bet_label)

        #bet button
        bet_button= QPushButton()
        bet_button.setStyleSheet("background-color: #CA3433")
        bet_button.setText("Place A Bet")
        bet_button.clicked.connect(self.bet_dialog)
        layout.addWidget(bet_button)

        self.widget.setLayout(layout)

    def bet_dialog(self):
        dialog = BetDialog(self)
        dialog.exec()
    
    def make_bet(self, choice, num_sides):
        if int(choice) not in self.winningNumbers:
            self.money-=self.bet
        if int(choice) in self.winningNumbers:
            self.money += int(self.bet * num_sides/len(self.winningNumbers))-self.bet

        self.money_label.setText(f"Account Balance:  ${str(self.money)}")

class BetDialog(QDialog):
    def __init__(self,parent):
        super().__init__()
        self.setWindowTitle("Place your bets!")
        self.parent = parent
        self.setStyleSheet("background-color: #FF66BB6A;")
        left_layout = QVBoxLayout()
        left_layout.addWidget(QLabel("Bet Amount"))

        #bet amount
        bet_amount = QLineEdit()
        bet_amount.textChanged.connect(self.handle_bet_amount)
        left_layout.addWidget(bet_amount)
        self.bet_error = QLabel()
        left_layout.addWidget(self.bet_error)

        #bets
        right_layout = QVBoxLayout()
        right_layout.addWidget(QLabel("Bet on..."))

        #buttons
        evens = QPushButton()
        evens.setStyleSheet("background-color: #CA3433")
        evens.setText("Evens")
        evens.clicked.connect(lambda: self.handle_buttons("evens"))
        right_layout.addWidget(evens)

        odds = QPushButton()
        odds.setStyleSheet("background-color: #CA3433")
        odds.setText("Odds")
        odds.clicked.connect(lambda: self.handle_buttons("odds"))
        right_layout.addWidget(odds)

        random = QPushButton()
        random.setStyleSheet("background-color: #CA3433")
        random.setText("Random")
        random.clicked.connect(lambda: self.handle_buttons("random"))
        right_layout.addWidget(random)

        right_layout.addWidget(QLabel("Custom..."))
        custom = QLineEdit()
        custom.textChanged.connect(self.custom_bet)
        self.custom=custom
        right_layout.addWidget(custom)

        close=QPushButton()
        close.setStyleSheet("background-color: #CA3433")
        close.setText("Close")
        close.clicked.connect(self.close)
        right_layout.addWidget(close,alignment = Qt.AlignRight)

        self.button_error = QLabel()
        right_layout.addWidget(self.button_error)
        
        #finalize
        leftWidget= QWidget()
        rightWidget = QWidget()
        leftWidget.setLayout(left_layout)
        rightWidget.setLayout(right_layout)
        
        final_layout = QHBoxLayout()
        final_layout.addWidget(leftWidget)
        final_layout.addWidget(rightWidget)
        self.setLayout(final_layout)

    def handle_buttons(self, bet):
        if bet == "evens":
            temp = list(range(self.parent.parent.num_sides))
            self.parent.winningNumbers = [i for i in temp if i % 2 == 0]
            self.button_error.setText("Betting on Evens!")
        if bet == "odds":
            temp = list(range(self.parent.parent.num_sides))
            self.parent.winningNumbers = [i for i in temp if i % 2 == 1]
            self.button_error.setText("Betting on Odds!")
        if bet == "random":
            self.parent.winningNumbers = generate_random_bet(self.parent.parent.num_sides)
            self.button_error.setText("Betting randomly! Very bold!")
        self.custom.setText(str(self.parent.winningNumbers)[1:-1])
        self.parent.bet_label.setText(f"Current Bet:  ${str(self.parent.bet)}")
        
    def handle_bet_amount(self, value):
        
        if value.isdigit():
            self.parent.bet= int(value)
            self.bet_error.setText("")
        elif value != "":
            self.bet_error.setText("Bet must be integer!")

        self.parent.bet_label.setText(f"Current Bet:  ${str(self.parent.bet)}")
    
    def custom_bet(self,value):
        r= re.compile("^([0-9]*,\s*)*[0-9]+$")
        
        if r.match(value):
            print(r.match(value))
            temp = value.split(',')
            self.parent.winningNumbers= [int(i) for i in temp]
            self.button_error.setText("Using Custom Bet!")
        else:
           self.button_error.setText("Custom bet must have format 1,2,3,4,5 \n(comma seprated integers)")


class BotPlayer(Player):
    num_of_bots=0
    def __init__(self):
        BotPlayer.num_of_bots+=1
        super().__init__()
        layout = QFormLayout()

        #name
        name= QLabel()
        name.setText(f"Bot {self.num_of_bots}")
        name.setFont(QFont('Arial',12))
        layout.addWidget(name)

        #money label
        self.money_label = QLabel(f"Account Balance:  ${str(self.money)}")
        layout.addWidget(self.money_label)

        #current bet
        self.bet_label = QLabel(f"Current Bet: ${str(self.bet)}")
        layout.addWidget(self.bet_label)

        #check winning numbers button
        self.bet_button = QPushButton()
        self.bet_button.setStyleSheet("background-color: #CA3433")
        self.bet_button.setText("Winning Numbers")
        self.bet_button.clicked.connect(self.numbers_dialog)
        layout.addWidget(self.bet_button)

        main_widget = QWidget()
        main_widget.setLayout(layout)

        self.widget=main_widget
    
    def __del__(self):
        BotPlayer.num_of_bots-=1
    
    def make_bet(self, choice, num_sides):
        self.bet=random.choice(range(100))
        self.bet_label.setText(f"Current Bet: ${str(self.bet)}")
        self.winningNumbers= generate_random_bet(num_sides)

        if int(choice) not in self.winningNumbers:
            self.money -= self.bet
        if int(choice) in self.winningNumbers:
            self.money += int(self.bet * num_sides/len(self.winningNumbers))-self.bet

        self.money_label.setText(f"Account Balance:  ${str(self.money)}")
    
    def numbers_dialog(self):
        dialog = NumbersDialog(self)
        dialog.exec()

class NumbersDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.setStyleSheet("background-color: #FF66BB6A;")
        layout = QHBoxLayout()
        layout.addWidget(QLabel("If the dice has landed on any \nof these numbers, this bot has won"))
        layout.addWidget(QLabel(str(parent.winningNumbers)[1:-1]))
        close = QPushButton()
        close.setText("Close")
        close.clicked.connect(self.close)
        self.setLayout(layout)


class SettingsDialog(QDialog):
    def __init__(self, parent):
        super().__init__()
        self.parent=parent
        self.setWindowTitle("Settings")
        self.setStyleSheet("background-color: #FF66BB6A")
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
        self.bots=[]
        self.humans=[]
        
        self.allWidgets=[]

        self.setWindowTitle('Dice Game')
        self.resize(600, 300)
        self.setStyleSheet("background-color: #005C29;")

        #ininitializing main layout
        main_widget = QWidget()
        main_layout= QVBoxLayout()

        #settings button
        settings_button= QPushButton(main_widget)
        settings_button.setStyleSheet("background-color: #CA3433")
        settings_button.setText("Settings")
        settings_button.clicked.connect(self.settings_switch)
        main_layout.addWidget(settings_button, alignment=Qt.AlignRight)

        #result
        self.result = QLabel(main_widget)
        self.result.setFont(QFont('Arial',20))
        main_layout.addWidget(self.result, alignment= Qt.AlignHCenter)

        #button
        button1= QPushButton(main_widget)
        button1.setStyleSheet("background-color: #CA3433")
        button1.setText("Roll Die")

        button1.clicked.connect(self.refresh_die)
        main_layout.addWidget(button1)
        
        main_widget.setLayout(main_layout)

        self.main_widget=main_widget

        #initialize human player
        player= HumanPlayer(self)
        self.humans.append(player)

        #make bot buttons
        bot_adder=QWidget()
        adder_layout= QFormLayout()

        add_button = QPushButton()
        minus_button = QPushButton()
        add_button.setStyleSheet("background-color: #CA3433")
        add_button.setText("+")
        minus_button.setStyleSheet("background-color: #CA3433")
        minus_button.setText("-")
        add_button.clicked.connect(self.add_bot)
        minus_button.clicked.connect(self.minus_bot)

        adder_layout.addWidget(add_button)
        adder_layout.addWidget(minus_button)
        bot_adder.setLayout(adder_layout)
        self.bot_adder=bot_adder

        #initialize final layout
        self.allWidgets.append(player.widget)
        self.allWidgets.append(main_widget)
        self.allWidgets.append(bot_adder)
        self.render()

    def refresh_die(self):
        choice = str(random.randrange(self.num_sides)+1)
        
        self.result.setText(choice)
        self.deal_with_bets(choice)
    
    def settings_switch(self):
        settings = SettingsDialog(self)
        settings.exec()

    def add_bot(self):
        newBot = BotPlayer()
        self.bots.append(newBot)
        self.allWidgets.insert(len(self.allWidgets)-1,newBot.widget)
        self.render()
    
    def minus_bot(self):
        if(len(self.allWidgets)>3):
            self.bots.pop()
            self.allWidgets.pop(len(self.allWidgets)-2)
            self.render()
        
    def render(self):
        final_layout = QHBoxLayout()
        central_widget = QWidget()
    
        #render humans
        for human in self.humans:
            final_layout.addWidget(human.widget)

        #render central widget
        final_layout.addWidget(self.main_widget)

        #render bots
        for bot in self.bots:
            final_layout.addWidget(bot.widget)

        #render adder module
        final_layout.addWidget(self.bot_adder)

        central_widget.setLayout(final_layout)
        self.setCentralWidget(central_widget)

    def deal_with_bets(self, choice):
        players= self.bots + self.humans
        for player in players: 
            player.make_bet(choice, self.num_sides)
        self.render()


if __name__ == "__main__":
    # print(generate_random_bet(6))
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

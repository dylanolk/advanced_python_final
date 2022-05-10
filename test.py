import sys
from random import randrange

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt



app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Dice Game')
window.resize(200,100)


layout= QVBoxLayout()


def refresh_die():
    result.setText(str(randrange(6)+1))
     
result = QLabel(window)
layout.addWidget(result, alignment= Qt.AlignHCenter)

button1= QPushButton(window)
button1.setText("Roll Die")
button1.clicked.connect(refresh_die)
layout.addWidget(button1)



window.setLayout(layout)
window.show()
sys.exit(app.exec_())

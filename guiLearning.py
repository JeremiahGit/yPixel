from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def window():
    app = QApplication(sys.argv) #system infomation or smth? like OS
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300) #The window's:: xpos, ypos, width, height
    win.setWindowTitle("yPixel - realtime stats tracker") #Set the little title, like the terraira verion of minecraft splash text area!!

    #
    # A label / textbox thingy. Set the Window it appears in
    # Set the text
    # Set the position
    #
    label = QtWidgets.QLabel(win)
    label.setText("WOw! A label!!!")
    label.move(100,100)

    win.show() #Shows the window
    sys.exit(app.exec_()) # Makes the window have a clean exit when the x button is pressed.

window()
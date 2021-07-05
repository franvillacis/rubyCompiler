from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QLineEdit, QPushButton, QTextEdit, \
    QPlainTextEdit, QVBoxLayout
import sys
from parser import *


from pyqt5_plugins.examplebutton import QtWidgets


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("background-color: #212121;")

        self.qline = QPlainTextEdit()
        self.qline.setFixedSize(700,320)
        self.qline.setPlaceholderText("Enter your code here...")
        self.qline.setStyleSheet("border: 3"
                            "px solid gray;outline: none; color: white;")

        self.pybutton = QPushButton(self)
        self.pybutton.resize(100, 32)

        self.pybutton.move(325,330)
        self.pybutton.clicked.connect(self.clickMethod)
        self.pybutton.setStyleSheet('background-color: #9ED36A')
        self.pybutton.setText('Compilar')

        self.qlabel = QLabel(self)
        self.qlabel.setStyleSheet("border: 3"
                            "px solid gray;outline: none; color: white;")
        self.qlabel.move(0,370)
        self.qlabel.resize(700,320)
        self.qlabel.setWordWrap(True);


        self.setWindowTitle("Ruby Compiler")
        self.setFixedSize(700,700)
        self.setCentralWidget(self.qline)


    def return_pressed(self):
        self.centralWidget().setText(self.centralWidget().selectedText()+"\"")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    def clickMethod(self):
        print('Clicked Pyqt button.')
        parser = yacc.yacc()
        code = self.qline.toPlainText()
        resultado = parser.parse(s)
        if resultado is not None:
            self.qlabel.setText(resultado)
        else:
            self.qlabel.setText("Not Ruby languaje")

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()


sys.exit(app.exec_())
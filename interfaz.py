from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QLineEdit, QPushButton, QTextEdit, \
    QPlainTextEdit, QVBoxLayout
import sys
from parser import *


from pyqt5_plugins.examplebutton import QtWidgets

from parser import *
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setStyleSheet("background-color: #212121;")


        self.title= QLabel(self)
        self.title.setText("You can try it entering line by line")
        self.title.resize(300,50)
        self.title.move(10,10)
        self.title.setStyleSheet("color: white;")

        self.file = QLabel(self)
        self.file.setText("Or you can choose a file")
        self.file.resize(300, 50)
        self.file.move(10, 180)
        self.file.setStyleSheet("color: white;")

        self.qline = QPlainTextEdit(self)
        self.qline.setFixedSize(700, 100)
        self.qline.setPlaceholderText("Enter your code here...")
        self.qline.setStyleSheet("border: 3"
                            "px solid gray;outline: none; color: white;")
        self.qline.move(0,50)

        self.compileButton = QPushButton(self)
        self.compileButton.resize(100, 32)

        self.compileButton.move(325, 160)
        self.compileButton.clicked.connect(self.click_compile)
        self.compileButton.setStyleSheet('background-color: #9ED36A')
        self.compileButton.setText('Compile')

        self.fileButton = QPushButton(self)
        self.fileButton.resize(100, 32)
        self.fileButton.move(10, 220)
        self.fileButton.clicked.connect(self.click_file)
        self.fileButton.setStyleSheet('background-color: #9ED36A')
        self.fileButton.setText('Choose file')

        self.qlabel = QPlainTextEdit(self)
        self.qlabel.setStyleSheet("border: 3""px solid gray;outline: none; color: white;")
        self.qlabel.move(0, 370)
        self.qlabel.resize(700, 320)
        self.qlabel.setReadOnly(True)

        self.setWindowTitle("Ruby Compiler")
        self.setFixedSize(700, 700)


    def return_pressed(self):
        self.centralWidget().setText(self.centralWidget().selectedText() + "\"")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)

    def click_compile(self):
        parser = yacc.yacc()
        code = self.qline.toPlainText()
        resultado = parser.parse(code)
        if resultado is not None:
            self.qlabel.clear()
            self.qlabel.insertPlainText(str(resultado))
        else:
            self.qlabel.clear()
            self.qlabel.insertPlainText("Not Ruby languaje")

    def click_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            archivo_prueba = open('test.rb', 'r').read()
            analizador = AnalizadorLexico()
            analizador.build()
            tokns = analizador.tokenizer(archivo_prueba)
            if(len(tokns)>0):
                text = 'Los tokens son validos!' + "\n"
                for token in tokns:
                    text += str(token) + "\n"
                self.qlabel.clear()
                self.qlabel.insertPlainText(text)




if __name__ == '__main__':  #
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

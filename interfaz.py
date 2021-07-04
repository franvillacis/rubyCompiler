from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Proyecto Lenguajes")
window.setFixedWidth(1000)
window.show()

sys.exit(app.exec_())
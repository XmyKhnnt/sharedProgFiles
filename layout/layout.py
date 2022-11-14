import sys

# from PyQt5.QtCore import QT
from PyQt5.QtWidgets import QApplication, QMainWindow
from color import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        widget = Color('red')
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()

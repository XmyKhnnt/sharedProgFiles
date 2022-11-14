

import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout



from PyQt5.QtGui import QIcon




class mainGui(QWidget):

    def __init__(self):
        super().__init__()

        # Set Windows style 
        self.setGeometry(200,200, 400,300)
        self.setWindowTitle("This is my App")
        self.setStyleSheet('background-color:white')
        self.setWindowIcon(QIcon('E:\Programming\WebAutomation Materials\ActualCodes\GUI_PyQt5\PyQt5 Course\icons\Kickstarter.png'))
        # self.setWindowOpacity(0.8) # set Windows opacity

       
        self.vertical_layout = QHBoxLayout()
        self.create_buttons()



    def create_buttons(self):


        button_1 = QPushButton('start', self)
        # button_1.setGeometry(100, 100, 100,50)
        button_1.setStyleSheet('color:pink')
        button_1.setStyleSheet('background-color:pink')
        button_1.clicked.connect(self.clicked_button_1)

        button_2 = QPushButton('start 2', self)
        # button_2.setGeometry(100, 150, 100,50)
        button_2.setStyleSheet('color:pink')
        button_2.setStyleSheet('background-color:pink')
        button_2.clicked.connect(self.clicked_button_2)

        button_3 = QPushButton('start 2', self)
        # button_3.setGeometry(100, 200, 100,50)
        button_3.setStyleSheet('color:pink')
        button_3.setStyleSheet('background-color:pink')
        button_3.clicked.connect(self.clicked_button_3)


        self.vertical_layout.addWidget(button_1)
        self.vertical_layout.addWidget(button_2)
        self.vertical_layout.addWidget(button_3)

    

    def clicked_button_1(self):
        print('Button 1 is clicked')

    def clicked_button_2(self):
        print('Button 2 is clicked')

    def clicked_button_3(self):
        print('Button 3 is clicked')
        
        






app = QApplication(sys.argv)
window = mainGui()
window.show()

# Main event loop
sys.exit(app.exec_())

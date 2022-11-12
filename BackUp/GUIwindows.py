#import abs_move 
#import rel_move 
#import where


import sys
#from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QTextEdit
from PyQt5.QtWidgets import *

class ExampleWidget(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    
        
        
    def initUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('sample')

        # buttonの設定
        self.button = QPushButton('Clear!!')
        self.label = QLabel('connected')
        #text
        self.textBox_p0 = QLineEdit()
        self.textBox_p1 = QLineEdit()
        self.textBox_p2 = QLineEdit()
        
        self.button.clicked.connect(import rel_move_func as rel 
                                    self.textBox_p0.text() 
                                    self.textBox_p1.text()
                                    self.textBox_p2.text()))#add kansuu
        #self.button.clicked.connect()
                
        # レイアウト配置
        self.grid = QGridLayout()
        self.grid.addWidget(self.label,      0, 0)
        self.grid.addWidget(self.button,     0, 1)
        self.grid.addWidget(self.textBox_p0, 0, 2)
        self.grid.addWidget(self.textBox_p1, 0, 3)
        self.grid.addWidget(self.textBox_p2, 0, 4)
    
        self.setLayout(self.grid)
        
        # 表示
        self.show()
        
        
        
def main():
    app = QApplication(sys.argv)
    #gui = MyWindow()
    gui = ExampleWidget()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
    


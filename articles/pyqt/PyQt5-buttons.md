Title: PyQt5 buttons
Date: 2017-10-12 00:51:01
Category: PyQt
Tags: PyQt, Python

> buttons

> PyQt5 supports buttons using the QPushButton class. This class is inside the PyQt5.QtWidgets group. The button can be created by calling the constructor QPushButton with the text to display as parameter

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 button - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # 创建 button
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(100, 70)
        # signal 和 slot 的连接
        button.clicked.connect(self.on_click)
        self.show()
    
    # Qt slot
    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```



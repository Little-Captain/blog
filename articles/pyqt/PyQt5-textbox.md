Title: PyQt5 textbox
Date: 2017-10-12 09:52:21
Category: PyQt
Tags: PyQt, Python

> textbox

> The widget is called `QLineEdit` and has the methods `setText()` to set the textbox value and `text()` to get the value.

> We can set the `size` of the textbox using the resize(width,height) method. The `position` can be set using the move(x,y) method or using a grid layout.

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # 创建 textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # 在 window 中创建一个 button
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)

        # 将 button 和 on_click 函数连接
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```


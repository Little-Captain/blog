Title: PyQt5 absolute position
Date: 2017-10-12 10:14:06
Category: PyQt
Tags: PyQt, Python

> absolute position

> PyQt5 supports several layout methods such as `grid layouts`, `horzontal layous` and `absolute positioning`. The layout you should pick depends on your preference and type of application.

> Absolute positioning gives you total control over the widget positions but you have to explicitly define every widget location.

> Widgets can be added on an absolute position using the move(x,y) method.

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QIcon


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt absolute positioning - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        label = QLabel('Python', self)
        label.move(50, 50)

        label2 = QLabel('PyQt5', self)
        label2.move(100, 100)

        label3 = QLabel('Examples', self)
        label3.move(150, 150)

        label4 = QLabel('pythonspot.com', self)
        label4.move(200, 200)

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```


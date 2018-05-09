Title: PyQt5 colors
Date: 2017-10-12 14:01:25
Category: PyQt
Tags: PyQt, Python

> colors

> Colors in PyQt5 are defined using the method `QColor(r, g, b)`. All colors on the screen are a combination of the red, green and blue values. Every color value should be in the range 0..255.
In a `QPainter` widget you can pass a color to the `setBrush` method

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import random


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt rectangle colors - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Set window background color
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)

        # Add paint widget and paint
        self.m = PainWidget(self)
        self.m.move(0, 0)
        self.m.resize(self.width, self.height)

        self.show()

class PainWidget(QWidget):
    def paintEvent(self, event):
        qp = QPainter(self)

        qp.setPen(Qt.black)
        size = self.size()

        # Colored rectangles
        qp.setBrush(QColor(200, 0, 0))
        qp.drawRect(0, 0, 100, 100)

        qp.setBrush(QColor(0, 200, 0))
        qp.drawRect(100, 0, 100, 100)

        qp.setBrush(QColor(0, 0, 200))
        qp.drawRect(200, 0, 100, 100)

        # Color Effect
        for i in range(0, 100):
            qp.setBrush(QColor(i * 10, 0, 0))
            qp.drawRect(10 * i, 100, 10, 32)

            qp.setBrush(QColor(i * 10, i * 10, 0))
            qp.drawRect(10 * i, 100 + 32, 10, 32)

            qp.setBrush(QColor(i * 2, i * 10, i * 1))
            qp.drawRect(10 * i, 100 + 64, 10, 32)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```


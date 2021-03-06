Title: PyQt5 tutorial(Events and signals)
Date: 2017-10-13 20:12:13
Category: PyQt
Tags: PyQt, Python

Events
======

> GUI applications are `event-driven`. Events are generated mainly by the user of an application. But they can be generated by other means as well; e.g. an Internet connection, a window manager, or a timer. When we call the application's `exec_()` method, the `application enters` the `main loop`. The `main loop` `fetches events` and `sends them to the objects`.

* event model 有三个参与者
  * event source : The event source is the object whose state changes. It generates events.
  * event object : The event object (event) encapsulates the state changes in the event source.
  * event target : The event target is the object that wants to be notified.
* Event source object delegates the task of handling an event to the event target. (代理设计模式)
* PyQt5 has a unique `signal and slot` mechanism to deal with events. Signals and slots are used for communication between objects. A signal is emitted when a particular event occurs. A slot can be any Python callable. A slot is called when its connected signal is emitted.

Signals and slots
=================

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        # Here we connect a valueChanged signal of the slider
        # to the display slot of the lcd number.
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Reimplementing event handler
============================

* Events in PyQt5 are processed often by reimplementing event handlers.

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    # reimplement the keyPressEvent() event handler.
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Event object
============

* Event object is a Python object that contains a number of attributes describing the event. Event object is specific to the generated event type.

```python
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        # Mouse tracking is disabled by default,
        # so the widget only receives mouse move events
        # when at least one mouse button is pressed
        # while the mouse is being moved.
        # If mouse tracking is enabled, the widget receives
        # mouse move events even if no buttons are pressed.
        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    # The e is the event object; it contains data 
    # about the event that was triggered; in our case, 
    # a mouse move event. With the x() and y() methods 
    # we determine the x and y coordinates of the mouse pointer. 
    # We build the string and set it to the label widget.
    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Event sender
============

* Sometimes it is convenient to know which widget is the sender of a signal.

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Event sender')
        self.show()

    def buttonClicked(self):
        # 获取信号发送者
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Emitting signals
================

* Objects created from a QObject can emit signals.

```python
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    # A signal is created with the pyqtSignal() as
    # a class attribute of the external Communicate class.
    closeApp = pyqtSignal()


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        # 连接信号
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        # 发送信号
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



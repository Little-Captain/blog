Title: PyQt5 tutorial(Widgets)
Date: 2017-10-13 22:30:07
Category: PyQt
Tags: PyQt, Python

* Widgets are basic building blocks of an application. PyQt5 has a wide range of various widgets, including buttons, check boxes, sliders, or list boxes. In this section of the tutorial, we will describe several useful widgets: a QCheckBox, a QPushButton in tooggle mode, a QSlider, a QProgressBar, and a QCalendarWidget.

QCheckBox
=========

* A `QCheckBox` is a widget that has two states: on and off. It is a box with a label. Checkboxes are typically used to represent features in an application that can be enabled or disabled.

```python
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        # check the checkbox
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QCheckBox')
        self.show()

    def changeTitle(self, state):

        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Toggle button
=============

* A toggle button is a QPushButton in a special mode. It is a button that has two states: pressed and not pressed. We toggle between these two states by clicking on it. There are situations where this functionality fits well.

```python
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QFrame, QApplication)
from PyQt5.QtGui import QColor
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.col = QColor(0, 0, 0)

        redb = QPushButton('Red', self)
        # 使能 checked 属性
        # To create a toggle button, we create
        # a QPushButton and make it checkable
        # by calling the setCheckable() method.
        redb.setCheckable(True)
        redb.move(10, 10)
        # We connect a clicked signal to our user defined method.
        # We use the clicked signal that operates with a Boolean value.
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 60)

        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 110)

        blueb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):

        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        # We use style sheets to change the background colour.
        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

QSlider
=======

* A QSlider is a widget that has a simple handle. This handle can be pulled back and forth. This way we are choosing a value for a specific task.

```python
from PyQt5.QtWidgets import (QWidget, QSlider,
                             QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('1.png'))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()

    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('1.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('2.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('3.png'))
        else:
            self.label.setPixmap(QPixmap('4.png'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

QProgressBar
============

* A progress bar is a widget that is used when we process lengthy tasks. It is animated so that the user knows that the task is progressing. The QProgressBar widget provides a horizontal or a vertical progress bar in PyQt5 toolkit. The programmer can set the minimum and maximum value for the progress bar. The default values are 0 and 99.

```python
from PyQt5.QtWidgets import (QWidget, QProgressBar,
                             QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)
        # To activate the progress bar, we use a timer object.
        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    # Each QObject and its descendants have a timerEvent() event handler.
    # In order to react to timer events, we reimplement the event handler.
    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):

        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            # To launch a timer event, we call its start() method.
            # This method has two parameters: the timeout and
            # the object which will receive the events.
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

QCalendarWidget
===============

* A QCalendarWidget provides a monthly based calendar widget. It allows a user to select a date in a simple and intuitive way.

```python
from PyQt5.QtWidgets import (QWidget, QCalendarWidget,
                             QLabel, QApplication, QVBoxLayout)
from PyQt5.QtCore import QDate
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout(self)

        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        vbox.addWidget(cal)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()
    # We retrieve the selected date by calling the selectedDate() method.
    # Then we transform the date object into string and set it to the label widget.
    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



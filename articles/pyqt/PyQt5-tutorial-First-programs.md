Title: PyQt5 tutorial(First programs)
Date: 2017-10-12 23:49:57
Category: PyQt
Tags: PyQt, Python

Simple example
==============

* 用于理解程序的基本原理

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget # The basic widgets are located in PyQt5.QtWidgets module

if __name__ == '__main__':
    # Every PyQt5 application must create an application object.
    # The sys.argv parameter is a list of arguments from a command line.
    # Python scripts can be run from the shell. It is a way how we can control the startup of our scripts.
    app = QApplication(sys.argv)
    # The QWidget widget is the base class of all user interface objects in PyQt5.
    # We provide the default constructor for QWidget. The default constructor has no parent. 
    # A widget with no parent is called a window.
    w = QWidget()
    # The resize() method resizes the widget.
    # It is 250px wide and 150px high.
    w.resize(250, 150) 
    # The move() method moves the widget to a position on the screen at x=300, y=300 coordinates.
    w.move(300, 300)
    # We set the title of the window with setWindowTitle().
    # The title is shown in the titlebar.
    w.setWindowTitle('Simple')
    # The show() method displays the widget on the screen. 
    # A widget is first created in memory and later shown on the screen.
    w.show()
    # Finally, we enter the mainloop of the application.
    # The event handling starts from this point. 
    # The mainloop receives events from the window system and dispatches them to the application widgets. 
    # The mainloop ends if we call the exit() method or the main widget is destroyed. 
    # The sys.exit() method ensures a clean exit. The environment will be informed how the application ended.
    # The exec_() method has an underscore. It is because the exec is a Python keyword. And thus, exec_() was used instead.
    sys.exit(app.exec_())
```

An application icon
===================

> The application icon is a small image which is usually displayed in the top left corner of the titlebar. 

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):
    def __init__(self):
        # The super() method returns the parent object of the Example class
        # and we call its constructor.
        super().__init__()
        # The creation of the GUI is delegated to the initUI() method.
        self.initUI()

    def initUI(self):
        # In fact, it combines the resize()
        # and move() methods in one method.
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        # sets the application icon
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Showing a tooltip
=================

> We can provide a balloon help for any of our widgets.

```python
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # This static method sets a font used to render tooltips.
        QToolTip.setFont(QFont('SansSerif', 10))

        # To create a tooltip, we call the setTooltip() method.
        # We can use rich text formatting.
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        # The sizeHint() method gives a recommended size for the button.
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Closing a window
================

```python
# the constructor of a QPushButton widget
# The text parameter is a text that will be displayed on the button.
# The parent is a widget on which we place our button.
# In our case it will be a QWidget.
# Widgets of an application form a hierarchy. In this hierarchy, most widgets have their parents. 
# Widgets without parents are toplevel windows.
QPushButton(string text, QWidget parent = None)
```

```python
import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        qbtn = QPushButton('Quit', self)
        # The event processing system in PyQt5
        # is built with the signal & slot mechanism.
        # If we click on the button, the signal clicked is emitted.
        # The slot can be a Qt slot or any Python callable.
        # The QCoreApplication contains the main event loop—it processes
        # and dispatches all events. The instance() method
        # gives us its current instance. Note that QCoreApplication
        # is created with the QApplication. The clicked signal is connected
        # to the quit() method which terminates the application.
        # The communication is done between two objects:
        # the sender and the receiver.
        # The sender is the push button, the receiver is the application object.
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Message Box
===========

```python
import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Message box')
        self.show()
    # If we close a QWidget, the QCloseEvent is generated.
    # To modify the widget behaviour we need to reimplement
    # the closeEvent() event handler.
    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Centering window on the screen
==============================

```python
import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Center')
        self.show()

    def center(self):
        # 自己的 Geometry
        qr = self.frameGeometry()
        # The QDesktopWidget class provides information
        # about the user's desktop, including the screen size.
        # 获取设备 Geometry, 并返回 center point
        cp = QDesktopWidget().availableGeometry().center()
        # 将 qr 的中心移到设备中心(cp)
        qr.moveCenter(cp)
        # 将 自己 移动到 qr 的左上点, 这样整个窗口就在屏幕中心了
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



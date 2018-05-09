Title: PyQt5 tutorial(Drag & drop)
Date: 2017-10-13 23:55:24
Category: PyQt
Tags: PyQt, Python

> In computer graphical user interfaces, drag-and-drop is the action of (or support for the action of) clicking on a virtual object and dragging it to a different location or onto another virtual object. In general, it can be used to invoke many kinds of actions, or create various types of associations between two abstract objects.

> Drag and drop is part of the graphical user interface. Drag and drop operations enable users to do complex things intuitively.

> Usually, we can drag and drop two things: data or some graphical objects.

QDrag
=====

* `QDrag` provides support for MIME-based drag and drop data transfer. It handles most of the details of a drag and drop operation. The transferred data is contained in a `QMimeData` object.

## Simple drag and drop

```python
from PyQt5.QtWidgets import (QPushButton, QWidget,
                             QLineEdit, QApplication)
import sys

# In order to drop text on the QPushButton widget,
# we must reimplement some methods.
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        # enable drop events for the widget with setAcceptDrops().
        self.setAcceptDrops(True)

    # reimplement the dragEnterEvent() method.
    # We inform about the data type that we accept.
    # In our case it is plain text.
    def dragEnterEvent(self, e):

        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    # reimplementing the dropEvent() method
    # we define what happes at the drop event.
    # Here we change the text of the button widget.
    def dropEvent(self, e):

        self.setText(e.mimeData().text())
        self.adjustSize()


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        edit = QLineEdit('', self)
        # The QLineEdit widget has a built-in support for drag operations. 
        # All we need to do is to call the setDragEnabled() method to activate it.
        edit.setDragEnabled(True)
        edit.move(30, 65)

        button = Button("Button", self)
        button.move(190, 65)

        self.setWindowTitle('Simple drag and drop')
        self.setGeometry(300, 300, 300, 150)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
```

## Drag and drop a button widget

```python
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag
import sys


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    # reimplement two methods of the QPushButton:
    # the mouseMoveEvent() and the mousePressEvent()
    # The mouseMoveEvent() method is the place where
    # the drag and drop operation begins.
    def mouseMoveEvent(self, e):
        # Here we decide that we can perform
        # drag and drop only with a right mouse button.
        if e.buttons() != Qt.RightButton:
            return

        # The QDrag object is created.
        # The class provides support for MIME-based
        # drag and drop data transfer.
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())
        # The exec_() method of the drag object starts
        # the drag and drop operation.
        dropAction = drag.exec_(Qt.MoveAction)

    def mousePressEvent(self, e):

        super().mousePressEvent(e)

        if e.button() == Qt.LeftButton:
            print('press')


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 280, 150)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)
        # We specify the type of the drop action with setDropAction(). 
        # In our case it is a move action.
        e.setDropAction(Qt.MoveAction)
        e.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
```


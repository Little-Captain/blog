Title: PyQt5 tutorial(Layout management)
Date: 2017-10-13 16:18:01
Category: PyQt
Tags: PyQt, Python

> Layout management is the way how we place the widgets on the application window. We can place our widgets using `absolute positioning` or with `layout classes`. Managing the layout with `layout managers` is the `preferred` way of organizing our widgets.

Absolute positioning
====================

* The programmer specifies the position and the size of each widget in pixels. 
* When you use absolute positioning, we have to understand the following limitations:
  * The size and the position of a widget do not change if we resize a window
  * Applications might look different on various platforms
  * Changing fonts in our application might spoil the layout
  * If we decide to change our layout, we must completely redo our layout, which is tedious and time consuming
  
```python
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        # The x values grow from left to right. 
        # The y values grow from top to bottom.
        lbl1.move(100, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)

        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```
  
Box layout
==========
  
* `QHBoxLayout` and `QVBoxLayout` are basic layout classes that line up widgets horizontally and vertically.
* Imagine that we wanted to place two buttons in the right bottom corner. To create such a layout, we use one horizontal and one vertical box. To create the necessary space, we add a stretch factor.
  
```python
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        # The stretch adds a stretchable space before the two buttons.
        # This will push them to the right of the window.
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        # The stretch factor in the vertical box will push
        # the horizontal box with the buttons to the bottom of the window.
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

QGridLayout
===========

* QGridLayout is the most universal layout class. It divides the space into rows and columns.

```python
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
                             QPushButton, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]
        # zip : zip([1, 2], [3, 4]) => [(1, 3), (2, 4)] (zip object)
        # 同时遍历 position、name
        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            # Python 允许你在 list 或 tuple 前面加一个 * 号，
            # 把 list 或 tuple 的元素变成可变参数传进去
            grid.addWidget(button, *position)

        self.move(300, 150)
        self.setWindowTitle('Calculator')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Review example
==============

* Widgets can span multiple columns or rows in a grid

```python
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()
        # We create a grid layout and set spacing between widgets.
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        
        grid.addWidget(review, 3, 0)
        # If we add a widget to a grid, we can provide row span and column span of the widget.
        grid.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



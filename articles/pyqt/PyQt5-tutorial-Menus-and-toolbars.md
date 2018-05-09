Title: PyQt5 tutorial(Menus and toolbars)
Date: 2017-10-13 11:10:55
Category: PyQt
Tags: PyQt, Python

QMainWindow
===========

> The `QMainWindow` class provides a main application window. This enables to create a classic application skeleton with a statusbar, toolbars, and a menubar.

Statusbar
=========

> A statusbar is a widget that is used for displaying status information.

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # statusBar 是懒加载的
        # To get the statusbar, we call the statusBar() method 
        # of the QtGui.QMainWindow class. The first call of 
        # the method creates a status bar. 
        # Subsequent calls return the statusbar object. 
        # The showMessage() displays a message on the statusbar.
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Statusbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Simple menu
===========

> A menubar is a common part of a GUI application. It is a group of commands located in various menus. (Mac OS treats menubars differently. To get a similar outcome, we can add the following line: menubar.setNativeMenuBar(False).)

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        # 针对 macOS 适配
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Simple menu')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Submenu
=======

> A submenu is a menu located inside another menu.

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        # 针对 macOS 适配
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('File')

        # New menu is created with QMenu.
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self)
        # An action is added to the submenu with addAction().
        impMenu.addAction(impAct)

        newAct = QAction('New', self)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Check menu
==========

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        # 针对 macOS 适配
        menubar.setNativeMenuBar(False)
        viewMenu = menubar.addMenu('View')
        # 创建 action, 使能 check
        viewStatAct = QAction('View statusbar', self, checkable=True)
        # 设置相应的状态栏提示
        viewStatAct.setStatusTip('View statusbar')
        # 默认 checked
        viewStatAct.setChecked(True)
        # 连接方法 toggleMenu
        viewStatAct.triggered.connect(self.toggleMenu)
        # 添加 action
        viewMenu.addAction(viewStatAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self, state):
        # 根据状态设置状态栏是否隐藏
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Context menu
============

> A context menu, also called a popup menu, is a list of commands that appears under some context. 

```python
import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Context menu')
        self.show()
    # To work with a context menu, we have to
    # reimplement the contextMenuEvent() method.
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        # The context menu is displayed with the exec_() method.
        # The get the coordinates of the mouse pointer from the event object.
        # The mapToGlobal() method translates the widget coordinates
        # to the global screen coordinates.
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Toolbar
=======

> Toolbars provide a quick access to the most frequently used commands.

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon('web.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)
        # The toolbar is created with the addToolBar() method.
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```

Putting it together
===================

```python
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('web.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)

        self.statusBar()

        menubar = self.menuBar()
        # 针对 macOS 适配
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```


Title: PyQt5 drag and drop
Date: 2017-10-12 14:13:58
Category: PyQt
Tags: PyQt, Python

> drag and drop

> Like any modern GUI toolkit, PyQt supports drag and drop. A widget parameter must be set using the setDragEnabled(True) method call. A custom widget should then be set to accept a drop with setAcceptDrops(True).

```python
# Drag text from the input field to the label, the label will update its text.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 drag and drop - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        editBox = QLineEdit('Drag this', self)
        editBox.setDragEnabled(True)
        editBox.move(10, 10)
        editBox.resize(100, 32)

        button = CustomLabel('Drop here', self)
        button.move(130, 15)

        self.show()

class CustomLabel(QLabel):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    # 拖拽进入事件
    def dragEnterEvent(self, e):
        # 校验数据格式
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()
    # 拖拽释放事件
    def dropEvent(self, e):
        self.setText(e.mimeData().text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```



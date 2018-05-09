Title: PyQt5 window
Date: 2017-10-12 00:16:46
Category: PyQt
Tags: PyQt, Python

> window

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 simple window - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()

# Make a script both importable and executable
# 直接执行这个文件, 模块名(__name__)为 `__main__`
# 导入到其他文件中, 模块名(__name__)为 `py文件的文件名`
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```



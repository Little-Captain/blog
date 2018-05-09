Title: PyQt5 messagebox
Date: 2017-10-12 09:36:49
Category: PyQt
Tags: PyQt, Python

> messagebox

> To show a messagebox we need to import `QMessageBox`. We use the method `QMessageBox.question()` to display the messagebox

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 messagebox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        # 创建 messagebox 对象, 同步等待用户选择结果
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you like PyQt5?",
                                           QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 处理结果
        if buttonReply == QMessageBox.Yes:
            print('Yes clicked')
        else:
            print('No clicked')
        # 显示
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
```

* available buttons

```python
QMessageBox.Cancel
QMessageBox.Ok
QMessageBox.Help
QMessageBox.Open
QMessageBox.Save
QMessageBox.SaveAll
QMessageBox.Discard
QMessageBox.Close	
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.NoButton
QMessageBox.RestoreDefaults
QMessageBox.Abort	
QMessageBox.Retry
QMessageBox.Ignore
```



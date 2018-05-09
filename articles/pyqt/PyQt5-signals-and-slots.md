Title: PyQt5 signals and slots
Date: 2017-10-12 09:19:08
Category: PyQt
Tags: PyQt, Python

> signals and slots

> Graphical applications (GUI) are event-driven, unlike console or terminal applications. A users action like clicks a button or selecting an item in a list is called an event.

> If an event takes place, each PyQt5 widget can emit a signal. A signal does not execute any action, that is done by a slot.

* 基本格式

```python
# The button click (signal) is connected to the action (slot)
button.clicked.connect(self.slot_method)
# This principle of connecting slots methods or function to a widget, applies to all widgets
widget.signal.connect(slot_method)
```

* 显式的定义信号

```python
QtCore.QObject.connect(widget, QtCore.SIGNAL(‘signalname’), slot_function)
```

> PyQt supports many type of signals, not just clicks. A slot is any callable function or method.

```python
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,\
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,\
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,\
                             QVBoxLayout)
import sys

class Dialog(QDialog):
    
    def slot_method(self):
        print('slot method called')

    def __init__(self):
        super(Dialog, self).__init__()

        button = QPushButton('Click')
        button.clicked.connect(self.slot_method)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(button)

        self.setLayout(mainLayout)
        self.setWindowTitle('Button Example - pythonspot.com')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
```


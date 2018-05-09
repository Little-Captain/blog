Title: PyQt5 Form Layout
Date: 2017-10-12 20:48:17
Category: PyQt
Tags: PyQt, Python

> Form Layout

> A form can be created using the class QFormLayout. This is the easiest way to create a form where widgets (input) have descriptions (labels)

```python
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

import sys


class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle('Form Layout - pythonspot.com')

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox('Form layout')
        layout = QFormLayout()
        # The Form Layout is created using the class QFormLayout. We can add rows to the form using the method addRow.
        layout.addRow(QLabel('Name:'), QLineEdit())
        layout.addRow(QLabel("Country:"), QComboBox())
        layout.addRow(QLabel("Age:"), QSpinBox())
        self.formGroupBox.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
```



Title: PyQt(Chapter 07)
Date: 2017-10-11 17:30:05
Category: PyQt
Tags: PyQt, Python

> PyQt

窗口和对话框
==========

* 对话框包括两类: modal、modeless
  * modal: 禁止用户与程序的其他部分交互
  * modeless: 与 modal 相对, 用户可以自由的与应用程序的其他部分交互

创建应用程序
==========

* 通过简单的纯文本编辑器创建
* 使用 Qt Designer

使用 Code 创建 GUI 程序
=====================

* 这是针对 Qt4 的代码, Qt5 运行要不起来

```python
# 导入需要的模块
import sys
from PyQt5 import QtGui, QtCore
# QWidget 是所有的交互对象的基类
class demowind(QtGui.QWidget):
    # 构造函数
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        # 设置控件的几何属性
        self.setGeometry(300, 300, 200, 200)
        # 设置title, title将显示在title bar上
        self.setWindowTitle('Demo window')
        # 创建一个 Push 按钮, 显示 `Close` 文字
        quit = QtGui.QPushButton('Close', self)
        # 设置几何属性, 相对父控件
        quit.setGeometry(10, 10, 70, 40)
        # 事件处理 : signal 和 slot
        # signal 是 事件
        # slot 是 当事件发生时的处理方法
        # connect 方法将 signal 和 slot 进行连接
        self.connect(quit, QtCore.SIGNAL('clicked()'), \
                     QtGui.qApp, QtCore.SLOT('quit()'))
# 创建应用程序对象
app = QtGui.QApplication(sys.argv)
# 创建 demowind 实例对象
dw = demowind()
# 显示 dw
dw.show()
# 启动事件处理循环
# 事件处理直到: exit 方法被调用, 或主控件被销毁
# exec_ 有 _ 是因为 exec 被 Python 关键字占用了
sys.exit(app.exec_())
```

使用 Qt Designer
================

* 预定义的 UI 模板
  * Dialog with buttons at the bottom : OK 和 Cancel 按钮被放置在底部的对话框
  * Dialog with buttons on the right : OK 和 Cancel 按钮被放置在右侧的对话框
  * Dialog without buttons : 没有任何按钮的对话框
  * Main window : 提供一个带有菜单栏和工具栏(可以移除)的应用程序主窗口
  * Widget : 创建一个父类是 QWidget 的控件

> When creating a GUI application, you need to specify a `top-level widget`, which is usually `QDialog`, `QWidget`, or `QMainWindow`. If you create an application based on the `Dialog template`, the top-level widget or the first class that you inherit is `QDialog`. Similarly, if the application is based on the `Main Window template`, the top-level widget will be `QMainWindow`, and if you use the `Widget template` for your application, the top-level widget will be `QWidget`. The widgets that you use for the user interface are then treated as child widgets of the classes.

> The `main component` used for creating a user interface is `widgets`. `Button`, `menus`, and `scrollbars` are examples of widgets and are not only used for receiving user input but also for displaying data and status information. `Widgets` can be `nested` inside another in a parent-child relationship. A widget that has `no parent widget` is called a `window`. The class for widgets, `QWidget`, provides methods to render them on screen, receive user input, and handle different events. `All UI elements that Qt provides are subclasses of QWidget`. Qt Designer displays a list of widgets in a Widget Box displayed on the left side.

## Widget Box

* Widget Box 用于分类显示 widget 的列表, 相似功能的 widget 放入一个分类中
* 类别
  * Layouts
  * Spacers
  * Buttons
  * Item Views(Model-Based)
  * Item Widgets(Item-Based)
  * Containers
  * Input Widgets
  * Display Widgets
  * Phonon

### Layouts

> Layouts are used for arranging widgets in a desired manner. The `layout` `controls` the `size` of the `widgets` `within it`, and `widgets` are `automatically` `resized` when the form is resized.

* 用于布局控件

| widget | description |
| :-: | :-: |
| Vertical Layout(QVBoxLayout) | Arranges widgets vertically, one below the other |
| Horizontal Layout(QHBoxLayout) | Arranges widgets horizontally, one next to the other |
| Grid Layout (QGridLayout) | Arranges widgets into rows and columns |
| Form Layout (QFormLayout) | Arranges widgets in a two- column layout. The first column usually displays message(s) in labels, and the second column usually contains the widgets, enabling the user to enter/edit data corresponding to the labels in the first column |

### Spacers

> Spacers are not visible while running a form and are used for inserting spaces between widgets or groups of widgets.

* 用于在控件间插入空白

| widget | description |
| :-: | :-: |
| Horizontal Spacer (Spacer) | Inserts horizontal spaces between widgets |
| Vertical Spacer (Spacer) | Inserts vertical spaces between widgets |

### Buttons

> Buttons are used to initiate an action. They are event or signal generators that can be used to perform tasks.

| widget | description |
| :-: | :-: |
| Push Button (QPushButton) | Displays a command button |
| Tool Button (QToolButton) | Displays a button to access commands or options. Used inside a toolbar |
| Radio Button (QRadioButton) | Displays a radio button with a text label |
| Check Box (QCheckBox) | Displays a check box with a text label |
| Command Link Button (QCommandLinkButton) | Displays a command link button |
| Button Box (QDialogButtonBox) | A sub-class of QWidgetthat presents a set of buttons in a layout |

### Item Views (Model-Based)

> Item Views widgets are used for displaying large volumes of data. Model-based means that the widgets are part of a `model/view` framework and enable you to present data in different formats and through multiple views. The classes of these widgets implement the interfaces defined by the `QAbstractItemViewclass` to allow it to display data provided by models derived from the `QAbstractItemModelclass`.

| widget | description |
| :-: | :-: |
| List View (QListView) | Used to display a list of items. Must be used with a QAbstractItemModel subclass |
| Tree View (QTreeView) | Used to display hierarchical data. Must be used with a QAbstractItemModel subclass |
| Table View (QTableView) | Used to display data in tabular form. Can display icons as well as text in every cell. Must be used in conjunction with a QAbstractItemModel subclass |
| Column View (QColumnView) | Provides a model/view implementation of a column view. It displays data in a number of list views |

### Item Widgets (Item-Based)

> Item Widgets have self-contained views.

| widget | description |
| :-: | :-: |
| List Widget (QListWidget) | Used to display a list of items. It has a built-in model, so items can be added to it directly |
| Tree Widget (QTreeWidget) | Used to display hierarchical data. It has a built-in model, so items can be added to it directly |
| Table Widget (QTableWidget) | Used to display data in tabular form. Can display icons as well as text in every cell. It has a built-in model, so items can be added to it directly |

### Containers

> Container widgets are used to control a collection of objects on a form. A widget dropped onto a container becomes a child object of the container. The child objects in a container can also be arranged in desired layouts.

| widget | description |
| :-: | :-: |
| Group Box (QGroupBox) | Used to group together a collection of widgets of similar function |
| Scroll Area (QScrollArea) | Used to display the contents of a child widget within a frame. If the child widget exceeds the size of the frame, scrollbars appear to enable you to view the entire child widget |
| Tool Box (QToolBox) | Displays a series of pages or sections in a tool box |
| Tab Widget (QTabWidget) | Displays tabs that can be used to display information. A large volume of information can be displayed by splitting it into chunks and displaying it under individual tabs |
| Stacked Widget (QStackedWidget) | Displays a stack of widgets where only one widget is visible at a time |
| Frame (QFrame) | Used to enclose and group widgets. Can also be used as a placeholder in forms |
| Widget (QWidget) | The base class of all user interface objects |
| MdiArea (QMdiArea) | Provides an area for displaying MDI windows |
| Dock Widget (QDockWidget) | Can be docked inside a main window or floated as an independent tool window |


### Input Widgets

> Input Widgets are for used for interacting with the user. The user can supply data to the application through these widgets.

| widget | description |
| :-: | :-: |
| Combo Box (QComboBox) | Displays a pop-up list |
| Font Combo Box (QFontComboBox) | Displays a combo box that allows font selection |
| Line Edit (QLineEdit) | Displays a single-line text box for entering/editing plain text |
| Text Edit (QTextEdit) | Used to edit plain text or HTML |
| Plain Text Edit (QPlainTextEdit) | Used to edit and display plain text |
| Spin Box (QSpinBox) | Displays a spin box |
| Double Spin Box (QDoubleSpinBox) | Displays a spin box for double values |
| Time Edit (QTimeEdit) | Used for editing times |
| Date Edit (QDateEdit) | Used for editing dates |
| Date/Time Edit (QDateTimeEdit) | Used for editing dates and times |
| Dial (QDial) | Displays a rounded range control |
| Horizontal Scrollbar (QScrollBar) | Displays a horizontal scrollbar |
| Vertical Scrollbar (QScrollBar) | Displays a vertical scrollbar |
| Horizontal Slider(QSlider) | Displays a horizontal slider |
| Vertical Slider (QSlider) | Displays a vertical slider |
| QsciScintilla | Scintilla is an editing component that performs syntax styling, code completion, break points, auto indenting, and other tasks. It is very useful in editing and debugging source code. The Scintilla component is inside QsciScintillaand used in Qt Designer for developing GUI applications like any other Qt widget |

### Display Widgets

> Display widgets are used for displaying information or messages to the user.


| widget | description |
| :-: | :-: |
| Label (QLabel) | Displays text or images |
| Text Browser (QTextBrowser) | Displays a read-only multiline text box that can display both plain text and HTML, including lists, tables, and images. It supports clickable links as well as cascading style sheets |
| Graphics View (QGraphicsView) | Used to displays graphics |
| Calendar (QCalenderWidget) | Displays a monthly calendar allowing you to select a date |
| LCD Number (QLCDNumber) | Displays digits in LCD-like display |
| Progress Bar (QProgressBar) | Displays horizontal and vertical progress bars |
| Horizontal Line (QFrame) | Displays a horizontal line |
| Vertical Line (QFrame) | Displays a vertical line |
| QDeclarativeView | A QGraphicsViewsubclass provided for displaying QML interfaces. To display a QML interface within QWidget-based GUI applications that do not use the Graphics View framework, QDeclarativeis used. QDeclarativeViewinitializes QGraphicsViewfor optimal performance with QML so that user interface objects can be placed on a standard QGraphicsSceneand displayed with QGraphics-View. QML is a declarative language used to describe the user interface in a tree of objects with properties |
| QWebView | Used to view and edit web documents |

### Phonon

> Phonon is a multimedia API that provides an abstraction layer for capturing, mixing, processing, and playing audio and video.

| widget | description |
| :-: | :-: |
| Phonon::VideoPlayer | Used to display video |
| Phonon::SeekSlider | Displays slider for setting positions in media stream |
| Phonon::VolumeSlider | Displays slider to control volume of audio output |

基本控件
=======

## Displaying Text

> To display non-editable text or an image, Label widgets are used; a Label is an instance of the `QLabel` class. A Label widget is a very popular widget for displaying messages or information to the user.

| Methods | Usage |
| :-: | :-: |
| setText() | Assigns text to the Label widget |
| setPixmap() | Assigns a pixmap, an instance of the QPixmapclass, to the Label widget |
| setNum() | Assigns an integer or double value to the Label widget |
| clear() | Clears text from the Label widget |

## Entering Single-Line Data

> To allow the user to enter or edit single-line data, you use the Line Edit widget, which is an instance of `QLineEdit`. The widget `supports` simple editing mechanisms such as `undo`, `redo`, `cut`, and `paste`.

| Methods | Usage |
| :-: | :-: |
| setEchoMode() | Used to set the echo mode of the Line Edit widget to determine how the contents of the Line Edit widget are displayed. The available options are these: <br> Normal: Default mode. Displays characters as they are entered. <br> NoEcho: Doesn’t display anything. <br> Password: Displays asterisks as the user enters data. <br> PasswordEchoOnEdit: Displays characters when editing; otherwise, asterisks are displayed. |
| maxLength() | Used to specify the maximum length of text that user can enter. For multiline editing, you use QTextEdit |
| setText() | Assigns text to the Line Edit widget |
| text() | Fetches the text entered in the Line Edit widget |
| clear() | Clears the contents of the Line Edit widget |
| setReadOnly() | Passes the Boolean value true to this method to make the Line Edit widget read-only. The user cannot edit the contents of the Line Edit widget but can copy it. The cursor will become invisible in read-only mode |
| isReadOnly() | Returns true if the Line Edit widget is in read-only mode |
| setEnabled() | The Line Edit widget will be blurred, indicating that it is disabled. You cannot edit content in a disabled Line Edit widget, but you can assign text via the setText() method |
| setFocus() | Used to set the cursor on the specified Line Edit widget |

* 相关信号(signal)

| Signals | Usage |
| :-: | :-: |
| textChanged() | The signal is emitted when text in the Line Edit widget is changed |
| returnPressed() | The signal is emitted when Return or Enter is pressed |
| editingFinished() | The signal is emitted when focus is lost on the Line Edit widget, confirming the editing task is over on it |

## Displaying Buttons

> To display pushbuttons (usually command buttons) in an application, you need to create an instance of the `QPushButton` class. When assigning text to buttons, you can create `shortcut` keys by preceding any character in the text with an `ampersand`.

| Methods | Usage |
| :-: | :-: |
| setText() | Used to assign the text to the pushbutton |
| setIcon() | Used to assign icon to the pushbutton |

Event Handling in PyQt
======================

> In PyQt, the `event-handling mechanism` is also known as `signals and slots`. Every widget emits signals when its state changes. Whenever a signal is emitted, it is simply thrown. To perform a task in response to a signal, the signal has to be connected to a slot. A slot refers to the method containing the code that you want to be executed on occurrence of a signal. Most widgets have predefined slots, you don’t have to write code for connecting a predefined signal to a predefined slot. To respond to the signals emitted, you identify the `QObject` and the signal it emits and invoke the associated method. You can use Qt Designer for connecting signals with built-in slots.



Title: PyQt5 tutorial(Introduction)
Date: 2017-10-12 21:27:32
Category: PyQt
Tags: PyQt, Python

PyQt5 modules
=============

* PyQt5's classes are divided into several modules

| module | function |
| :-: | :-: |
| QtCore | The QtCore module contains the core non-GUI functionality. This module is used for working with time, files and directories, various data types, streams, URLs, mime types, threads or processes. |
| QtGui | The QtGui contains classes for windowing system integration, event handling, 2D graphics, basic imaging, fonts and text. |
| QtWidgets | The QtWidgets module contains classes that provide a set of UI elements to create classic desktop-style user interfaces. |
| QtMultimedia | The QtMultimedia contains classes to handle multimedia content and APIs to access camera and radio functionality. |
| QtBluetooth | The QtBluetooth module contains classes to scan for devices and connect and interact with them.  |
| QtNetwork | The QtNetwork module contains the classes for network programming. These classes facilitate the coding of TCP/IP and UDP clients and servers by making the network programming easier and more portable. |
| QtPositioning | The QtPositioning contains classes to determine a position by using a variety of possible sources, including satellite, Wi-Fi, or a text file. |
| Enginio | The Enginio module implements the client-side library for accessing the Qt Cloud Services Managed Application Runtime. |
| QtWebSockets | The QtWebSockets module contains classes that implement the WebSocket protocol. |
| QtWebKit | The QtWebKit contains classes for a web browser implementation based on the WebKit2 library.  |
| QtWebKitWidgets | The QtWebKitWidgets contains classes for a WebKit1 based implementation of a web browser for use in QtWidgets based applications. |
| QtXml | The QtXml contains classes for working with XML files. This module provides implementation for both SAX and DOM APIs. |
| QtSvg | The QtSvg module provides classes for displaying the contents of SVG files. Scalable Vector Graphics (SVG) is a language for describing two-dimensional graphics and graphical applications in XML. |
| QtSql | The QtSql module provides classes for working with databases. |
| QtTest | The QtTest contains functions that enable unit testing of PyQt5 applications. |

PyQt4 and PyQt5 differences
===========================

* Python modules have been reorganized. Some modules have been dropped (QtScript), others have been split into submodules (QtGui, QtWebKit).
* New modules have been introduced, including QtBluetooth, QtPositioning, or Enginio.
* PyQt5 supports only the new-style signal and slots handlig. The calls to SIGNAL() or SLOT() are no longer supported.
* PyQt5 does not support any parts of the Qt API that are marked as deprecated or obsolete in Qt v5.0.





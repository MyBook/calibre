# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/shortcuts.ui'
#
# Created: Thu Jul 19 23:32:29 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(400, 170)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.gridLayout = QtGui.QGridLayout(Frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.default_shortcuts = QtGui.QRadioButton(Frame)
        self.default_shortcuts.setObjectName(_fromUtf8("default_shortcuts"))
        self.gridLayout.addWidget(self.default_shortcuts, 1, 0, 1, 2)
        self.custom = QtGui.QRadioButton(Frame)
        self.custom.setObjectName(_fromUtf8("custom"))
        self.gridLayout.addWidget(self.custom, 2, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(25, -1, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label1 = QtGui.QLabel(Frame)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.horizontalLayout.addWidget(self.label1)
        self.button1 = QtGui.QPushButton(Frame)
        self.button1.setObjectName(_fromUtf8("button1"))
        self.horizontalLayout.addWidget(self.button1)
        self.clear1 = QtGui.QToolButton(Frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("clear_left.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear1.setIcon(icon)
        self.clear1.setObjectName(_fromUtf8("clear1"))
        self.horizontalLayout.addWidget(self.clear1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(25, -1, -1, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label2 = QtGui.QLabel(Frame)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.horizontalLayout_3.addWidget(self.label2)
        self.button2 = QtGui.QPushButton(Frame)
        self.button2.setObjectName(_fromUtf8("button2"))
        self.horizontalLayout_3.addWidget(self.button2)
        self.clear2 = QtGui.QToolButton(Frame)
        self.clear2.setIcon(icon)
        self.clear2.setObjectName(_fromUtf8("clear2"))
        self.horizontalLayout_3.addWidget(self.clear2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)
        self.header = QtGui.QLabel(Frame)
        self.header.setText(_fromUtf8(""))
        self.header.setWordWrap(True)
        self.header.setObjectName(_fromUtf8("header"))
        self.gridLayout.addWidget(self.header, 0, 0, 1, 2)
        self.label1.setBuddy(self.button1)
        self.label2.setBuddy(self.button1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_("Frame"))
        self.default_shortcuts.setText(_("&Default"))
        self.custom.setText(_("&Custom"))
        self.label1.setText(_("&Shortcut:"))
        self.button1.setToolTip(_("Click to change"))
        self.button1.setText(_("None"))
        self.clear1.setToolTip(_("Clear"))
        self.clear1.setText(_("..."))
        self.label2.setText(_("&Alternate shortcut:"))
        self.button2.setToolTip(_("Click to change"))
        self.button2.setText(_("None"))
        self.clear2.setToolTip(_("Clear"))
        self.clear2.setText(_("..."))



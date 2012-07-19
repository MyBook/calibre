# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/conversion.ui'
#
# Created: Fri May 11 09:13:10 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(720, 603)
        self.horizontalLayout = QtGui.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.list = QtGui.QListView(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setMinimumSize(QtCore.QSize(180, 0))
        self.list.setMaximumSize(QtCore.QSize(180, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.list.setFont(font)
        self.list.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.list.setTabKeyNavigation(True)
        self.list.setProperty("showDropIndicator", False)
        self.list.setIconSize(QtCore.QSize(48, 48))
        self.list.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.list.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.list.setFlow(QtGui.QListView.TopToBottom)
        self.list.setSpacing(10)
        self.list.setViewMode(QtGui.QListView.ListMode)
        self.list.setObjectName(_fromUtf8("list"))
        self.horizontalLayout.addWidget(self.list)
        self.stack = QtGui.QStackedWidget(Form)
        self.stack.setObjectName(_fromUtf8("stack"))
        self.horizontalLayout.addWidget(self.stack)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))


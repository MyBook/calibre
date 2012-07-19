# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/quickview.ui'
#
# Created: Mon Jun 27 12:05:40 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Quickview(object):
    def setupUi(self, Quickview):
        Quickview.setObjectName(_fromUtf8("Quickview"))
        Quickview.resize(768, 342)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Quickview.sizePolicy().hasHeightForWidth())
        Quickview.setSizePolicy(sizePolicy)
        self.gridlayout = QtGui.QGridLayout(Quickview)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.items_label = QtGui.QLabel(Quickview)
        self.items_label.setObjectName(_fromUtf8("items_label"))
        self.gridlayout.addWidget(self.items_label, 0, 0, 1, 1)
        self.items = QtGui.QListWidget(Quickview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.items.sizePolicy().hasHeightForWidth())
        self.items.setSizePolicy(sizePolicy)
        self.items.setObjectName(_fromUtf8("items"))
        self.gridlayout.addWidget(self.items, 1, 0, 1, 1)
        self.books_label = QtGui.QLabel(Quickview)
        self.books_label.setObjectName(_fromUtf8("books_label"))
        self.gridlayout.addWidget(self.books_label, 0, 1, 1, 1)
        self.books_table = QtGui.QTableWidget(Quickview)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(4)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.books_table.sizePolicy().hasHeightForWidth())
        self.books_table.setSizePolicy(sizePolicy)
        self.books_table.setColumnCount(0)
        self.books_table.setRowCount(0)
        self.books_table.setObjectName(_fromUtf8("books_table"))
        self.books_table.setColumnCount(0)
        self.books_table.setRowCount(0)
        self.gridlayout.addWidget(self.books_table, 1, 1, 1, 1)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.search_button = QtGui.QPushButton(Quickview)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.hboxlayout.addWidget(self.search_button)
        spacerItem = QtGui.QSpacerItem(0, 0, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(Quickview)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.hboxlayout.addWidget(self.buttonBox)
        self.gridlayout.addLayout(self.hboxlayout, 3, 0, 1, 2)

        self.retranslateUi(Quickview)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Quickview.reject)
        QtCore.QMetaObject.connectSlotsByName(Quickview)

    def retranslateUi(self, Quickview):
        Quickview.setWindowTitle(_("Quickview"))
        self.items_label.setText(_("Items"))
        self.search_button.setText(_("Search"))
        self.search_button.setToolTip(_("Search in the library view for the selected item"))


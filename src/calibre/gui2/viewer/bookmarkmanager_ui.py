# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\work\cl\src\calibre\gui2\viewer\bookmarkmanager.ui'
#
# Created: Fri Apr 20 12:37:20 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BookmarkManager(object):
    def setupUi(self, BookmarkManager):
        BookmarkManager.setObjectName(_fromUtf8("BookmarkManager"))
        BookmarkManager.resize(451, 363)
        self.gridLayout = QtGui.QGridLayout(BookmarkManager)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(BookmarkManager)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.button_edit = QtGui.QPushButton(self.groupBox)
        self.button_edit.setObjectName(_fromUtf8("button_edit"))
        self.verticalLayout.addWidget(self.button_edit)
        self.button_delete = QtGui.QPushButton(self.groupBox)
        self.button_delete.setObjectName(_fromUtf8("button_delete"))
        self.verticalLayout.addWidget(self.button_delete)
        self.button_revert = QtGui.QPushButton(self.groupBox)
        self.button_revert.setObjectName(_fromUtf8("button_revert"))
        self.verticalLayout.addWidget(self.button_revert)
        self.button_export = QtGui.QPushButton(self.groupBox)
        self.button_export.setObjectName(_fromUtf8("button_export"))
        self.verticalLayout.addWidget(self.button_export)
        self.button_import = QtGui.QPushButton(self.groupBox)
        self.button_import.setObjectName(_fromUtf8("button_import"))
        self.verticalLayout.addWidget(self.button_import)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.bookmarks_table = QtGui.QTableView(BookmarkManager)
        self.bookmarks_table.setProperty("showDropIndicator", False)
        self.bookmarks_table.setAlternatingRowColors(True)
        self.bookmarks_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.bookmarks_table.setSortingEnabled(False)
        self.bookmarks_table.setObjectName(_fromUtf8("bookmarks_table"))
        self.gridLayout.addWidget(self.bookmarks_table, 0, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(BookmarkManager)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

        self.retranslateUi(BookmarkManager)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), BookmarkManager.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), BookmarkManager.reject)
        QtCore.QMetaObject.connectSlotsByName(BookmarkManager)

    def retranslateUi(self, BookmarkManager):
        BookmarkManager.setWindowTitle(_("Bookmark Manager"))
        self.groupBox.setTitle(_("Actions"))
        self.button_edit.setText(_("Edit"))
        self.button_delete.setText(_("Delete"))
        self.button_revert.setText(_("Reset"))
        self.button_export.setText(_("Export"))
        self.button_import.setText(_("Import"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/dialogs/tag_list_editor.ui'
#
# Created: Thu Jul 19 23:32:30 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_TagListEditor(object):
    def setupUi(self, TagListEditor):
        TagListEditor.setObjectName(_fromUtf8("TagListEditor"))
        TagListEditor.resize(397, 335)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("chapters.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TagListEditor.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(TagListEditor)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.search_box = HistoryLineEdit(TagListEditor)
        self.search_box.setObjectName(_fromUtf8("search_box"))
        self.horizontalLayout_11.addWidget(self.search_box)
        self.search_button = QtGui.QToolButton(TagListEditor)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.horizontalLayout_11.addWidget(self.search_button)
        self.gridlayout.addLayout(self.horizontalLayout_11, 0, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.delete_button = QtGui.QToolButton(TagListEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("trash.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QtCore.QSize(32, 32))
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.verticalLayout_2.addWidget(self.delete_button)
        self.rename_button = QtGui.QToolButton(TagListEditor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("edit_input.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_button.setIcon(icon2)
        self.rename_button.setIconSize(QtCore.QSize(32, 32))
        self.rename_button.setObjectName(_fromUtf8("rename_button"))
        self.verticalLayout_2.addWidget(self.rename_button)
        self.gridlayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.table = QtGui.QTableWidget(TagListEditor)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.gridlayout.addWidget(self.table, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(TagListEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.retranslateUi(TagListEditor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), TagListEditor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), TagListEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(TagListEditor)

    def retranslateUi(self, TagListEditor):
        TagListEditor.setWindowTitle(_("Category Editor"))
        self.search_box.setToolTip(_("Search for an item in the Tag column"))
        self.search_button.setText(_("Find"))
        self.search_button.setToolTip(_("Copy the selected color name to the clipboard"))
        self.delete_button.setToolTip(_("Delete item from database. This will unapply the item from all books and then remove it from the database."))
        self.delete_button.setText(_("..."))
        self.rename_button.setToolTip(_("Rename the item in every book where it is used."))
        self.rename_button.setText(_("..."))
        self.rename_button.setShortcut(_("Ctrl+S"))

from calibre.gui2.widgets import HistoryLineEdit

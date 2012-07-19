# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/device_category_editor.ui'
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

class Ui_DeviceCategoryEditor(object):
    def setupUi(self, DeviceCategoryEditor):
        DeviceCategoryEditor.setObjectName(_fromUtf8("DeviceCategoryEditor"))
        DeviceCategoryEditor.resize(397, 335)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("chapters.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeviceCategoryEditor.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(DeviceCategoryEditor)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(DeviceCategoryEditor)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName(_fromUtf8("hboxlayout1"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.delete_button = QtGui.QToolButton(DeviceCategoryEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("trash.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_button.setIcon(icon1)
        self.delete_button.setIconSize(QtCore.QSize(32, 32))
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.verticalLayout_2.addWidget(self.delete_button)
        self.rename_button = QtGui.QToolButton(DeviceCategoryEditor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("edit_input.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_button.setIcon(icon2)
        self.rename_button.setIconSize(QtCore.QSize(32, 32))
        self.rename_button.setObjectName(_fromUtf8("rename_button"))
        self.verticalLayout_2.addWidget(self.rename_button)
        self.hboxlayout1.addLayout(self.verticalLayout_2)
        self.available_tags = QtGui.QListWidget(DeviceCategoryEditor)
        self.available_tags.setAlternatingRowColors(True)
        self.available_tags.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.available_tags.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.available_tags.setObjectName(_fromUtf8("available_tags"))
        self.hboxlayout1.addWidget(self.available_tags)
        self.vboxlayout.addLayout(self.hboxlayout1)
        self.gridlayout.addLayout(self.vboxlayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(DeviceCategoryEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 1, 0, 1, 2)
        self.label.setBuddy(self.available_tags)

        self.retranslateUi(DeviceCategoryEditor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DeviceCategoryEditor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DeviceCategoryEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(DeviceCategoryEditor)

    def retranslateUi(self, DeviceCategoryEditor):
        DeviceCategoryEditor.setWindowTitle(_("Category Editor"))
        self.label.setText(_("Items in use"))
        self.delete_button.setToolTip(_("Delete item from database. This will unapply the item from all books and then remove it from the database."))
        self.delete_button.setText(_("..."))
        self.rename_button.setToolTip(_("Rename the item in every book where it is used."))
        self.rename_button.setText(_("..."))
        self.rename_button.setShortcut(_("Ctrl+S"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/dialogs/choose_library.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(602, 245)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("lt.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.old_location = QtGui.QLabel(Dialog)
        self.old_location.setWordWrap(True)
        self.old_location.setObjectName(_fromUtf8("old_location"))
        self.gridLayout.addWidget(self.old_location, 0, 0, 1, 4)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.existing_library = QtGui.QRadioButton(Dialog)
        self.existing_library.setChecked(True)
        self.existing_library.setObjectName(_fromUtf8("existing_library"))
        self.gridLayout.addWidget(self.existing_library, 4, 0, 1, 4)
        self.hbox1 = QtGui.QHBoxLayout()
        self.hbox1.setObjectName(_fromUtf8("hbox1"))
        self.empty_library = QtGui.QRadioButton(Dialog)
        self.empty_library.setObjectName(_fromUtf8("empty_library"))
        self.hbox1.addWidget(self.empty_library)
        self.copy_structure = QtGui.QCheckBox(Dialog)
        self.copy_structure.setObjectName(_fromUtf8("copy_structure"))
        self.hbox1.addWidget(self.copy_structure)
        self.gridLayout.addLayout(self.hbox1, 5, 0, 1, 3)
        self.move_library = QtGui.QRadioButton(Dialog)
        self.move_library.setObjectName(_fromUtf8("move_library"))
        self.gridLayout.addWidget(self.move_library, 6, 0, 1, 3)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 8, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        self.browse_button = QtGui.QToolButton(Dialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("document_open.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.browse_button.setIcon(icon1)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.gridLayout.addWidget(self.browse_button, 2, 3, 1, 1)
        self.location = HistoryLineEdit(Dialog)
        self.location.setObjectName(_fromUtf8("location"))
        self.gridLayout.addWidget(self.location, 2, 1, 1, 2)
        self.label_2.setBuddy(self.location)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Choose your calibre library"))
        self.old_location.setText(_("Your calibre library is currently located at {0}"))
        self.label_2.setText(_("New &Location:"))
        self.existing_library.setText(_("Use the previously &existing library at the new location"))
        self.empty_library.setText(_("&Create an empty library at the new location"))
        self.copy_structure.setText(_("&Copy structure from the current library"))
        self.copy_structure.setToolTip(_("Copy the custom columns, saved searches, column widths, plugboards,\n"
"user categories, and other information from the old to the new library"))
        self.move_library.setText(_("&Move current library to new location"))
        self.browse_button.setText(_("..."))

from calibre.gui2.widgets import HistoryLineEdit


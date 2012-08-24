# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/dialogs/add_from_isbn.ui'
#
# Created: Thu Jul 19 23:32:31 2012
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
        Dialog.resize(678, 430)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("add_book.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.isbn_box = QtGui.QPlainTextEdit(Dialog)
        self.isbn_box.setObjectName(_fromUtf8("isbn_box"))
        self.verticalLayout_2.addWidget(self.isbn_box)
        self.paste_button = QtGui.QPushButton(Dialog)
        self.paste_button.setObjectName(_fromUtf8("paste_button"))
        self.verticalLayout_2.addWidget(self.paste_button)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 2, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.add_tags = QtGui.QLineEdit(Dialog)
        self.add_tags.setObjectName(_fromUtf8("add_tags"))
        self.verticalLayout.addWidget(self.add_tags)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.label_2.setBuddy(self.add_tags)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Add books by ISBN"))
        self.paste_button.setText(_("&Paste from clipboard"))
        self.label.setText(_("<p>Enter a list of ISBNs in the box to the left, one per line. calibre will automatically create entries for books based on the ISBN and download metadata and covers for them.</p>\n"
"<p>Any invalid ISBNs in the list will be ignored.</p>\n"
"<p>You can also specify a file that will be added with each ISBN. To do this enter the full path to the file after a <code>>></code>.  For example:</p>\n"
"<p><code>9788842915232 >> %s</code></p>"))
        self.label_2.setText(_("&Tags to set on created book entries:"))



# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/dialogs/conversion_error.ui'
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

class Ui_ConversionErrorDialog(object):
    def setupUi(self, ConversionErrorDialog):
        ConversionErrorDialog.setObjectName(_fromUtf8("ConversionErrorDialog"))
        ConversionErrorDialog.resize(658, 515)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("lt.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ConversionErrorDialog.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(ConversionErrorDialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.label = QtGui.QLabel(ConversionErrorDialog)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(I("dialog_error.png"))))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 0, 0, 1, 1)
        self.text = QtGui.QTextBrowser(ConversionErrorDialog)
        self.text.setObjectName(_fromUtf8("text"))
        self.gridlayout.addWidget(self.text, 0, 1, 2, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 1, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ConversionErrorDialog)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 1, 1, 1)

        self.retranslateUi(ConversionErrorDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ConversionErrorDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ConversionErrorDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ConversionErrorDialog)

    def retranslateUi(self, ConversionErrorDialog):
        ConversionErrorDialog.setWindowTitle(_("ERROR"))



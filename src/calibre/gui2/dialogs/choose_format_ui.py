# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/choose_format.ui'
#
# Created: Sat Apr 30 12:56:24 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChooseFormatDialog(object):
    def setupUi(self, ChooseFormatDialog):
        ChooseFormatDialog.setObjectName(_fromUtf8("ChooseFormatDialog"))
        ChooseFormatDialog.resize(507, 377)
        icon = QtGui.QIcon()
        icon.addFile(_fromUtf8(I("mimetypes/unknown.png")))
        ChooseFormatDialog.setWindowIcon(icon)
        self.vboxlayout = QtGui.QVBoxLayout(ChooseFormatDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.msg = QtGui.QLabel(ChooseFormatDialog)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.vboxlayout.addWidget(self.msg)
        self.formats = QtGui.QListWidget(ChooseFormatDialog)
        self.formats.setIconSize(QtCore.QSize(64, 64))
        self.formats.setObjectName(_fromUtf8("formats"))
        self.vboxlayout.addWidget(self.formats)
        self.buttonBox = QtGui.QDialogButtonBox(ChooseFormatDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ChooseFormatDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChooseFormatDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChooseFormatDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseFormatDialog)

    def retranslateUi(self, ChooseFormatDialog):
        ChooseFormatDialog.setWindowTitle(_("Choose Format"))
        self.msg.setText(_("TextLabel"))



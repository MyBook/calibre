# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/dialogs/choose_format_device.ui'
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

class Ui_ChooseFormatDeviceDialog(object):
    def setupUi(self, ChooseFormatDeviceDialog):
        ChooseFormatDeviceDialog.setObjectName(_fromUtf8("ChooseFormatDeviceDialog"))
        ChooseFormatDeviceDialog.resize(507, 377)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("mimetypes/unknown.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ChooseFormatDeviceDialog.setWindowIcon(icon)
        self.vboxlayout = QtGui.QVBoxLayout(ChooseFormatDeviceDialog)
        self.vboxlayout.setObjectName(_fromUtf8("vboxlayout"))
        self.msg = QtGui.QLabel(ChooseFormatDeviceDialog)
        self.msg.setText(_fromUtf8(""))
        self.msg.setObjectName(_fromUtf8("msg"))
        self.vboxlayout.addWidget(self.msg)
        self.formats = QtGui.QTreeWidget(ChooseFormatDeviceDialog)
        self.formats.setAlternatingRowColors(True)
        self.formats.setIconSize(QtCore.QSize(64, 64))
        self.formats.setAllColumnsShowFocus(True)
        self.formats.setObjectName(_fromUtf8("formats"))
        self.formats.headerItem().setTextAlignment(1, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.vboxlayout.addWidget(self.formats)
        self.buttonBox = QtGui.QDialogButtonBox(ChooseFormatDeviceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.vboxlayout.addWidget(self.buttonBox)

        self.retranslateUi(ChooseFormatDeviceDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ChooseFormatDeviceDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ChooseFormatDeviceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ChooseFormatDeviceDialog)

    def retranslateUi(self, ChooseFormatDeviceDialog):
        ChooseFormatDeviceDialog.setWindowTitle(_("Choose Format"))
        self.formats.headerItem().setText(0, _("Format"))
        self.formats.headerItem().setText(1, _("Existing"))
        self.formats.headerItem().setText(2, _("Convertible"))



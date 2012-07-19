# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/password.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(350, 209)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("mimetypes/unknown.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(Dialog)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.msg = QtGui.QLabel(Dialog)
        self.msg.setWordWrap(True)
        self.msg.setOpenExternalLinks(True)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.gridlayout.addWidget(self.msg, 0, 1, 1, 1)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout.addWidget(self.label, 1, 0, 1, 1)
        self.gui_username = QtGui.QLineEdit(Dialog)
        self.gui_username.setObjectName(_fromUtf8("gui_username"))
        self.gridlayout.addWidget(self.gui_username, 1, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.gui_password = QtGui.QLineEdit(Dialog)
        self.gui_password.setEchoMode(QtGui.QLineEdit.Password)
        self.gui_password.setObjectName(_fromUtf8("gui_password"))
        self.gridlayout.addWidget(self.gui_password, 2, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.show_password = QtGui.QCheckBox(Dialog)
        self.show_password.setObjectName(_fromUtf8("show_password"))
        self.gridlayout.addWidget(self.show_password, 3, 1, 1, 1)
        self.label.setBuddy(self.gui_username)
        self.label_2.setBuddy(self.gui_password)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Password needed"))
        self.msg.setText(_("TextLabel"))
        self.label.setText(_("&Username:"))
        self.label_2.setText(_("&Password:"))
        self.show_password.setText(_("&Show password"))



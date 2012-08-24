# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/store/web_store_dialog.ui'
#
# Created: Thu Jul 19 23:32:29 2012
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
        Dialog.resize(962, 656)
        Dialog.setWindowTitle(_fromUtf8(""))
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.view = NPWebView(self.frame)
        self.view.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.view.setObjectName(_fromUtf8("view"))
        self.verticalLayout.addWidget(self.view)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 5)
        self.home = QtGui.QPushButton(Dialog)
        self.home.setObjectName(_fromUtf8("home"))
        self.gridLayout.addWidget(self.home, 1, 0, 1, 1)
        self.reload = QtGui.QPushButton(Dialog)
        self.reload.setObjectName(_fromUtf8("reload"))
        self.gridLayout.addWidget(self.reload, 1, 1, 1, 1)
        self.progress = QtGui.QProgressBar(Dialog)
        self.progress.setProperty("value", 0)
        self.progress.setObjectName(_fromUtf8("progress"))
        self.gridLayout.addWidget(self.progress, 1, 3, 1, 1)
        self.back = QtGui.QPushButton(Dialog)
        self.back.setObjectName(_fromUtf8("back"))
        self.gridLayout.addWidget(self.back, 1, 2, 1, 1)
        self.close = QtGui.QPushButton(Dialog)
        self.close.setObjectName(_fromUtf8("close"))
        self.gridLayout.addWidget(self.close, 1, 4, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        self.home.setText(_("Home"))
        self.reload.setText(_("Reload"))
        self.progress.setFormat(_("%p%"))
        self.back.setText(_("Back"))
        self.close.setText(_("Close"))

from web_control import NPWebView

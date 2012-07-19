# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/delete_matching_from_device.ui'
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

class Ui_DeleteMatchingFromDeviceDialog(object):
    def setupUi(self, DeleteMatchingFromDeviceDialog):
        DeleteMatchingFromDeviceDialog.setObjectName(_fromUtf8("DeleteMatchingFromDeviceDialog"))
        DeleteMatchingFromDeviceDialog.resize(730, 342)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DeleteMatchingFromDeviceDialog.sizePolicy().hasHeightForWidth())
        DeleteMatchingFromDeviceDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(DeleteMatchingFromDeviceDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.explanation = QtGui.QLabel(DeleteMatchingFromDeviceDialog)
        self.explanation.setObjectName(_fromUtf8("explanation"))
        self.verticalLayout.addWidget(self.explanation)
        self.table = QtGui.QTableWidget(DeleteMatchingFromDeviceDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setColumnCount(0)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.buttonBox = QtGui.QDialogButtonBox(DeleteMatchingFromDeviceDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DeleteMatchingFromDeviceDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DeleteMatchingFromDeviceDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DeleteMatchingFromDeviceDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(DeleteMatchingFromDeviceDialog)

    def retranslateUi(self, DeleteMatchingFromDeviceDialog):
        DeleteMatchingFromDeviceDialog.setWindowTitle(_("Delete from device"))


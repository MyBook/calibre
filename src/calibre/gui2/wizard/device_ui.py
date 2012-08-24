# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/wizard/device.ui'
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

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("wizard.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        WizardPage.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(WizardPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(WizardPage)
        self.label.setText(_fromUtf8(""))
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(WizardPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.manufacturer_view = QtGui.QListView(self.groupBox)
        self.manufacturer_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.manufacturer_view.setObjectName(_fromUtf8("manufacturer_view"))
        self.verticalLayout.addWidget(self.manufacturer_view)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(WizardPage)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.device_view = QtGui.QListView(self.groupBox_2)
        self.device_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.device_view.setObjectName(_fromUtf8("device_view"))
        self.verticalLayout_2.addWidget(self.device_view)
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_("Welcome to calibre"))
        WizardPage.setTitle(_("Welcome to calibre"))
        WizardPage.setSubTitle(_("The one stop solution to all your e-book needs."))
        self.groupBox.setTitle(_("&Manufacturers"))
        self.groupBox_2.setTitle(_("&Devices"))



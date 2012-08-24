# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/wizard/library.ui'
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
        WizardPage.resize(481, 300)
        self.gridLayout = QtGui.QGridLayout(WizardPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(WizardPage)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.language = QtGui.QComboBox(WizardPage)
        self.language.setObjectName(_fromUtf8("language"))
        self.gridLayout.addWidget(self.language, 0, 1, 1, 2)
        self.libloc_label1 = QtGui.QLabel(WizardPage)
        self.libloc_label1.setWordWrap(True)
        self.libloc_label1.setObjectName(_fromUtf8("libloc_label1"))
        self.gridLayout.addWidget(self.libloc_label1, 2, 0, 1, 3)
        self.location = QtGui.QLineEdit(WizardPage)
        self.location.setReadOnly(True)
        self.location.setObjectName(_fromUtf8("location"))
        self.gridLayout.addWidget(self.location, 3, 0, 1, 2)
        self.button_change = QtGui.QPushButton(WizardPage)
        self.button_change.setObjectName(_fromUtf8("button_change"))
        self.gridLayout.addWidget(self.button_change, 3, 2, 1, 1)
        self.libloc_label2 = QtGui.QLabel(WizardPage)
        self.libloc_label2.setWordWrap(True)
        self.libloc_label2.setObjectName(_fromUtf8("libloc_label2"))
        self.gridLayout.addWidget(self.libloc_label2, 4, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.label_3.setBuddy(self.language)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_("WizardPage"))
        WizardPage.setTitle(_("Welcome to calibre"))
        WizardPage.setSubTitle(_("The one stop solution to all your e-book needs."))
        self.label_3.setText(_("Choose your &language:"))
        self.libloc_label1.setText(_("<p>Choose a location for your books. When you add books to calibre, they will be copied here. Use an <b>empty folder</b> for a new calibre library:"))
        self.button_change.setText(_("&Change"))
        self.libloc_label2.setText(_("If you have an existing calibre library, it will be copied to the new location. If a calibre library already exists at the new location, calibre will switch to using it."))


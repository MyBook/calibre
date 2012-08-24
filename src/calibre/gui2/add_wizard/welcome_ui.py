# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/add_wizard/welcome.ui'
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

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(704, 468)
        self.gridLayout = QtGui.QGridLayout(WizardPage)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(WizardPage)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.label_2 = QtGui.QLabel(WizardPage)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.opt_root_folder = QtGui.QLineEdit(WizardPage)
        self.opt_root_folder.setObjectName(_fromUtf8("opt_root_folder"))
        self.gridLayout.addWidget(self.opt_root_folder, 2, 1, 1, 1)
        self.button_choose_root_folder = QtGui.QToolButton(WizardPage)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("document_open.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_choose_root_folder.setIcon(icon)
        self.button_choose_root_folder.setObjectName(_fromUtf8("button_choose_root_folder"))
        self.gridLayout.addWidget(self.button_choose_root_folder, 2, 2, 1, 1)
        self.groupBox = QtGui.QGroupBox(WizardPage)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.opt_one_per_folder = QtGui.QRadioButton(self.groupBox)
        self.opt_one_per_folder.setObjectName(_fromUtf8("opt_one_per_folder"))
        self.verticalLayout.addWidget(self.opt_one_per_folder)
        self.opt_many_per_folder = QtGui.QRadioButton(self.groupBox)
        self.opt_many_per_folder.setObjectName(_fromUtf8("opt_many_per_folder"))
        self.verticalLayout.addWidget(self.opt_many_per_folder)
        self.gridLayout.addWidget(self.groupBox, 4, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        self.label_2.setBuddy(self.opt_root_folder)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_("WizardPage"))
        WizardPage.setTitle(_("Choose the location to add books from"))
        WizardPage.setSubTitle(_("Select a folder on your hard disk"))
        self.label.setText(_("<p>calibre can scan your computer for existing books automatically. These books will then be <b>copied</b> into the calibre library. This wizard will help you customize the scanning and import process for your existing book collection.</p>\n"
"<p>Choose a root folder. Books will be searched for only inside this folder and any sub-folders.</p>\n"
"<p>Make sure that the folder you chose for your calibre library <b>is not</b> under the root folder you choose.</p>"))
        self.label_2.setText(_("&Root folder:"))
        self.opt_root_folder.setToolTip(_("This folder and its sub-folders will be scanned for books to import into calibre\'s library"))
        self.button_choose_root_folder.setToolTip(_("Choose root folder"))
        self.button_choose_root_folder.setText(_("..."))
        self.groupBox.setTitle(_("Handle multiple files per book"))
        self.opt_one_per_folder.setText(_("&One book per folder, assumes every ebook file in a folder is the same book in a different format"))
        self.opt_many_per_folder.setText(_("&Multiple books per folder, assumes every ebook file is a different book"))



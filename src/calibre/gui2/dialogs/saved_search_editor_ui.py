# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/saved_search_editor.ui'
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

class Ui_SavedSearchEditor(object):
    def setupUi(self, SavedSearchEditor):
        SavedSearchEditor.setObjectName(_fromUtf8("SavedSearchEditor"))
        SavedSearchEditor.resize(548, 148)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("chapters.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SavedSearchEditor.setWindowIcon(icon)
        self.gridlayout = QtGui.QGridLayout(SavedSearchEditor)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.buttonBox = QtGui.QDialogButtonBox(SavedSearchEditor)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 2, 0, 1, 2)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(SavedSearchEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(100, 0))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.search_name_box = QtGui.QComboBox(SavedSearchEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(160)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_name_box.sizePolicy().hasHeightForWidth())
        self.search_name_box.setSizePolicy(sizePolicy)
        self.search_name_box.setMinimumSize(QtCore.QSize(145, 0))
        self.search_name_box.setEditable(False)
        self.search_name_box.setObjectName(_fromUtf8("search_name_box"))
        self.gridLayout.addWidget(self.search_name_box, 0, 1, 1, 1)
        self.delete_search_button = QtGui.QToolButton(SavedSearchEditor)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("trash.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_search_button.setIcon(icon1)
        self.delete_search_button.setObjectName(_fromUtf8("delete_search_button"))
        self.gridLayout.addWidget(self.delete_search_button, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.input_box = QtGui.QLineEdit(SavedSearchEditor)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(60)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_box.sizePolicy().hasHeightForWidth())
        self.input_box.setSizePolicy(sizePolicy)
        self.input_box.setObjectName(_fromUtf8("input_box"))
        self.gridLayout.addWidget(self.input_box, 0, 4, 1, 1)
        self.add_search_button = QtGui.QToolButton(SavedSearchEditor)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("plus.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_search_button.setIcon(icon2)
        self.add_search_button.setObjectName(_fromUtf8("add_search_button"))
        self.gridLayout.addWidget(self.add_search_button, 0, 5, 1, 1)
        self.rename_button = QtGui.QToolButton(SavedSearchEditor)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(I("edit-undo.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rename_button.setIcon(icon3)
        self.rename_button.setObjectName(_fromUtf8("rename_button"))
        self.gridLayout.addWidget(self.rename_button, 0, 6, 1, 1)
        self.gridlayout.addLayout(self.gridLayout, 0, 0, 1, 2)
        self.search_text = QtGui.QPlainTextEdit(SavedSearchEditor)
        self.search_text.setObjectName(_fromUtf8("search_text"))
        self.gridlayout.addWidget(self.search_text, 1, 0, 1, 1)
        self.label_3.setBuddy(self.search_name_box)

        self.retranslateUi(SavedSearchEditor)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SavedSearchEditor.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SavedSearchEditor.reject)
        QtCore.QMetaObject.connectSlotsByName(SavedSearchEditor)

    def retranslateUi(self, SavedSearchEditor):
        SavedSearchEditor.setWindowTitle(_("Saved Search Editor"))
        self.label_3.setText(_("Saved Search: "))
        self.search_name_box.setToolTip(_("Select a saved search to edit"))
        self.delete_search_button.setToolTip(_("Delete this selected saved search"))
        self.delete_search_button.setText(_("..."))
        self.input_box.setToolTip(_("Enter a new saved search name."))
        self.add_search_button.setToolTip(_("Add the new saved search"))
        self.add_search_button.setText(_("..."))
        self.rename_button.setToolTip(_("Rename the current search to what is in the box"))
        self.rename_button.setText(_("..."))
        self.search_text.setToolTip(_("Change the contents of the saved search"))


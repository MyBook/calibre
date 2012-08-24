# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/dialogs/edit_authors_dialog.ui'
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

class Ui_EditAuthorsDialog(object):
    def setupUi(self, EditAuthorsDialog):
        EditAuthorsDialog.setObjectName(_fromUtf8("EditAuthorsDialog"))
        EditAuthorsDialog.resize(768, 342)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(EditAuthorsDialog.sizePolicy().hasHeightForWidth())
        EditAuthorsDialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtGui.QVBoxLayout(EditAuthorsDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.label = QtGui.QLabel(EditAuthorsDialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.find_box = HistoryLineEdit(EditAuthorsDialog)
        self.find_box.setMinimumSize(QtCore.QSize(200, 0))
        self.find_box.setObjectName(_fromUtf8("find_box"))
        self.hboxlayout.addWidget(self.find_box)
        self.find_button = QtGui.QPushButton(EditAuthorsDialog)
        self.find_button.setObjectName(_fromUtf8("find_button"))
        self.hboxlayout.addWidget(self.find_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.hboxlayout)
        self.table = QtGui.QTableWidget(EditAuthorsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setColumnCount(0)
        self.table.setObjectName(_fromUtf8("table"))
        self.table.setRowCount(0)
        self.verticalLayout.addWidget(self.table)
        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.sort_by_author = QtGui.QPushButton(EditAuthorsDialog)
        self.sort_by_author.setObjectName(_fromUtf8("sort_by_author"))
        self.gridlayout.addWidget(self.sort_by_author, 0, 0, 1, 1)
        self.sort_by_author_sort = QtGui.QPushButton(EditAuthorsDialog)
        self.sort_by_author_sort.setObjectName(_fromUtf8("sort_by_author_sort"))
        self.gridlayout.addWidget(self.sort_by_author_sort, 0, 1, 1, 1)
        self.recalc_author_sort = QtGui.QPushButton(EditAuthorsDialog)
        self.recalc_author_sort.setObjectName(_fromUtf8("recalc_author_sort"))
        self.gridlayout.addWidget(self.recalc_author_sort, 1, 0, 1, 1)
        self.auth_sort_to_author = QtGui.QPushButton(EditAuthorsDialog)
        self.auth_sort_to_author.setObjectName(_fromUtf8("auth_sort_to_author"))
        self.gridlayout.addWidget(self.auth_sort_to_author, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(EditAuthorsDialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridlayout.addWidget(self.buttonBox, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridlayout)
        self.label.setBuddy(self.find_box)

        self.retranslateUi(EditAuthorsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), EditAuthorsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), EditAuthorsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(EditAuthorsDialog)

    def retranslateUi(self, EditAuthorsDialog):
        EditAuthorsDialog.setWindowTitle(_("Manage authors"))
        self.label.setText(_("&Search for:"))
        self.find_button.setText(_("F&ind"))
        self.sort_by_author.setText(_("Sort by author"))
        self.sort_by_author_sort.setText(_("Sort by author sort"))
        self.recalc_author_sort.setToolTip(_("Reset all the author sort values to a value automatically\n"
"generated from the author. Exactly how this value is automatically\n"
"generated can be controlled via Preferences->Advanced->Tweaks"))
        self.recalc_author_sort.setText(_("Recalculate all author sort values"))
        self.auth_sort_to_author.setToolTip(_("Copy author sort to author for every author. You typically use this button\n"
"after changing Preferences->Advanced->Tweaks->Author sort name algorithm"))
        self.auth_sort_to_author.setText(_("Copy all author sort values to author"))

from calibre.gui2.widgets import HistoryLineEdit

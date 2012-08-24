# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/store/stores/mobileread/store_dialog.ui'
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
        Dialog.resize(691, 614)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.adv_search_button = QtGui.QToolButton(Dialog)
        self.adv_search_button.setObjectName(_fromUtf8("adv_search_button"))
        self.horizontalLayout_2.addWidget(self.adv_search_button)
        self.search_query = HistoryLineEdit(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_query.sizePolicy().hasHeightForWidth())
        self.search_query.setSizePolicy(sizePolicy)
        self.search_query.setObjectName(_fromUtf8("search_query"))
        self.horizontalLayout_2.addWidget(self.search_query)
        self.search_button = QtGui.QPushButton(Dialog)
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.horizontalLayout_2.addWidget(self.search_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.results_view = QtGui.QTreeView(Dialog)
        self.results_view.setAlternatingRowColors(True)
        self.results_view.setRootIsDecorated(False)
        self.results_view.setItemsExpandable(False)
        self.results_view.setSortingEnabled(True)
        self.results_view.setExpandsOnDoubleClick(False)
        self.results_view.setObjectName(_fromUtf8("results_view"))
        self.results_view.header().setCascadingSectionResizes(False)
        self.verticalLayout.addWidget(self.results_view)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.total = QtGui.QLabel(Dialog)
        self.total.setObjectName(_fromUtf8("total"))
        self.horizontalLayout.addWidget(self.total)
        spacerItem = QtGui.QSpacerItem(308, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_button = QtGui.QPushButton(Dialog)
        self.close_button.setObjectName(_fromUtf8("close_button"))
        self.horizontalLayout.addWidget(self.close_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label.setBuddy(self.search_query)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.close_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Dialog"))
        self.label.setText(_("&Query:"))
        self.adv_search_button.setText(_("..."))
        self.search_button.setText(_("Search"))
        self.label_2.setText(_("Books:"))
        self.total.setText(_("0"))
        self.close_button.setText(_("Close"))

from calibre.gui2.widgets import HistoryLineEdit

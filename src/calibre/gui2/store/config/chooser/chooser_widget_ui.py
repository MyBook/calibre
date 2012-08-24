# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/store/config/chooser/chooser_widget.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(610, 553)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.adv_search_builder = QtGui.QToolButton(Form)
        self.adv_search_builder.setObjectName(_fromUtf8("adv_search_builder"))
        self.horizontalLayout.addWidget(self.adv_search_builder)
        self.query = HistoryLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.query.sizePolicy().hasHeightForWidth())
        self.query.setSizePolicy(sizePolicy)
        self.query.setObjectName(_fromUtf8("query"))
        self.horizontalLayout.addWidget(self.query)
        self.search = QtGui.QPushButton(Form)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout.addWidget(self.search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.results_view = ResultsView(Form)
        self.results_view.setAlternatingRowColors(True)
        self.results_view.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.results_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.results_view.setRootIsDecorated(False)
        self.results_view.setUniformRowHeights(True)
        self.results_view.setItemsExpandable(False)
        self.results_view.setSortingEnabled(True)
        self.results_view.setExpandsOnDoubleClick(False)
        self.results_view.setObjectName(_fromUtf8("results_view"))
        self.results_view.header().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.results_view)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.enable_all = QtGui.QPushButton(Form)
        self.enable_all.setObjectName(_fromUtf8("enable_all"))
        self.horizontalLayout_2.addWidget(self.enable_all)
        self.enable_none = QtGui.QPushButton(Form)
        self.enable_none.setObjectName(_fromUtf8("enable_none"))
        self.horizontalLayout_2.addWidget(self.enable_none)
        self.enable_invert = QtGui.QPushButton(Form)
        self.enable_invert.setObjectName(_fromUtf8("enable_invert"))
        self.horizontalLayout_2.addWidget(self.enable_invert)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("Query:"))
        self.adv_search_builder.setText(_("..."))
        self.search.setText(_("Search"))
        self.label_2.setText(_("Enable"))
        self.enable_all.setText(_("All"))
        self.enable_none.setText(_("None"))
        self.enable_invert.setText(_("Invert"))

from calibre.gui2.widgets import HistoryLineEdit
from results_view import ResultsView

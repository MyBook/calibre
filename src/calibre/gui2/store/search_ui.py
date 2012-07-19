# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/store/search.ui'
#
# Created: Thu Apr 21 18:43:12 2011
#      by: PyQt4 UI code generator 4.8.3
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
        Dialog.resize(937, 669)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("store.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.search_edit = QtGui.QLineEdit(Dialog)
        self.search_edit.setObjectName(_fromUtf8("search_edit"))
        self.horizontalLayout_2.addWidget(self.search_edit)
        self.search = QtGui.QPushButton(Dialog)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout_2.addWidget(self.search)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.store_splitter = QtGui.QSplitter(Dialog)
        self.store_splitter.setOrientation(QtCore.Qt.Horizontal)
        self.store_splitter.setObjectName(_fromUtf8("store_splitter"))
        self.groupBox = QtGui.QGroupBox(self.store_splitter)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.stores_group = QtGui.QScrollArea(self.groupBox)
        self.stores_group.setWidgetResizable(True)
        self.stores_group.setObjectName(_fromUtf8("stores_group"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 170, 138))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.stores_group.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.stores_group)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.select_all_stores = QtGui.QPushButton(self.groupBox)
        self.select_all_stores.setObjectName(_fromUtf8("select_all_stores"))
        self.horizontalLayout_3.addWidget(self.select_all_stores)
        self.select_invert_stores = QtGui.QPushButton(self.groupBox)
        self.select_invert_stores.setObjectName(_fromUtf8("select_invert_stores"))
        self.horizontalLayout_3.addWidget(self.select_invert_stores)
        self.select_none_stores = QtGui.QPushButton(self.groupBox)
        self.select_none_stores.setObjectName(_fromUtf8("select_none_stores"))
        self.horizontalLayout_3.addWidget(self.select_none_stores)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.splitter_2 = QtGui.QSplitter(self.store_splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.results_view = QtGui.QTreeView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.results_view.sizePolicy().hasHeightForWidth())
        self.results_view.setSizePolicy(sizePolicy)
        self.results_view.setMinimumSize(QtCore.QSize(0, 0))
        self.results_view.setAlternatingRowColors(True)
        self.results_view.setIconSize(QtCore.QSize(32, 32))
        self.results_view.setRootIsDecorated(False)
        self.results_view.setUniformRowHeights(False)
        self.results_view.setItemsExpandable(False)
        self.results_view.setSortingEnabled(True)
        self.results_view.setExpandsOnDoubleClick(False)
        self.results_view.setObjectName(_fromUtf8("results_view"))
        self.verticalLayout.addWidget(self.store_splitter)
        self.bottom_layout = QtGui.QHBoxLayout()
        self.bottom_layout.setObjectName(_fromUtf8("bottom_layout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.bottom_layout.addItem(spacerItem)
        self.close = QtGui.QPushButton(Dialog)
        self.close.setObjectName(_fromUtf8("close"))
        self.bottom_layout.addWidget(self.close)
        self.verticalLayout.addLayout(self.bottom_layout)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.close, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Get Books"))
        self.label.setText(_("Query:"))
        self.search.setText(_("Search"))
        self.groupBox.setTitle(_("Stores"))
        self.select_all_stores.setText(_("All"))
        self.select_invert_stores.setText(_("Invert"))
        self.select_none_stores.setText(_("None"))
        self.close.setText(_("Close"))



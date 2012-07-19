# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/device_drivers/configwidget.ui'
#
# Created: Mon May  2 11:18:02 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ConfigWidget(object):
    def setupUi(self, ConfigWidget):
        ConfigWidget.setObjectName(_fromUtf8("ConfigWidget"))
        ConfigWidget.resize(442, 332)
        self.gridLayout = QtGui.QGridLayout(ConfigWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(ConfigWidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.columns = QtGui.QListWidget(self.groupBox)
        self.columns.setAlternatingRowColors(True)
        self.columns.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.columns.setObjectName(_fromUtf8("columns"))
        self.horizontalLayout_3.addWidget(self.columns)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.column_up = QtGui.QToolButton(self.groupBox)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-up.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.column_up.setIcon(icon)
        self.column_up.setObjectName(_fromUtf8("column_up"))
        self.verticalLayout_3.addWidget(self.column_up)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.column_down = QtGui.QToolButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-down.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.column_down.setIcon(icon1)
        self.column_down.setObjectName(_fromUtf8("column_down"))
        self.verticalLayout_3.addWidget(self.column_down)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.opt_read_metadata = QtGui.QCheckBox(ConfigWidget)
        self.opt_read_metadata.setObjectName(_fromUtf8("opt_read_metadata"))
        self.gridLayout.addWidget(self.opt_read_metadata, 1, 0, 1, 1)
        self.opt_use_subdirs = QtGui.QCheckBox(ConfigWidget)
        self.opt_use_subdirs.setObjectName(_fromUtf8("opt_use_subdirs"))
        self.gridLayout.addWidget(self.opt_use_subdirs, 2, 0, 1, 1)
        self.opt_use_author_sort = QtGui.QCheckBox(ConfigWidget)
        self.opt_use_author_sort.setObjectName(_fromUtf8("opt_use_author_sort"))
        self.gridLayout.addWidget(self.opt_use_author_sort, 3, 0, 1, 1)
        self.extra_layout = QtGui.QGridLayout()
        self.extra_layout.setObjectName(_fromUtf8("extra_layout"))
        self.gridLayout.addLayout(self.extra_layout, 6, 0, 1, 1)
        self.label = QtGui.QLabel(ConfigWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.opt_save_template = QtGui.QLineEdit(ConfigWidget)
        self.opt_save_template.setObjectName(_fromUtf8("opt_save_template"))
        self.gridLayout.addWidget(self.opt_save_template, 5, 0, 1, 1)
        self.label.setBuddy(self.opt_save_template)

        self.retranslateUi(ConfigWidget)
        QtCore.QMetaObject.connectSlotsByName(ConfigWidget)

    def retranslateUi(self, ConfigWidget):
        ConfigWidget.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Select available formats and their order for this device"))
        self.column_up.setText(_("..."))
        self.column_down.setText(_("..."))
        self.opt_read_metadata.setText(_("Read metadata from files on device"))
        self.opt_use_subdirs.setToolTip(_("If checked, books are placed into sub directories based on their metadata on the device. If unchecked, books are all put into the top level directory."))
        self.opt_use_subdirs.setText(_("Use sub directories"))
        self.opt_use_author_sort.setText(_("Use author sort for author"))
        self.label.setText(_("Save &template:"))



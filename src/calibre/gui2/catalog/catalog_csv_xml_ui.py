# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/catalog/catalog_csv_xml.ui'
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
        Form.resize(579, 411)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.db_fields = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_fields.sizePolicy().hasHeightForWidth())
        self.db_fields.setSizePolicy(sizePolicy)
        self.db_fields.setToolTip(_fromUtf8(""))
        self.db_fields.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.db_fields.setObjectName(_fromUtf8("db_fields"))
        self.gridLayout.addWidget(self.db_fields, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_6.setText(_("Fields to include in output:"))


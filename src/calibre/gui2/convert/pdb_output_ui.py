# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/pdb_output.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.opt_format = QtGui.QComboBox(Form)
        self.opt_format.setObjectName(_fromUtf8("opt_format"))
        self.gridLayout.addWidget(self.opt_format, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(148, 246, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.opt_inline_toc = QtGui.QCheckBox(Form)
        self.opt_inline_toc.setObjectName(_fromUtf8("opt_inline_toc"))
        self.gridLayout.addWidget(self.opt_inline_toc, 2, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.opt_pdb_output_encoding = EncodingComboBox(Form)
        self.opt_pdb_output_encoding.setEditable(True)
        self.opt_pdb_output_encoding.setObjectName(_fromUtf8("opt_pdb_output_encoding"))
        self.gridLayout.addWidget(self.opt_pdb_output_encoding, 1, 1, 1, 1)
        self.label.setBuddy(self.opt_format)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("&Format:"))
        self.opt_inline_toc.setText(_("&Inline TOC"))
        self.label_2.setText(_("Output Encoding:"))

from calibre.gui2.widgets import EncodingComboBox

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/pmlz_output.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 246, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.opt_inline_toc = QtGui.QCheckBox(Form)
        self.opt_inline_toc.setObjectName(_fromUtf8("opt_inline_toc"))
        self.gridLayout.addWidget(self.opt_inline_toc, 2, 0, 1, 1)
        self.opt_full_image_depth = QtGui.QCheckBox(Form)
        self.opt_full_image_depth.setObjectName(_fromUtf8("opt_full_image_depth"))
        self.gridLayout.addWidget(self.opt_full_image_depth, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.opt_pml_output_encoding = EncodingComboBox(Form)
        self.opt_pml_output_encoding.setEditable(True)
        self.opt_pml_output_encoding.setObjectName(_fromUtf8("opt_pml_output_encoding"))
        self.horizontalLayout.addWidget(self.opt_pml_output_encoding)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_inline_toc.setText(_("&Inline TOC"))
        self.opt_full_image_depth.setText(_("Do not reduce image size and depth"))
        self.label.setText(_("Output Encoding:"))

from calibre.gui2.widgets import EncodingComboBox

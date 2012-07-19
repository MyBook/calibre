# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/pdb_input.ui'
#
# Created: Thu Jan  6 09:21:30 2011
#      by: PyQt4 UI code generator 4.8.2
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
        spacerItem = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.opt_single_line_paras = QtGui.QCheckBox(Form)
        self.opt_single_line_paras.setObjectName(_fromUtf8("opt_single_line_paras"))
        self.gridLayout.addWidget(self.opt_single_line_paras, 0, 0, 1, 1)
        self.opt_print_formatted_paras = QtGui.QCheckBox(Form)
        self.opt_print_formatted_paras.setObjectName(_fromUtf8("opt_print_formatted_paras"))
        self.gridLayout.addWidget(self.opt_print_formatted_paras, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_single_line_paras.setText(_("Treat each &line as a paragraph"))
        self.opt_print_formatted_paras.setText(_("Assume print formatting"))


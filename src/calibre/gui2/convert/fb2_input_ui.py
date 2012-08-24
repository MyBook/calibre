# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/fb2_input.ui'
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
        spacerItem = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.opt_no_inline_fb2_toc = QtGui.QCheckBox(Form)
        self.opt_no_inline_fb2_toc.setObjectName(_fromUtf8("opt_no_inline_fb2_toc"))
        self.gridLayout.addWidget(self.opt_no_inline_fb2_toc, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_no_inline_fb2_toc.setText(_("Do not insert a &Table of Contents at the beginning of the book."))


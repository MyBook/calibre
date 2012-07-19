# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/snb_output.ui'
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
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)
        self.opt_snb_hide_chapter_name = QtGui.QCheckBox(Form)
        self.opt_snb_hide_chapter_name.setObjectName(_fromUtf8("opt_snb_hide_chapter_name"))
        self.gridLayout.addWidget(self.opt_snb_hide_chapter_name, 3, 0, 1, 1)
        self.opt_snb_dont_indent_first_line = QtGui.QCheckBox(Form)
        self.opt_snb_dont_indent_first_line.setObjectName(_fromUtf8("opt_snb_dont_indent_first_line"))
        self.gridLayout.addWidget(self.opt_snb_dont_indent_first_line, 2, 0, 1, 1)
        self.opt_snb_insert_empty_line = QtGui.QCheckBox(Form)
        self.opt_snb_insert_empty_line.setObjectName(_fromUtf8("opt_snb_insert_empty_line"))
        self.gridLayout.addWidget(self.opt_snb_insert_empty_line, 1, 0, 1, 1)
        self.opt_snb_full_screen = QtGui.QCheckBox(Form)
        self.opt_snb_full_screen.setObjectName(_fromUtf8("opt_snb_full_screen"))
        self.gridLayout.addWidget(self.opt_snb_full_screen, 4, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_snb_hide_chapter_name.setText(_("Hide chapter name"))
        self.opt_snb_dont_indent_first_line.setText(_("Don\'t indent the first line for each paragraph"))
        self.opt_snb_insert_empty_line.setText(_("Insert empty line between paragraphs"))
        self.opt_snb_full_screen.setText(_("Optimize for full-sceen view "))


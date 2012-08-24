# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/htmlz_output.ui'
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
        Form.resize(438, 300)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 246, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.opt_htmlz_class_style = QtGui.QComboBox(Form)
        self.opt_htmlz_class_style.setObjectName(_fromUtf8("opt_htmlz_class_style"))
        self.gridLayout.addWidget(self.opt_htmlz_class_style, 1, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.opt_htmlz_css_type = QtGui.QComboBox(Form)
        self.opt_htmlz_css_type.setMinimumContentsLength(20)
        self.opt_htmlz_css_type.setObjectName(_fromUtf8("opt_htmlz_css_type"))
        self.gridLayout.addWidget(self.opt_htmlz_css_type, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.opt_htmlz_title_filename = QtGui.QCheckBox(Form)
        self.opt_htmlz_title_filename.setObjectName(_fromUtf8("opt_htmlz_title_filename"))
        self.gridLayout.addWidget(self.opt_htmlz_title_filename, 2, 0, 1, 2)
        self.label.setBuddy(self.opt_htmlz_css_type)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("How to handle CSS"))
        self.label_2.setText(_("How to handle class based CSS"))
        self.opt_htmlz_title_filename.setText(_("Use book &title as the filename for the HTML file inside the archive"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/pdf_input.ui'
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
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.opt_unwrap_factor = QtGui.QDoubleSpinBox(Form)
        self.opt_unwrap_factor.setMaximum(1.0)
        self.opt_unwrap_factor.setSingleStep(0.01)
        self.opt_unwrap_factor.setProperty("value", 0.45)
        self.opt_unwrap_factor.setObjectName(_fromUtf8("opt_unwrap_factor"))
        self.gridLayout.addWidget(self.opt_unwrap_factor, 0, 1, 1, 1)
        self.opt_no_images = QtGui.QCheckBox(Form)
        self.opt_no_images.setObjectName(_fromUtf8("opt_no_images"))
        self.gridLayout.addWidget(self.opt_no_images, 1, 0, 1, 1)
        self.label_2.setBuddy(self.opt_unwrap_factor)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_2.setText(_("Line &Un-Wrapping Factor:"))
        self.opt_no_images.setText(_("No &Images"))


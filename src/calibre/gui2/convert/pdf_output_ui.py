# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/pdf_output.ui'
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
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.opt_paper_size = QtGui.QComboBox(Form)
        self.opt_paper_size.setObjectName(_fromUtf8("opt_paper_size"))
        self.gridLayout.addWidget(self.opt_paper_size, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.opt_orientation = QtGui.QComboBox(Form)
        self.opt_orientation.setObjectName(_fromUtf8("opt_orientation"))
        self.gridLayout.addWidget(self.opt_orientation, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.opt_preserve_cover_aspect_ratio = QtGui.QCheckBox(Form)
        self.opt_preserve_cover_aspect_ratio.setObjectName(_fromUtf8("opt_preserve_cover_aspect_ratio"))
        self.gridLayout.addWidget(self.opt_preserve_cover_aspect_ratio, 3, 0, 1, 2)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.opt_custom_size = QtGui.QLineEdit(Form)
        self.opt_custom_size.setObjectName(_fromUtf8("opt_custom_size"))
        self.gridLayout.addWidget(self.opt_custom_size, 2, 1, 1, 1)
        self.label.setBuddy(self.opt_paper_size)
        self.label_2.setBuddy(self.opt_orientation)
        self.label_3.setBuddy(self.opt_custom_size)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("&Paper Size:"))
        self.label_2.setText(_("&Orientation:"))
        self.opt_preserve_cover_aspect_ratio.setText(_("Preserve &aspect ratio of cover"))
        self.label_3.setText(_("&Custom size:"))


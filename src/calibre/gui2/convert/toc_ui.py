# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/toc.ui'
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
        Form.resize(436, 382)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.opt_no_chapters_in_toc = QtGui.QCheckBox(Form)
        self.opt_no_chapters_in_toc.setObjectName(_fromUtf8("opt_no_chapters_in_toc"))
        self.gridLayout.addWidget(self.opt_no_chapters_in_toc, 1, 0, 1, 2)
        self.label_10 = QtGui.QLabel(Form)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.opt_max_toc_links = QtGui.QSpinBox(Form)
        self.opt_max_toc_links.setMaximum(10000)
        self.opt_max_toc_links.setObjectName(_fromUtf8("opt_max_toc_links"))
        self.gridLayout.addWidget(self.opt_max_toc_links, 3, 1, 1, 1)
        self.label_16 = QtGui.QLabel(Form)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout.addWidget(self.label_16, 4, 0, 1, 1)
        self.opt_toc_threshold = QtGui.QSpinBox(Form)
        self.opt_toc_threshold.setObjectName(_fromUtf8("opt_toc_threshold"))
        self.gridLayout.addWidget(self.opt_toc_threshold, 4, 1, 1, 1)
        self.opt_use_auto_toc = QtGui.QCheckBox(Form)
        self.opt_use_auto_toc.setObjectName(_fromUtf8("opt_use_auto_toc"))
        self.gridLayout.addWidget(self.opt_use_auto_toc, 0, 0, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.opt_toc_filter = QtGui.QLineEdit(Form)
        self.opt_toc_filter.setObjectName(_fromUtf8("opt_toc_filter"))
        self.gridLayout.addWidget(self.opt_toc_filter, 5, 1, 1, 1)
        self.opt_level1_toc = XPathEdit(Form)
        self.opt_level1_toc.setObjectName(_fromUtf8("opt_level1_toc"))
        self.gridLayout.addWidget(self.opt_level1_toc, 6, 0, 1, 2)
        self.opt_level2_toc = XPathEdit(Form)
        self.opt_level2_toc.setObjectName(_fromUtf8("opt_level2_toc"))
        self.gridLayout.addWidget(self.opt_level2_toc, 7, 0, 1, 2)
        self.opt_level3_toc = XPathEdit(Form)
        self.opt_level3_toc.setObjectName(_fromUtf8("opt_level3_toc"))
        self.gridLayout.addWidget(self.opt_level3_toc, 8, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 0, 1, 1)
        self.opt_duplicate_links_in_toc = QtGui.QCheckBox(Form)
        self.opt_duplicate_links_in_toc.setObjectName(_fromUtf8("opt_duplicate_links_in_toc"))
        self.gridLayout.addWidget(self.opt_duplicate_links_in_toc, 2, 0, 1, 2)
        self.label_10.setBuddy(self.opt_max_toc_links)
        self.label_16.setBuddy(self.opt_toc_threshold)
        self.label.setBuddy(self.opt_toc_filter)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_no_chapters_in_toc.setText(_("Do not add &detected chapters to the Table of Contents"))
        self.label_10.setText(_("Number of &links to add to Table of Contents"))
        self.label_16.setText(_("Chapter &threshold"))
        self.opt_use_auto_toc.setText(_("&Force use of auto-generated Table of Contents"))
        self.label.setText(_("TOC &Filter:"))
        self.opt_duplicate_links_in_toc.setText(_("Allow &duplicate links when creating the Table of Contents"))

from calibre.gui2.convert.xpath_wizard import XPathEdit

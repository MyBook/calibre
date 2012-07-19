# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/epub_output.ui'
#
# Created: Fri May 11 09:13:10 2012
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
        self.opt_dont_split_on_page_breaks = QtGui.QCheckBox(Form)
        self.opt_dont_split_on_page_breaks.setObjectName(_fromUtf8("opt_dont_split_on_page_breaks"))
        self.gridLayout.addWidget(self.opt_dont_split_on_page_breaks, 0, 0, 1, 1)
        self.opt_no_default_epub_cover = QtGui.QCheckBox(Form)
        self.opt_no_default_epub_cover.setObjectName(_fromUtf8("opt_no_default_epub_cover"))
        self.gridLayout.addWidget(self.opt_no_default_epub_cover, 1, 0, 1, 1)
        self.opt_no_svg_cover = QtGui.QCheckBox(Form)
        self.opt_no_svg_cover.setObjectName(_fromUtf8("opt_no_svg_cover"))
        self.gridLayout.addWidget(self.opt_no_svg_cover, 2, 0, 1, 1)
        self.opt_preserve_cover_aspect_ratio = QtGui.QCheckBox(Form)
        self.opt_preserve_cover_aspect_ratio.setObjectName(_fromUtf8("opt_preserve_cover_aspect_ratio"))
        self.gridLayout.addWidget(self.opt_preserve_cover_aspect_ratio, 2, 1, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.opt_flow_size = QtGui.QSpinBox(Form)
        self.opt_flow_size.setMinimum(25)
        self.opt_flow_size.setMaximum(1000000)
        self.opt_flow_size.setSingleStep(20)
        self.opt_flow_size.setObjectName(_fromUtf8("opt_flow_size"))
        self.gridLayout.addWidget(self.opt_flow_size, 3, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 262, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.opt_epub_flatten = QtGui.QCheckBox(Form)
        self.opt_epub_flatten.setObjectName(_fromUtf8("opt_epub_flatten"))
        self.gridLayout.addWidget(self.opt_epub_flatten, 1, 1, 1, 1)
        self.label.setBuddy(self.opt_flow_size)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.opt_no_svg_cover, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_preserve_cover_aspect_ratio.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_dont_split_on_page_breaks.setText(_("Do not &split on page breaks"))
        self.opt_no_default_epub_cover.setText(_("No default &cover"))
        self.opt_no_svg_cover.setText(_("No &SVG cover"))
        self.opt_preserve_cover_aspect_ratio.setText(_("Preserve cover &aspect ratio"))
        self.label.setText(_("Split files &larger than:"))
        self.opt_flow_size.setSuffix(_(" KB"))
        self.opt_epub_flatten.setText(_("&Flatten EPUB file structure"))


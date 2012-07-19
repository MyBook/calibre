# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/azw3_output.ui'
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
        Form.resize(724, 342)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 0, 1, 1)
        self.opt_prefer_author_sort = QtGui.QCheckBox(Form)
        self.opt_prefer_author_sort.setObjectName(_fromUtf8("opt_prefer_author_sort"))
        self.gridLayout.addWidget(self.opt_prefer_author_sort, 3, 0, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.opt_share_not_sync = QtGui.QCheckBox(Form)
        self.opt_share_not_sync.setObjectName(_fromUtf8("opt_share_not_sync"))
        self.gridLayout.addWidget(self.opt_share_not_sync, 5, 0, 1, 1)
        self.opt_no_inline_toc = QtGui.QCheckBox(Form)
        self.opt_no_inline_toc.setObjectName(_fromUtf8("opt_no_inline_toc"))
        self.gridLayout.addWidget(self.opt_no_inline_toc, 0, 0, 1, 1)
        self.opt_mobi_toc_at_start = QtGui.QCheckBox(Form)
        self.opt_mobi_toc_at_start.setObjectName(_fromUtf8("opt_mobi_toc_at_start"))
        self.gridLayout.addWidget(self.opt_mobi_toc_at_start, 2, 0, 1, 2)
        self.opt_toc_title = QtGui.QLineEdit(Form)
        self.opt_toc_title.setObjectName(_fromUtf8("opt_toc_title"))
        self.gridLayout.addWidget(self.opt_toc_title, 1, 1, 1, 1)
        self.opt_dont_compress = QtGui.QCheckBox(Form)
        self.opt_dont_compress.setObjectName(_fromUtf8("opt_dont_compress"))
        self.gridLayout.addWidget(self.opt_dont_compress, 4, 0, 1, 1)
        self.label.setBuddy(self.opt_toc_title)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.opt_prefer_author_sort.setText(_("Use author &sort for author"))
        self.label.setText(_("&Title for Table of Contents:"))
        self.opt_share_not_sync.setText(_("Enable sharing of book content via Facebook, etc. WARNING: Disables last read syncing"))
        self.opt_no_inline_toc.setText(_("Do not add Table of Contents to book"))
        self.opt_mobi_toc_at_start.setText(_("Put generated Table of Contents at &start of book instead of end"))
        self.opt_dont_compress.setText(_("Disable compression of the file contents"))


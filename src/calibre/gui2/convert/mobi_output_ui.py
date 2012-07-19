# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/mobi_output.ui'
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
        Form.resize(588, 342)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.opt_personal_doc = QtGui.QLineEdit(self.groupBox)
        self.opt_personal_doc.setObjectName(_fromUtf8("opt_personal_doc"))
        self.horizontalLayout.addWidget(self.opt_personal_doc)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.opt_share_not_sync = QtGui.QCheckBox(self.groupBox)
        self.opt_share_not_sync.setObjectName(_fromUtf8("opt_share_not_sync"))
        self.verticalLayout.addWidget(self.opt_share_not_sync)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 8, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 9, 0, 1, 1)
        self.opt_mobi_toc_at_start = QtGui.QCheckBox(Form)
        self.opt_mobi_toc_at_start.setObjectName(_fromUtf8("opt_mobi_toc_at_start"))
        self.gridLayout.addWidget(self.opt_mobi_toc_at_start, 2, 0, 1, 2)
        self.opt_mobi_ignore_margins = QtGui.QCheckBox(Form)
        self.opt_mobi_ignore_margins.setObjectName(_fromUtf8("opt_mobi_ignore_margins"))
        self.gridLayout.addWidget(self.opt_mobi_ignore_margins, 3, 0, 1, 1)
        self.opt_prefer_author_sort = QtGui.QCheckBox(Form)
        self.opt_prefer_author_sort.setObjectName(_fromUtf8("opt_prefer_author_sort"))
        self.gridLayout.addWidget(self.opt_prefer_author_sort, 4, 0, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.opt_toc_title = QtGui.QLineEdit(Form)
        self.opt_toc_title.setObjectName(_fromUtf8("opt_toc_title"))
        self.gridLayout.addWidget(self.opt_toc_title, 1, 1, 1, 1)
        self.opt_dont_compress = QtGui.QCheckBox(Form)
        self.opt_dont_compress.setObjectName(_fromUtf8("opt_dont_compress"))
        self.gridLayout.addWidget(self.opt_dont_compress, 6, 0, 1, 1)
        self.opt_no_inline_toc = QtGui.QCheckBox(Form)
        self.opt_no_inline_toc.setObjectName(_fromUtf8("opt_no_inline_toc"))
        self.gridLayout.addWidget(self.opt_no_inline_toc, 0, 0, 1, 1)
        self.opt_mobi_keep_original_images = QtGui.QCheckBox(Form)
        self.opt_mobi_keep_original_images.setObjectName(_fromUtf8("opt_mobi_keep_original_images"))
        self.gridLayout.addWidget(self.opt_mobi_keep_original_images, 5, 0, 1, 2)
        self.label.setBuddy(self.opt_toc_title)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Kindle options"))
        self.label_3.setText(_("Personal Doc tag:"))
        self.opt_share_not_sync.setText(_("Enable sharing of book content via Facebook, etc. WARNING: Disables last read syncing"))
        self.opt_mobi_toc_at_start.setText(_("Put generated Table of Contents at &start of book instead of end"))
        self.opt_mobi_ignore_margins.setText(_("Ignore &margins"))
        self.opt_prefer_author_sort.setText(_("Use author &sort for author"))
        self.label.setText(_("&Title for Table of Contents:"))
        self.opt_dont_compress.setText(_("Disable compression of the file contents"))
        self.opt_no_inline_toc.setText(_("Do not add Table of Contents to book"))
        self.opt_mobi_keep_original_images.setText(_("Do not convert all images to &JPEG (may result in images not working in older viewers)"))


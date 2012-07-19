# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/structure_detection.ui'
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
        Form.resize(657, 479)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.opt_chapter = XPathEdit(Form)
        self.opt_chapter.setObjectName(_fromUtf8("opt_chapter"))
        self.gridLayout.addWidget(self.opt_chapter, 0, 0, 1, 3)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.opt_chapter_mark = QtGui.QComboBox(Form)
        self.opt_chapter_mark.setMinimumContentsLength(20)
        self.opt_chapter_mark.setObjectName(_fromUtf8("opt_chapter_mark"))
        self.gridLayout.addWidget(self.opt_chapter_mark, 1, 1, 1, 1)
        self.opt_remove_first_image = QtGui.QCheckBox(Form)
        self.opt_remove_first_image.setObjectName(_fromUtf8("opt_remove_first_image"))
        self.gridLayout.addWidget(self.opt_remove_first_image, 2, 0, 1, 2)
        self.opt_insert_metadata = QtGui.QCheckBox(Form)
        self.opt_insert_metadata.setObjectName(_fromUtf8("opt_insert_metadata"))
        self.gridLayout.addWidget(self.opt_insert_metadata, 3, 0, 1, 2)
        self.opt_page_breaks_before = XPathEdit(Form)
        self.opt_page_breaks_before.setObjectName(_fromUtf8("opt_page_breaks_before"))
        self.gridLayout.addWidget(self.opt_page_breaks_before, 7, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 3)
        self.opt_remove_fake_margins = QtGui.QCheckBox(Form)
        self.opt_remove_fake_margins.setObjectName(_fromUtf8("opt_remove_fake_margins"))
        self.gridLayout.addWidget(self.opt_remove_fake_margins, 2, 2, 1, 1)
        self.label.setBuddy(self.opt_chapter_mark)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("Chapter &mark:"))
        self.opt_remove_first_image.setText(_("Remove first &image"))
        self.opt_insert_metadata.setText(_("Insert &metadata as page at start of book"))
        self.label_2.setText(_("The header and footer removal options have been replaced by the Search & Replace options. Click the Search & Replace category in the bar to the left to use these options. Leave the replace field blank and enter your header/footer removal regexps into the search field."))
        self.opt_remove_fake_margins.setText(_("Remove &fake margins"))

from calibre.gui2.convert.xpath_wizard import XPathEdit

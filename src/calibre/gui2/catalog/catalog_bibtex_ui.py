# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/catalog/catalog_bibtex.ui'
#
# Created: Mon Sep 19 14:02:07 2011
#      by: PyQt4 UI code generator 4.8.5
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
        Form.resize(579, 411)
        Form.setWindowTitle(_("Form"))
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setText(_("Bib file encoding:"))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setText(_("Fields to include in output:"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.bibfile_enc = QtGui.QComboBox(Form)
        self.bibfile_enc.setObjectName(_fromUtf8("bibfile_enc"))
        self.gridLayout.addWidget(self.bibfile_enc, 1, 0, 1, 1)
        self.db_fields = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.db_fields.sizePolicy().hasHeightForWidth())
        self.db_fields.setSizePolicy(sizePolicy)
        self.db_fields.setToolTip(_fromUtf8(""))
        self.db_fields.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.db_fields.setObjectName(_fromUtf8("db_fields"))
        self.gridLayout.addWidget(self.db_fields, 1, 1, 11, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setText(_("Encoding configuration (change if you have errors) :"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.bibfile_enctag = QtGui.QComboBox(Form)
        self.bibfile_enctag.setObjectName(_fromUtf8("bibfile_enctag"))
        self.gridLayout.addWidget(self.bibfile_enctag, 3, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 60, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 0, 1, 1)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setText(_("BibTeX entry type:"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.bib_entry = QtGui.QComboBox(Form)
        self.bib_entry.setObjectName(_fromUtf8("bib_entry"))
        self.gridLayout.addWidget(self.bib_entry, 6, 0, 1, 1)
        self.impcit = QtGui.QCheckBox(Form)
        self.impcit.setText(_("Create a citation tag?"))
        self.impcit.setObjectName(_fromUtf8("impcit"))
        self.gridLayout.addWidget(self.impcit, 7, 0, 1, 1)
        self.addfiles = QtGui.QCheckBox(Form)
        self.addfiles.setText(_("Add files path with formats?"))
        self.addfiles.setObjectName(_fromUtf8("addfiles"))
        self.gridLayout.addWidget(self.addfiles, 8, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setText(_("Expression to form the BibTeX citation tag:"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 9, 0, 1, 1)
        self.bib_cit = QtGui.QLineEdit(Form)
        self.bib_cit.setObjectName(_fromUtf8("bib_cit"))
        self.gridLayout.addWidget(self.bib_cit, 10, 0, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setText(_("Some explanation about this template:\n"
" -The fields availables are \'author_sort\', \'authors\', \'id\',\n"
"    \'isbn\', \'pubdate\', \'publisher\', \'series_index\', \'series\',\n"
"   \'tags\', \'timestamp\', \'title\', \'uuid\', \'title_sort\'\n"
" -For list types ie authors and tags, only the first element\n"
"   will be selected.\n"
" -For time field, only the date will be used. "))
        self.label_4.setScaledContents(False)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass


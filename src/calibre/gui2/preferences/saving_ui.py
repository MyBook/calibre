# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/preferences/saving.ui'
#
# Created: Thu Jul 19 23:32:29 2012
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
        Form.resize(707, 340)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.opt_save_cover = QtGui.QCheckBox(Form)
        self.opt_save_cover.setObjectName(_fromUtf8("opt_save_cover"))
        self.gridLayout.addWidget(self.opt_save_cover, 1, 0, 1, 1)
        self.opt_replace_whitespace = QtGui.QCheckBox(Form)
        self.opt_replace_whitespace.setObjectName(_fromUtf8("opt_replace_whitespace"))
        self.gridLayout.addWidget(self.opt_replace_whitespace, 1, 1, 1, 1)
        self.opt_update_metadata = QtGui.QCheckBox(Form)
        self.opt_update_metadata.setObjectName(_fromUtf8("opt_update_metadata"))
        self.gridLayout.addWidget(self.opt_update_metadata, 2, 0, 1, 1)
        self.opt_to_lowercase = QtGui.QCheckBox(Form)
        self.opt_to_lowercase.setObjectName(_fromUtf8("opt_to_lowercase"))
        self.gridLayout.addWidget(self.opt_to_lowercase, 2, 1, 1, 1)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)
        self.opt_timefmt = QtGui.QLineEdit(Form)
        self.opt_timefmt.setObjectName(_fromUtf8("opt_timefmt"))
        self.gridLayout.addWidget(self.opt_timefmt, 6, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 1)
        self.opt_formats = QtGui.QLineEdit(Form)
        self.opt_formats.setObjectName(_fromUtf8("opt_formats"))
        self.gridLayout.addWidget(self.opt_formats, 7, 1, 1, 1)
        self.save_template = SaveTemplate(Form)
        self.save_template.setObjectName(_fromUtf8("save_template"))
        self.gridLayout.addWidget(self.save_template, 8, 0, 1, 2)
        self.opt_asciiize = QtGui.QCheckBox(Form)
        self.opt_asciiize.setObjectName(_fromUtf8("opt_asciiize"))
        self.gridLayout.addWidget(self.opt_asciiize, 3, 1, 1, 1)
        self.opt_write_opf = QtGui.QCheckBox(Form)
        self.opt_write_opf.setObjectName(_fromUtf8("opt_write_opf"))
        self.gridLayout.addWidget(self.opt_write_opf, 3, 0, 1, 1)
        self.opt_show_files_after_save = QtGui.QCheckBox(Form)
        self.opt_show_files_after_save.setObjectName(_fromUtf8("opt_show_files_after_save"))
        self.gridLayout.addWidget(self.opt_show_files_after_save, 4, 0, 1, 2)
        self.label_2.setBuddy(self.opt_timefmt)
        self.label_3.setBuddy(self.opt_formats)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("Here you can control how calibre will save your books when you click the Save to Disk button:"))
        self.opt_save_cover.setText(_("Save &cover separately"))
        self.opt_replace_whitespace.setText(_("Replace space with &underscores"))
        self.opt_update_metadata.setText(_("Update &metadata in saved copies"))
        self.opt_to_lowercase.setText(_("Change paths to &lowercase"))
        self.label_2.setText(_("Format &dates as:"))
        self.label_3.setText(_("File &formats to save:"))
        self.opt_asciiize.setText(_("Convert non-English characters to &English equivalents"))
        self.opt_write_opf.setText(_("Save metadata in &OPF file"))
        self.opt_show_files_after_save.setText(_("&Show files in file browser after saving to disk"))

from calibre.gui2.preferences.save_template import SaveTemplate

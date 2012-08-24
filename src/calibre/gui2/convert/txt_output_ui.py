# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/txt_output.ui'
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
        Form.resize(392, 346)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.opt_txt_output_encoding = EncodingComboBox(self.groupBox)
        self.opt_txt_output_encoding.setEditable(True)
        self.opt_txt_output_encoding.setObjectName(_fromUtf8("opt_txt_output_encoding"))
        self.gridLayout.addWidget(self.opt_txt_output_encoding, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.opt_newline = QtGui.QComboBox(self.groupBox)
        self.opt_newline.setObjectName(_fromUtf8("opt_newline"))
        self.gridLayout.addWidget(self.opt_newline, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.opt_txt_output_formatting = QtGui.QComboBox(self.groupBox)
        self.opt_txt_output_formatting.setObjectName(_fromUtf8("opt_txt_output_formatting"))
        self.gridLayout.addWidget(self.opt_txt_output_formatting, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.opt_max_line_length = QtGui.QSpinBox(self.groupBox_2)
        self.opt_max_line_length.setObjectName(_fromUtf8("opt_max_line_length"))
        self.gridLayout_2.addWidget(self.opt_max_line_length, 1, 1, 1, 1)
        self.opt_force_max_line_length = QtGui.QCheckBox(self.groupBox_2)
        self.opt_force_max_line_length.setObjectName(_fromUtf8("opt_force_max_line_length"))
        self.gridLayout_2.addWidget(self.opt_force_max_line_length, 2, 0, 1, 2)
        self.opt_inline_toc = QtGui.QCheckBox(self.groupBox_2)
        self.opt_inline_toc.setObjectName(_fromUtf8("opt_inline_toc"))
        self.gridLayout_2.addWidget(self.opt_inline_toc, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.opt_keep_links = QtGui.QCheckBox(self.groupBox_3)
        self.opt_keep_links.setObjectName(_fromUtf8("opt_keep_links"))
        self.verticalLayout.addWidget(self.opt_keep_links)
        self.opt_keep_image_references = QtGui.QCheckBox(self.groupBox_3)
        self.opt_keep_image_references.setObjectName(_fromUtf8("opt_keep_image_references"))
        self.verticalLayout.addWidget(self.opt_keep_image_references)
        self.opt_keep_color = QtGui.QCheckBox(self.groupBox_3)
        self.opt_keep_color.setObjectName(_fromUtf8("opt_keep_color"))
        self.verticalLayout.addWidget(self.opt_keep_color)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.label_3.setBuddy(self.opt_txt_output_encoding)
        self.label.setBuddy(self.opt_newline)
        self.label_4.setBuddy(self.opt_txt_output_formatting)
        self.label_2.setBuddy(self.opt_max_line_length)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("General"))
        self.label_3.setText(_("Output &Encoding:"))
        self.label.setText(_("&Line ending style:"))
        self.label_4.setText(_("&Formatting:"))
        self.groupBox_2.setTitle(_("Plain"))
        self.label_2.setText(_("&Maximum line length:"))
        self.opt_force_max_line_length.setText(_("Force maximum line length"))
        self.opt_inline_toc.setText(_("&Inline TOC"))
        self.groupBox_3.setTitle(_("Markdown, Textile"))
        self.opt_keep_links.setText(_("Do not remove links (<a> tags) before processing"))
        self.opt_keep_image_references.setText(_("Do not remove image references before processing"))
        self.opt_keep_color.setText(_("Keep text color, when possible"))

from calibre.gui2.widgets import EncodingComboBox

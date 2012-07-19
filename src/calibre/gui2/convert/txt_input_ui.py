# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/txt_input.ui'
#
# Created: Sat Apr 30 12:56:24 2011
#      by: PyQt4 UI code generator 4.8.3
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
        Form.resize(518, 353)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.opt_paragraph_type = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_paragraph_type.sizePolicy().hasHeightForWidth())
        self.opt_paragraph_type.setSizePolicy(sizePolicy)
        self.opt_paragraph_type.setObjectName(_fromUtf8("opt_paragraph_type"))
        self.gridLayout.addWidget(self.opt_paragraph_type, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.opt_formatting_type = QtGui.QComboBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_formatting_type.sizePolicy().hasHeightForWidth())
        self.opt_formatting_type.setSizePolicy(sizePolicy)
        self.opt_formatting_type.setObjectName(_fromUtf8("opt_formatting_type"))
        self.gridLayout.addWidget(self.opt_formatting_type, 1, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.opt_preserve_spaces = QtGui.QCheckBox(self.groupBox_2)
        self.opt_preserve_spaces.setObjectName(_fromUtf8("opt_preserve_spaces"))
        self.verticalLayout_2.addWidget(self.opt_preserve_spaces)
        self.opt_txt_in_remove_indents = QtGui.QCheckBox(self.groupBox_2)
        self.opt_txt_in_remove_indents.setObjectName(_fromUtf8("opt_txt_in_remove_indents"))
        self.verticalLayout_2.addWidget(self.opt_txt_in_remove_indents)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.opt_markdown_disable_toc = QtGui.QCheckBox(self.groupBox)
        self.opt_markdown_disable_toc.setObjectName(_fromUtf8("opt_markdown_disable_toc"))
        self.verticalLayout.addWidget(self.opt_markdown_disable_toc)
        self.verticalLayout_3.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 213, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox_3.setTitle(_("Structure"))
        self.label_2.setText(_("Paragraph style:"))
        self.label_3.setText(_("Formatting style:"))
        self.groupBox_2.setTitle(_("Common"))
        self.opt_preserve_spaces.setText(_("Preserve &spaces"))
        self.opt_txt_in_remove_indents.setText(_("Remove indents at the beginning of lines"))
        self.groupBox.setTitle(_("Markdown"))
        self.label.setText(_("<p>Markdown is a simple markup language for text files, that allows for advanced formatting. To learn more visit <a href=\"http://daringfireball.net/projects/markdown\">markdown</a>."))
        self.opt_markdown_disable_toc.setText(_("Do not insert Table of Contents into output text when using markdown"))


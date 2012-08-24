# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/preferences/save_template.ui'
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
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 2)
        self.template_variables = QtGui.QTextBrowser(self.groupBox)
        self.template_variables.setObjectName(_fromUtf8("template_variables"))
        self.gridLayout_2.addWidget(self.template_variables, 3, 0, 1, 2)
        self.opt_template = HistoryBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opt_template.sizePolicy().hasHeightForWidth())
        self.opt_template.setSizePolicy(sizePolicy)
        self.opt_template.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.opt_template.setMinimumContentsLength(40)
        self.opt_template.setObjectName(_fromUtf8("opt_template"))
        self.gridLayout_2.addWidget(self.opt_template, 1, 0, 1, 1)
        self.open_editor = QtGui.QPushButton(self.groupBox)
        self.open_editor.setObjectName(_fromUtf8("open_editor"))
        self.gridLayout_2.addWidget(self.open_editor, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Save &template"))
        self.label_4.setText(_("By adjusting the template below, you can control what folders the files are saved in and what filenames they are given. You can use the / character to indicate sub-folders. Available metadata variables are described below. If a particular book does not have some metadata, the variable will be replaced by the empty string."))
        self.label_5.setText(_("Available variables:"))
        self.open_editor.setText(_("Template Editor"))

from calibre.gui2.preferences.history import HistoryBox

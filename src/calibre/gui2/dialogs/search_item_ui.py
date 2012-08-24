# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/dialogs/search_item.ui'
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
        Form.resize(400, 39)
        self.hboxlayout = QtGui.QHBoxLayout(Form)
        self.hboxlayout.setObjectName(_fromUtf8("hboxlayout"))
        self.field = QtGui.QComboBox(Form)
        self.field.setObjectName(_fromUtf8("field"))
        self.hboxlayout.addWidget(self.field)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.hboxlayout.addWidget(self.label)
        self.text = QtGui.QLineEdit(Form)
        self.text.setObjectName(_fromUtf8("text"))
        self.hboxlayout.addWidget(self.text)
        self.negate = QtGui.QCheckBox(Form)
        self.negate.setObjectName(_fromUtf8("negate"))
        self.hboxlayout.addWidget(self.negate)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("contains"))
        self.text.setToolTip(_("The text to search for. It is interpreted as a regular expression."))
        self.negate.setToolTip(_("<p>Negate this match. That is, only return results that <b>do not</b> match this query."))
        self.negate.setText(_("Negate"))


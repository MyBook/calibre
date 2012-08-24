# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/xpath_wizard.ui'
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
        Form.resize(400, 381)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.tag = QtGui.QComboBox(Form)
        self.tag.setEditable(True)
        self.tag.setObjectName(_fromUtf8("tag"))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.tag.addItem(_fromUtf8(""))
        self.verticalLayout.addWidget(self.tag)
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.attribute = QtGui.QLineEdit(Form)
        self.attribute.setObjectName(_fromUtf8("attribute"))
        self.verticalLayout.addWidget(self.attribute)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.value = QtGui.QLineEdit(Form)
        self.value.setObjectName(_fromUtf8("value"))
        self.verticalLayout.addWidget(self.value)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setWordWrap(True)
        self.label_5.setOpenExternalLinks(True)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label.setBuddy(self.tag)
        self.label_2.setBuddy(self.attribute)
        self.label_3.setBuddy(self.value)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("Match HTML &tags with tag name:"))
        self.tag.setItemText(0, _("*"))
        self.tag.setItemText(1, _("a"))
        self.tag.setItemText(2, _("br"))
        self.tag.setItemText(3, _("div"))
        self.tag.setItemText(4, _("h1"))
        self.tag.setItemText(5, _("h2"))
        self.tag.setItemText(6, _("h3"))
        self.tag.setItemText(7, _("h4"))
        self.tag.setItemText(8, _("h5"))
        self.tag.setItemText(9, _("h6"))
        self.tag.setItemText(10, _("hr"))
        self.tag.setItemText(11, _("span"))
        self.label_2.setText(_("Having the &attribute:"))
        self.label_3.setText(_("With &value:"))
        self.label_4.setText(_("(A regular expression)"))
        self.label_5.setText(_("<p>For example, to match all h2 tags that have class=\"chapter\", set tag to <i>h2</i>, attribute to <i>class</i> and value to <i>chapter</i>.</p><p>Leaving attribute blank will match any attribute and leaving value blank will match any value. Setting tag to * will match any tag.</p><p>To learn more advanced usage of XPath see the <a href=\"http://manual.calibre-ebook.com/xpath.html\">XPath Tutorial</a>."))


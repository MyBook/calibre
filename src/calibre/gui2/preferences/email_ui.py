# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/email.ui'
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
        Form.resize(701, 494)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_22 = QtGui.QLabel(Form)
        self.label_22.setWordWrap(True)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.verticalLayout.addWidget(self.label_22)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.email_view = QtGui.QTableView(Form)
        self.email_view.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.email_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.email_view.setObjectName(_fromUtf8("email_view"))
        self.horizontalLayout_8.addWidget(self.email_view)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.email_add = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("plus.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.email_add.setIcon(icon)
        self.email_add.setIconSize(QtCore.QSize(24, 24))
        self.email_add.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.email_add.setObjectName(_fromUtf8("email_add"))
        self.verticalLayout_8.addWidget(self.email_add)
        self.email_make_default = QtGui.QPushButton(Form)
        self.email_make_default.setObjectName(_fromUtf8("email_make_default"))
        self.verticalLayout_8.addWidget(self.email_make_default)
        self.email_remove = QtGui.QToolButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("minus.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.email_remove.setIcon(icon1)
        self.email_remove.setIconSize(QtCore.QSize(24, 24))
        self.email_remove.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.email_remove.setObjectName(_fromUtf8("email_remove"))
        self.verticalLayout_8.addWidget(self.email_remove)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.send_email_widget = SendEmail(Form)
        self.send_email_widget.setObjectName(_fromUtf8("send_email_widget"))
        self.verticalLayout.addWidget(self.send_email_widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_22.setText(_("calibre can send your books to you (or your reader) by email. Emails will be automatically sent for downloaded news to all email addresses that have Auto-send checked."))
        self.email_add.setToolTip(_("Add an email address to which to send books"))
        self.email_add.setText(_("&Add email"))
        self.email_make_default.setText(_("Make &default"))
        self.email_remove.setText(_("&Remove email"))

from calibre.gui2.wizard.send_email import SendEmail


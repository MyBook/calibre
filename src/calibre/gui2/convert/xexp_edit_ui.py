# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/xexp_edit.ui'
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
        Form.resize(430, 74)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.msg = QtGui.QLabel(Form)
        self.msg.setWordWrap(True)
        self.msg.setObjectName(_fromUtf8("msg"))
        self.verticalLayout.addWidget(self.msg)
        self.edit = HistoryLineEdit(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit.sizePolicy().hasHeightForWidth())
        self.edit.setSizePolicy(sizePolicy)
        self.edit.setMinimumSize(QtCore.QSize(350, 0))
        self.edit.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.edit.setMinimumContentsLength(30)
        self.edit.setObjectName(_fromUtf8("edit"))
        self.verticalLayout.addWidget(self.edit)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.button = QtGui.QToolButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("wizard.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button.setIcon(icon)
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setObjectName(_fromUtf8("button"))
        self.gridLayout.addWidget(self.button, 0, 1, 1, 1)
        self.msg.setBuddy(self.edit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.msg.setText(_("TextLabel"))
        self.button.setToolTip(_("Use a wizard to help construct the Regular expression"))
        self.button.setText(_("..."))

from calibre.gui2.widgets import HistoryLineEdit


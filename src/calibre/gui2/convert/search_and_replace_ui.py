# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/search_and_replace.ui'
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
        Form.resize(667, 451)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout_4 = QtGui.QGridLayout(Form)
        self.gridLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.sr_search = RegexEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_search.sizePolicy().hasHeightForWidth())
        self.sr_search.setSizePolicy(sizePolicy)
        self.sr_search.setObjectName(_fromUtf8("sr_search"))
        self.gridLayout_2.addWidget(self.sr_search, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.sr_replace = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_replace.sizePolicy().hasHeightForWidth())
        self.sr_replace.setSizePolicy(sizePolicy)
        self.sr_replace.setObjectName(_fromUtf8("sr_replace"))
        self.gridLayout_2.addWidget(self.sr_replace, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 1, 0, 1, 1)
        self.buttonsLayout = QtGui.QHBoxLayout()
        self.buttonsLayout.setSpacing(-1)
        self.buttonsLayout.setContentsMargins(0, -1, -1, -1)
        self.buttonsLayout.setObjectName(_fromUtf8("buttonsLayout"))
        self.sr_add = QtGui.QPushButton(Form)
        self.sr_add.setObjectName(_fromUtf8("sr_add"))
        self.buttonsLayout.addWidget(self.sr_add)
        self.sr_change = QtGui.QPushButton(Form)
        self.sr_change.setEnabled(False)
        self.sr_change.setObjectName(_fromUtf8("sr_change"))
        self.buttonsLayout.addWidget(self.sr_change)
        self.sr_remove = QtGui.QPushButton(Form)
        self.sr_remove.setEnabled(False)
        self.sr_remove.setObjectName(_fromUtf8("sr_remove"))
        self.buttonsLayout.addWidget(self.sr_remove)
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.VLine)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(3)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.buttonsLayout.addWidget(self.frame)
        self.sr_load = QtGui.QPushButton(Form)
        self.sr_load.setObjectName(_fromUtf8("sr_load"))
        self.buttonsLayout.addWidget(self.sr_load)
        self.sr_save = QtGui.QPushButton(Form)
        self.sr_save.setEnabled(False)
        self.sr_save.setObjectName(_fromUtf8("sr_save"))
        self.buttonsLayout.addWidget(self.sr_save)
        self.gridLayout_4.addLayout(self.buttonsLayout, 2, 0, 1, 1)
        self.searchReplaceLayout = QtGui.QHBoxLayout()
        self.searchReplaceLayout.setSpacing(-1)
        self.searchReplaceLayout.setContentsMargins(0, -1, -1, -1)
        self.searchReplaceLayout.setObjectName(_fromUtf8("searchReplaceLayout"))
        self.search_replace = QtGui.QTableWidget(Form)
        self.search_replace.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.search_replace.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.search_replace.setObjectName(_fromUtf8("search_replace"))
        self.search_replace.setColumnCount(0)
        self.search_replace.setRowCount(0)
        self.searchReplaceLayout.addWidget(self.search_replace)
        self.positionLayout = QtGui.QVBoxLayout()
        self.positionLayout.setObjectName(_fromUtf8("positionLayout"))
        self.sr_up = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_up.sizePolicy().hasHeightForWidth())
        self.sr_up.setSizePolicy(sizePolicy)
        self.sr_up.setMaximumSize(QtCore.QSize(32, 16777215))
        self.sr_up.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-up.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sr_up.setIcon(icon)
        self.sr_up.setObjectName(_fromUtf8("sr_up"))
        self.positionLayout.addWidget(self.sr_up)
        self.sr_down = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sr_down.sizePolicy().hasHeightForWidth())
        self.sr_down.setSizePolicy(sizePolicy)
        self.sr_down.setMaximumSize(QtCore.QSize(32, 16777215))
        self.sr_down.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-down.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sr_down.setIcon(icon1)
        self.sr_down.setObjectName(_fromUtf8("sr_down"))
        self.positionLayout.addWidget(self.sr_down)
        self.searchReplaceLayout.addLayout(self.positionLayout)
        self.gridLayout_4.addLayout(self.searchReplaceLayout, 3, 0, 1, 1)
        self.label = QtGui.QLabel(Form)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.label_4.setBuddy(self.sr_replace)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.groupBox.setTitle(_("Search/Replace Definition Edit"))
        self.label_4.setText(_("&Replacement Text"))
        self.sr_add.setToolTip(_("Add the current expression to the list of expressions that will be applied"))
        self.sr_add.setText(_("&Add"))
        self.sr_change.setToolTip(_("Edit the currently selected expression"))
        self.sr_change.setText(_("&Change"))
        self.sr_remove.setToolTip(_("Remove the currently selected expression"))
        self.sr_remove.setText(_("&Remove"))
        self.sr_load.setToolTip(_("Load a list of expressions from a previously saved file"))
        self.sr_load.setText(_("&Load"))
        self.sr_save.setToolTip(_("Save this list of expressions so that you can re-use it easily"))
        self.sr_save.setText(_("&Save"))
        self.sr_up.setToolTip(_("Move expression up."))
        self.sr_down.setToolTip(_("Move expression down."))
        self.label.setText(_("<p>Search and replace uses <i>regular expressions</i>. See the <a href=\"http://manual.calibre-ebook.com/regexp.html\">regular expressions tutorial</a> to get started with regular expressions. Also clicking the wizard button below will allow you to test your regular expression against the current input document. When you are happy with an expression, click the Add button to add it to the list of expressions."))

from regex_builder import RegexEdit

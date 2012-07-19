# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/convert/regex_builder.ui'
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

class Ui_RegexBuilder(object):
    def setupUi(self, RegexBuilder):
        RegexBuilder.setObjectName(_fromUtf8("RegexBuilder"))
        RegexBuilder.resize(882, 605)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RegexBuilder)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label = QtGui.QLabel(RegexBuilder)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_6.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.regex = QtGui.QLineEdit(RegexBuilder)
        self.regex.setObjectName(_fromUtf8("regex"))
        self.horizontalLayout.addWidget(self.regex)
        self.test = QtGui.QPushButton(RegexBuilder)
        self.test.setObjectName(_fromUtf8("test"))
        self.horizontalLayout.addWidget(self.test)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.label_3 = QtGui.QLabel(RegexBuilder)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_5.addWidget(self.label_3)
        self.occurrences = QtGui.QLabel(RegexBuilder)
        self.occurrences.setObjectName(_fromUtf8("occurrences"))
        self.horizontalLayout_5.addWidget(self.occurrences)
        spacerItem = QtGui.QSpacerItem(298, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(RegexBuilder)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.previous = QtGui.QPushButton(RegexBuilder)
        self.previous.setEnabled(False)
        self.previous.setObjectName(_fromUtf8("previous"))
        self.horizontalLayout_3.addWidget(self.previous)
        self.next = QtGui.QPushButton(RegexBuilder)
        self.next.setEnabled(False)
        self.next.setObjectName(_fromUtf8("next"))
        self.horizontalLayout_3.addWidget(self.next)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.groupBox = QtGui.QGroupBox(RegexBuilder)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.preview = QtGui.QPlainTextEdit(self.groupBox)
        self.preview.setUndoRedoEnabled(False)
        self.preview.setReadOnly(True)
        self.preview.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.preview.setObjectName(_fromUtf8("preview"))
        self.verticalLayout.addWidget(self.preview)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(328, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.button_box = QtGui.QDialogButtonBox(RegexBuilder)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.button_box.setObjectName(_fromUtf8("button_box"))
        self.horizontalLayout_4.addWidget(self.button_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(RegexBuilder)
        QtCore.QObject.connect(self.button_box, QtCore.SIGNAL(_fromUtf8("rejected()")), RegexBuilder.reject)
        QtCore.QMetaObject.connectSlotsByName(RegexBuilder)

    def retranslateUi(self, RegexBuilder):
        RegexBuilder.setWindowTitle(_("Regex Builder"))
        self.label.setText(_("Regex:"))
        self.test.setText(_("Test"))
        self.label_3.setText(_("Occurrences:"))
        self.occurrences.setText(_("0"))
        self.label_2.setText(_("Goto:"))
        self.previous.setText(_("&Previous"))
        self.next.setText(_("&Next"))
        self.groupBox.setTitle(_("Preview"))


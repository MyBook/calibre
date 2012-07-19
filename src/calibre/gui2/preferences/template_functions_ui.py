# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/template_functions.ui'
#
# Created: Sat Apr 30 12:56:25 2011
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
        Form.resize(798, 672)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.function_name = QtGui.QComboBox(Form)
        self.function_name.setEditable(True)
        self.function_name.setObjectName(_fromUtf8("function_name"))
        self.gridLayout_3.addWidget(self.function_name, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setToolTip(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.argument_count = QtGui.QSpinBox(Form)
        self.argument_count.setMinimum(-1)
        self.argument_count.setObjectName(_fromUtf8("argument_count"))
        self.gridLayout_3.addWidget(self.argument_count, 1, 1, 1, 1)
        self.documentation = QtGui.QTextEdit(Form)
        self.documentation.setObjectName(_fromUtf8("documentation"))
        self.gridLayout_3.addWidget(self.documentation, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.clear_button = QtGui.QPushButton(Form)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.horizontalLayout_2.addWidget(self.clear_button)
        self.delete_button = QtGui.QPushButton(Form)
        self.delete_button.setObjectName(_fromUtf8("delete_button"))
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.replace_button = QtGui.QPushButton(Form)
        self.replace_button.setObjectName(_fromUtf8("replace_button"))
        self.horizontalLayout_2.addWidget(self.replace_button)
        self.create_button = QtGui.QPushButton(Form)
        self.create_button.setObjectName(_fromUtf8("create_button"))
        self.horizontalLayout_2.addWidget(self.create_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_3)
        self.horizontalLayout1 = QtGui.QVBoxLayout()
        self.horizontalLayout1.setObjectName(_fromUtf8("horizontalLayout1"))
        self.label_41 = QtGui.QLabel(Form)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.horizontalLayout1.addWidget(self.label_41)
        self.program = QtGui.QPlainTextEdit(Form)
        self.program.setMinimumSize(QtCore.QSize(400, 0))
        self.program.setDocumentTitle(_fromUtf8(""))
        self.program.setTabStopWidth(30)
        self.program.setObjectName(_fromUtf8("program"))
        self.horizontalLayout1.addWidget(self.program)
        self.horizontalLayout.addLayout(self.horizontalLayout1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.textBrowser = QtGui.QTextBrowser(Form)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.label_2.setBuddy(self.function_name)
        self.label_3.setBuddy(self.argument_count)
        self.label_4.setBuddy(self.documentation)
        self.label_41.setBuddy(self.program)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_2.setText(_("&Function:"))
        self.function_name.setToolTip(_("Enter the name of the function to create."))
        self.label_3.setText(_("Arg &count:"))
        self.argument_count.setToolTip(_("Set this to -1 if the function takes a variable number of arguments"))
        self.label_4.setText(_("&Documentation:"))
        self.clear_button.setText(_("&Clear"))
        self.delete_button.setText(_("&Delete"))
        self.replace_button.setText(_("&Replace"))
        self.create_button.setText(_("C&reate"))
        self.label_41.setText(_("&Program Code: (be sure to follow python indenting rules)"))


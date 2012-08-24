# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/preferences/plugboard.ui'
#
# Created: Thu Jul 19 23:32:29 2012
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
        Form.resize(931, 389)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(Form)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout.addWidget(self.line, 1, 0, 1, 2)
        self.device_label = QtGui.QLabel(Form)
        self.device_label.setObjectName(_fromUtf8("device_label"))
        self.gridLayout.addWidget(self.device_label, 2, 0, 1, 2)
        self.line1 = QtGui.QFrame(Form)
        self.line1.setFrameShape(QtGui.QFrame.HLine)
        self.line1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line1.setObjectName(_fromUtf8("line1"))
        self.gridLayout.addWidget(self.line1, 3, 0, 1, 2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_2.addWidget(self.label_7, 0, 2, 1, 1)
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.new_format = QtGui.QComboBox(Form)
        self.new_format.setObjectName(_fromUtf8("new_format"))
        self.gridLayout_2.addWidget(self.new_format, 1, 1, 1, 1)
        self.new_device = QtGui.QComboBox(Form)
        self.new_device.setObjectName(_fromUtf8("new_device"))
        self.gridLayout_2.addWidget(self.new_device, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        self.edit_format = QtGui.QComboBox(Form)
        self.edit_format.setObjectName(_fromUtf8("edit_format"))
        self.gridLayout_2.addWidget(self.edit_format, 2, 1, 1, 1)
        self.edit_device = QtGui.QComboBox(Form)
        self.edit_device.setObjectName(_fromUtf8("edit_device"))
        self.gridLayout_2.addWidget(self.edit_device, 2, 2, 1, 1)
        self.label_41 = QtGui.QLabel(Form)
        self.label_41.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_2.addWidget(self.label_41, 3, 0, 1, 1)
        self.existing_plugboards = QtGui.QListWidget(Form)
        self.existing_plugboards.setSizeIncrement(QtCore.QSize(0, 0))
        self.existing_plugboards.setObjectName(_fromUtf8("existing_plugboards"))
        self.gridLayout_2.addWidget(self.existing_plugboards, 3, 1, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 4, 0, 1, 1)
        self.fields_layout = QtGui.QGridLayout()
        self.fields_layout.setObjectName(_fromUtf8("fields_layout"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.fields_layout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.fields_layout.addWidget(self.label_3, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.fields_layout.addItem(spacerItem1, 21, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ok_button = QtGui.QPushButton(Form)
        self.ok_button.setObjectName(_fromUtf8("ok_button"))
        self.horizontalLayout.addWidget(self.ok_button)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.del_button = QtGui.QPushButton(Form)
        self.del_button.setObjectName(_fromUtf8("del_button"))
        self.horizontalLayout.addWidget(self.del_button)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.fields_layout.addLayout(self.horizontalLayout, 19, 0, 1, 1)
        self.gridLayout.addLayout(self.fields_layout, 4, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label.setText(_("Here you can change the metadata calibre uses to update a book when saving to disk or sending to device.\n"
"\n"
"Use this dialog to define a \'plugboard\' for a format (or all formats) and a device (or all devices). The plugboard specifies what template is connected to what field. The template is used to compute a value, and that value is assigned to the connected field.\n"
"\n"
"Often templates will contain simple references to composite columns, but this is not necessary. You can use any template in a source box that you can use elsewhere in calibre.\n"
"\n"
"One possible use for a plugboard is to alter the title to contain series information. Another would be to change the author sort, something that mobi users might do to force it to use the \';\' that the kindle requires. A third would be to specify the language."))
        self.label_6.setText(_("Format (choose first)"))
        self.label_7.setText(_("Device (choose second)"))
        self.label_5.setText(_("Add new plugboard"))
        self.label_4.setText(_("Edit existing plugboard"))
        self.label_41.setText(_("Existing plugboards"))
        self.label_2.setText(_("Source template"))
        self.label_3.setText(_("Destination field"))
        self.ok_button.setText(_("Save plugboard"))
        self.del_button.setText(_("Delete plugboard"))


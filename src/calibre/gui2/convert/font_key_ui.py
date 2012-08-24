# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/convert/font_key.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(536, 554)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("wizard.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok|QtGui.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 3)
        self.label = QtGui.QLabel(Dialog)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 2)
        self.font_size_key = QtGui.QLineEdit(self.groupBox_2)
        self.font_size_key.setObjectName(_fromUtf8("font_size_key"))
        self.gridLayout_2.addWidget(self.font_size_key, 1, 2, 1, 1)
        self.output_base_font_size = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.output_base_font_size.setDecimals(1)
        self.output_base_font_size.setObjectName(_fromUtf8("output_base_font_size"))
        self.gridLayout_2.addWidget(self.output_base_font_size, 0, 2, 1, 1)
        self.button_use_default = QtGui.QPushButton(self.groupBox_2)
        self.button_use_default.setObjectName(_fromUtf8("button_use_default"))
        self.gridLayout_2.addWidget(self.button_use_default, 2, 0, 1, 3)
        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 4)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.input_base_font_size = QtGui.QDoubleSpinBox(self.groupBox)
        self.input_base_font_size.setDecimals(1)
        self.input_base_font_size.setObjectName(_fromUtf8("input_base_font_size"))
        self.gridLayout_3.addWidget(self.input_base_font_size, 0, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout.addWidget(self.label_6)
        self.input_font_size = QtGui.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_font_size.sizePolicy().hasHeightForWidth())
        self.input_font_size.setSizePolicy(sizePolicy)
        self.input_font_size.setMaximumSize(QtCore.QSize(130, 16777215))
        self.input_font_size.setDecimals(1)
        self.input_font_size.setObjectName(_fromUtf8("input_font_size"))
        self.horizontalLayout.addWidget(self.input_font_size)
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.input_mapped_font_size = QtGui.QLabel(self.groupBox)
        self.input_mapped_font_size.setObjectName(_fromUtf8("input_mapped_font_size"))
        self.horizontalLayout.addWidget(self.input_mapped_font_size)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 4)
        self.label_3.setBuddy(self.output_base_font_size)
        self.label_4.setBuddy(self.font_size_key)
        self.label_5.setBuddy(self.input_base_font_size)
        self.label_6.setBuddy(self.input_font_size)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Font rescaling wizard"))
        self.label.setText(_("<p>This wizard will help you choose an appropriate font size key for your needs. Just enter the base font size of the input document and then enter an input font size. The wizard will display what font size it will be mapped to, by the font rescaling algorithm. You can adjust the algorithm by adjusting the output base font size and font key below. When you find values suitable for you, click OK.</p>\n"
"<p>By default, if the output base font size is zero and/or no font size key is specified, calibre will use the values from the current Output Profile. </p>\n"
"<p>See the <a href=\"http://manual.calibre-ebook.com/conversion.html#font-size-rescaling\">User Manual</a> for a discussion of how font size rescaling works.</p>"))
        self.groupBox_2.setTitle(_("&Output document"))
        self.label_3.setText(_("&Base font size:"))
        self.label_4.setText(_("Font size &key:"))
        self.output_base_font_size.setSuffix(_(" pt"))
        self.button_use_default.setText(_("Use &default values"))
        self.groupBox.setTitle(_("&Input document"))
        self.label_5.setText(_("&Base font size:"))
        self.input_base_font_size.setSuffix(_(" pt"))
        self.label_6.setText(_("&Font size: "))
        self.input_font_size.setSuffix(_(" pt"))
        self.label_7.setText(_(" will map to size: "))
        self.input_mapped_font_size.setText(_("0.0 pt"))



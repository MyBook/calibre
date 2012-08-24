# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/preferences/misc.ui'
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
        Form.resize(502, 314)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.opt_worker_limit = QtGui.QSpinBox(Form)
        self.opt_worker_limit.setMinimum(1)
        self.opt_worker_limit.setObjectName(_fromUtf8("opt_worker_limit"))
        self.gridLayout.addWidget(self.opt_worker_limit, 0, 1, 1, 1)
        self.opt_enforce_cpu_limit = QtGui.QCheckBox(Form)
        self.opt_enforce_cpu_limit.setObjectName(_fromUtf8("opt_enforce_cpu_limit"))
        self.gridLayout.addWidget(self.opt_enforce_cpu_limit, 1, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.device_detection_button = QtGui.QPushButton(Form)
        self.device_detection_button.setObjectName(_fromUtf8("device_detection_button"))
        self.gridLayout.addWidget(self.device_detection_button, 4, 0, 1, 2)
        self.user_defined_device_button = QtGui.QPushButton(Form)
        self.user_defined_device_button.setObjectName(_fromUtf8("user_defined_device_button"))
        self.gridLayout.addWidget(self.user_defined_device_button, 5, 0, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(20, 19, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 7, 0, 1, 1)
        self.button_open_config_dir = QtGui.QPushButton(Form)
        self.button_open_config_dir.setObjectName(_fromUtf8("button_open_config_dir"))
        self.gridLayout.addWidget(self.button_open_config_dir, 8, 0, 1, 2)
        spacerItem3 = QtGui.QSpacerItem(20, 19, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 9, 0, 1, 1)
        self.button_osx_symlinks = QtGui.QPushButton(Form)
        self.button_osx_symlinks.setObjectName(_fromUtf8("button_osx_symlinks"))
        self.gridLayout.addWidget(self.button_osx_symlinks, 10, 0, 1, 2)
        spacerItem4 = QtGui.QSpacerItem(20, 1000, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 22, 0, 1, 1)
        self.proxies = QtGui.QLabel(Form)
        self.proxies.setText(_fromUtf8(""))
        self.proxies.setObjectName(_fromUtf8("proxies"))
        self.gridLayout.addWidget(self.proxies, 11, 0, 1, 2)
        self.label = QtGui.QLabel(Form)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        self.opt_worker_max_time = QtGui.QSpinBox(Form)
        self.opt_worker_max_time.setMaximum(100000)
        self.opt_worker_max_time.setSingleStep(10)
        self.opt_worker_max_time.setObjectName(_fromUtf8("opt_worker_max_time"))
        self.gridLayout.addWidget(self.opt_worker_max_time, 3, 1, 1, 1)
        self.label_5.setBuddy(self.opt_worker_limit)
        self.label.setBuddy(self.opt_worker_max_time)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_5.setText(_("Max. simultaneous conversion/news download jobs:"))
        self.opt_enforce_cpu_limit.setText(_("Limit the max. simultaneous jobs to the available CPU &cores"))
        self.device_detection_button.setText(_("Debug &device detection"))
        self.user_defined_device_button.setText(_("Get information to setup the &user defined device"))
        self.button_open_config_dir.setText(_("Open calibre &configuration directory"))
        self.button_osx_symlinks.setText(_("&Install command line tools"))
        self.label.setText(_("&Abort conversion jobs that take more than:"))
        self.opt_worker_max_time.setSpecialValueText(_("Never abort"))
        self.opt_worker_max_time.setSuffix(_(" minutes"))


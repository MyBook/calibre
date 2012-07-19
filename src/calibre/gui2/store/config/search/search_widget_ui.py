# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/store/config/search/search_widget.ui'
#
# Created: Sun Nov 13 17:08:05 2011
#      by: PyQt4 UI code generator 4.8.5
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
        Form.resize(465, 396)
        Form.setWindowTitle(_("Form"))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setTitle(_("Time"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setText(_("Number of seconds to wait for a store to respond"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.opt_timeout = QtGui.QSpinBox(self.groupBox)
        self.opt_timeout.setMinimum(1)
        self.opt_timeout.setObjectName(_fromUtf8("opt_timeout"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.opt_timeout)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(_("Number of seconds to let a store process results"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.opt_hang_time = QtGui.QSpinBox(self.groupBox)
        self.opt_hang_time.setMinimum(1)
        self.opt_hang_time.setMaximum(99)
        self.opt_hang_time.setSingleStep(1)
        self.opt_hang_time.setProperty("value", 1)
        self.opt_hang_time.setObjectName(_fromUtf8("opt_hang_time"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.opt_hang_time)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setTitle(_("Display"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setText(_("Maximum number of results to show per store"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_3)
        self.opt_max_results = QtGui.QSpinBox(self.groupBox_2)
        self.opt_max_results.setMinimum(1)
        self.opt_max_results.setObjectName(_fromUtf8("opt_max_results"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.opt_max_results)
        self.opt_open_external = QtGui.QCheckBox(self.groupBox_2)
        self.opt_open_external.setText(_("Open search result in system browser"))
        self.opt_open_external.setObjectName(_fromUtf8("opt_open_external"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.opt_open_external)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(Form)
        self.groupBox_3.setTitle(_("Threads"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setText(_("Number of search threads to use"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.opt_search_thread_count = QtGui.QSpinBox(self.groupBox_3)
        self.opt_search_thread_count.setMinimum(1)
        self.opt_search_thread_count.setObjectName(_fromUtf8("opt_search_thread_count"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.opt_search_thread_count)
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setText(_("Number of cache update threads to use"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.opt_cache_thread_count = QtGui.QSpinBox(self.groupBox_3)
        self.opt_cache_thread_count.setMinimum(1)
        self.opt_cache_thread_count.setObjectName(_fromUtf8("opt_cache_thread_count"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.opt_cache_thread_count)
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setText(_("Number of cover download threads to use"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.opt_cover_thread_count = QtGui.QSpinBox(self.groupBox_3)
        self.opt_cover_thread_count.setMinimum(1)
        self.opt_cover_thread_count.setObjectName(_fromUtf8("opt_cover_thread_count"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.opt_cover_thread_count)
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setText(_("Number of details threads to use"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.opt_details_thread_count = QtGui.QSpinBox(self.groupBox_3)
        self.opt_details_thread_count.setMinimum(1)
        self.opt_details_thread_count.setObjectName(_fromUtf8("opt_details_thread_count"))
        self.formLayout_3.setWidget(3, QtGui.QFormLayout.FieldRole, self.opt_details_thread_count)
        self.verticalLayout.addWidget(self.groupBox_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/jobs.ui'
#
# Created: Tue Nov 15 12:18:50 2011
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_JobsDialog(object):
    def setupUi(self, JobsDialog):
        JobsDialog.setObjectName(_fromUtf8("JobsDialog"))
        JobsDialog.resize(633, 542)
        JobsDialog.setWindowTitle(_("Active Jobs"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("jobs.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        JobsDialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(JobsDialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search = SearchBox2(JobsDialog)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout.addWidget(self.search)
        self.search_button = QtGui.QToolButton(JobsDialog)
        self.search_button.setToolTip(_("Find next match"))
        self.search_button.setText(_("&Search"))
        self.search_button.setObjectName(_fromUtf8("search_button"))
        self.horizontalLayout.addWidget(self.search_button)
        self.clear_button = QtGui.QToolButton(JobsDialog)
        self.clear_button.setToolTip(_("Find previous match"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("clear_left.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon1)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.horizontalLayout.addWidget(self.clear_button)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 2)
        self.jobs_view = QtGui.QTableView(JobsDialog)
        self.jobs_view.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.jobs_view.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.jobs_view.setAlternatingRowColors(True)
        self.jobs_view.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.jobs_view.setIconSize(QtCore.QSize(32, 32))
        self.jobs_view.setObjectName(_fromUtf8("jobs_view"))
        self.gridLayout.addWidget(self.jobs_view, 1, 0, 1, 2)
        self.kill_button = QtGui.QPushButton(JobsDialog)
        self.kill_button.setText(_("&Stop selected jobs"))
        self.kill_button.setObjectName(_fromUtf8("kill_button"))
        self.gridLayout.addWidget(self.kill_button, 2, 0, 1, 1)
        self.hide_button = QtGui.QPushButton(JobsDialog)
        self.hide_button.setText(_("&Hide selected jobs"))
        self.hide_button.setObjectName(_fromUtf8("hide_button"))
        self.gridLayout.addWidget(self.hide_button, 2, 1, 1, 1)
        self.details_button = QtGui.QPushButton(JobsDialog)
        self.details_button.setText(_("Show job &details"))
        self.details_button.setObjectName(_fromUtf8("details_button"))
        self.gridLayout.addWidget(self.details_button, 3, 0, 1, 1)
        self.show_button = QtGui.QPushButton(JobsDialog)
        self.show_button.setText(_("Show &all jobs"))
        self.show_button.setObjectName(_fromUtf8("show_button"))
        self.gridLayout.addWidget(self.show_button, 3, 1, 1, 1)
        self.stop_all_jobs_button = QtGui.QPushButton(JobsDialog)
        self.stop_all_jobs_button.setText(_("Stop &all non device jobs"))
        self.stop_all_jobs_button.setObjectName(_fromUtf8("stop_all_jobs_button"))
        self.gridLayout.addWidget(self.stop_all_jobs_button, 4, 0, 1, 1)
        self.hide_all_button = QtGui.QPushButton(JobsDialog)
        self.hide_all_button.setText(_("&Hide all jobs"))
        self.hide_all_button.setObjectName(_fromUtf8("hide_all_button"))
        self.gridLayout.addWidget(self.hide_all_button, 4, 1, 1, 1)

        self.retranslateUi(JobsDialog)
        QtCore.QMetaObject.connectSlotsByName(JobsDialog)

    def retranslateUi(self, JobsDialog):
        pass

from calibre.gui2.search_box import SearchBox2


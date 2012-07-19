# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/comicconf.ui'
#
# Created: Sat Apr 30 12:56:24 2011
#      by: PyQt4 UI code generator 4.8.3
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
        Dialog.resize(646, 503)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("convert.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.title_label = QtGui.QLabel(Dialog)
        self.title_label.setObjectName(_fromUtf8("title_label"))
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 1)
        self.opt_title = EnLineEdit(Dialog)
        self.opt_title.setObjectName(_fromUtf8("opt_title"))
        self.gridLayout.addWidget(self.opt_title, 0, 1, 1, 1)
        self.author_label = QtGui.QLabel(Dialog)
        self.author_label.setObjectName(_fromUtf8("author_label"))
        self.gridLayout.addWidget(self.author_label, 1, 0, 1, 1)
        self.opt_author = EnLineEdit(Dialog)
        self.opt_author.setObjectName(_fromUtf8("opt_author"))
        self.gridLayout.addWidget(self.opt_author, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.opt_colors = QtGui.QSpinBox(Dialog)
        self.opt_colors.setMinimum(8)
        self.opt_colors.setMaximum(3200000)
        self.opt_colors.setSingleStep(8)
        self.opt_colors.setObjectName(_fromUtf8("opt_colors"))
        self.gridLayout.addWidget(self.opt_colors, 2, 1, 1, 1)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.opt_profile = QtGui.QComboBox(Dialog)
        self.opt_profile.setObjectName(_fromUtf8("opt_profile"))
        self.gridLayout.addWidget(self.opt_profile, 3, 1, 1, 1)
        self.opt_dont_normalize = QtGui.QCheckBox(Dialog)
        self.opt_dont_normalize.setObjectName(_fromUtf8("opt_dont_normalize"))
        self.gridLayout.addWidget(self.opt_dont_normalize, 4, 0, 1, 1)
        self.opt_keep_aspect_ratio = QtGui.QCheckBox(Dialog)
        self.opt_keep_aspect_ratio.setObjectName(_fromUtf8("opt_keep_aspect_ratio"))
        self.gridLayout.addWidget(self.opt_keep_aspect_ratio, 5, 0, 1, 1)
        self.opt_dont_sharpen = QtGui.QCheckBox(Dialog)
        self.opt_dont_sharpen.setObjectName(_fromUtf8("opt_dont_sharpen"))
        self.gridLayout.addWidget(self.opt_dont_sharpen, 6, 0, 1, 1)
        self.opt_landscape = QtGui.QCheckBox(Dialog)
        self.opt_landscape.setObjectName(_fromUtf8("opt_landscape"))
        self.gridLayout.addWidget(self.opt_landscape, 9, 0, 1, 1)
        self.opt_no_sort = QtGui.QCheckBox(Dialog)
        self.opt_no_sort.setObjectName(_fromUtf8("opt_no_sort"))
        self.gridLayout.addWidget(self.opt_no_sort, 11, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 13, 1, 1, 1)
        self.opt_right2left = QtGui.QCheckBox(Dialog)
        self.opt_right2left.setObjectName(_fromUtf8("opt_right2left"))
        self.gridLayout.addWidget(self.opt_right2left, 10, 0, 1, 1)
        self.opt_despeckle = QtGui.QCheckBox(Dialog)
        self.opt_despeckle.setObjectName(_fromUtf8("opt_despeckle"))
        self.gridLayout.addWidget(self.opt_despeckle, 12, 0, 1, 1)
        self.opt_wide = QtGui.QCheckBox(Dialog)
        self.opt_wide.setObjectName(_fromUtf8("opt_wide"))
        self.gridLayout.addWidget(self.opt_wide, 8, 0, 1, 1)
        self.opt_disable_trim = QtGui.QCheckBox(Dialog)
        self.opt_disable_trim.setObjectName(_fromUtf8("opt_disable_trim"))
        self.gridLayout.addWidget(self.opt_disable_trim, 7, 0, 1, 1)
        self.title_label.setBuddy(self.opt_title)
        self.author_label.setBuddy(self.opt_author)
        self.label_3.setBuddy(self.opt_colors)
        self.label_4.setBuddy(self.opt_profile)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_("Dialog"))
        self.title_label.setText(_("&Title:"))
        self.author_label.setText(_("&Author(s):"))
        self.label_3.setText(_("&Number of Colors:"))
        self.label_4.setText(_("&Profile:"))
        self.opt_dont_normalize.setText(_("Disable &normalize"))
        self.opt_keep_aspect_ratio.setText(_("Keep &aspect ratio"))
        self.opt_dont_sharpen.setText(_("Disable &Sharpening"))
        self.opt_landscape.setText(_("&Landscape"))
        self.opt_no_sort.setText(_("Don\'t so&rt"))
        self.opt_right2left.setText(_("&Right to left"))
        self.opt_despeckle.setText(_("De&speckle"))
        self.opt_wide.setText(_("&Wide"))
        self.opt_disable_trim.setText(_("Disable &Trimming"))

from calibre.gui2.widgets import EnLineEdit


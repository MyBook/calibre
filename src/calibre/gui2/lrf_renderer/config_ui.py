# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/lrf_renderer/config.ui'
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

class Ui_ViewerConfig(object):
    def setupUi(self, ViewerConfig):
        ViewerConfig.setObjectName(_fromUtf8("ViewerConfig"))
        ViewerConfig.resize(373, 264)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("config.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ViewerConfig.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(ViewerConfig)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.white_background = QtGui.QCheckBox(ViewerConfig)
        self.white_background.setObjectName(_fromUtf8("white_background"))
        self.gridLayout.addWidget(self.white_background, 0, 0, 1, 1)
        self.hyphenate = QtGui.QCheckBox(ViewerConfig)
        self.hyphenate.setChecked(True)
        self.hyphenate.setObjectName(_fromUtf8("hyphenate"))
        self.gridLayout.addWidget(self.hyphenate, 1, 0, 1, 1)
        self.label = QtGui.QLabel(ViewerConfig)
        self.label.setFrameShape(QtGui.QFrame.Box)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(ViewerConfig)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 1)

        self.retranslateUi(ViewerConfig)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ViewerConfig.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ViewerConfig.reject)
        QtCore.QMetaObject.connectSlotsByName(ViewerConfig)

    def retranslateUi(self, ViewerConfig):
        ViewerConfig.setWindowTitle(_("Configure Viewer"))
        self.white_background.setText(_("Use white background"))
        self.hyphenate.setText(_("Hyphenate"))
        self.label.setText(_("<b>Changes will only take effect after a restart.</b>"))



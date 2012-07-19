# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/dialogs/book_info.ui'
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

class Ui_BookInfo(object):
    def setupUi(self, BookInfo):
        BookInfo.setObjectName(_fromUtf8("BookInfo"))
        BookInfo.resize(917, 492)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("metadata.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        BookInfo.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(BookInfo)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.title = QtGui.QLabel(BookInfo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName(_fromUtf8("title"))
        self.gridLayout.addWidget(self.title, 0, 0, 1, 2)
        self.cover = CoverView(BookInfo)
        self.cover.setObjectName(_fromUtf8("cover"))
        self.gridLayout.addWidget(self.cover, 2, 0, 3, 1)
        self.fit_cover = QtGui.QCheckBox(BookInfo)
        self.fit_cover.setObjectName(_fromUtf8("fit_cover"))
        self.gridLayout.addWidget(self.fit_cover, 3, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.previous_button = QtGui.QPushButton(BookInfo)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("previous.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon1)
        self.previous_button.setObjectName(_fromUtf8("previous_button"))
        self.horizontalLayout.addWidget(self.previous_button)
        self.next_button = QtGui.QPushButton(BookInfo)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("next.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon2)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.horizontalLayout.addWidget(self.next_button)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.details = QtWebKit.QWebView(BookInfo)
        self.details.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.details.setObjectName(_fromUtf8("details"))
        self.gridLayout.addWidget(self.details, 2, 1, 1, 1)

        self.retranslateUi(BookInfo)
        QtCore.QMetaObject.connectSlotsByName(BookInfo)

    def retranslateUi(self, BookInfo):
        BookInfo.setWindowTitle(_("Dialog"))
        self.title.setText(_("TextLabel"))
        self.fit_cover.setText(_("Fit &cover within view"))
        self.previous_button.setText(_("&Previous"))
        self.next_button.setText(_("&Next"))

from PyQt4 import QtWebKit
from calibre.gui2.widgets import CoverView


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/wizard/stanza.ui'
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

class Ui_WizardPage(object):
    def setupUi(self, WizardPage):
        WizardPage.setObjectName(_fromUtf8("WizardPage"))
        WizardPage.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(WizardPage)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(WizardPage)
        self.label.setWordWrap(True)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.content_server = QtGui.QCheckBox(WizardPage)
        self.content_server.setObjectName(_fromUtf8("content_server"))
        self.verticalLayout.addWidget(self.content_server)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.instructions = QtGui.QLabel(WizardPage)
        self.instructions.setWordWrap(True)
        self.instructions.setObjectName(_fromUtf8("instructions"))
        self.verticalLayout.addWidget(self.instructions)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(WizardPage)
        QtCore.QMetaObject.connectSlotsByName(WizardPage)

    def retranslateUi(self, WizardPage):
        WizardPage.setWindowTitle(_("WizardPage"))
        WizardPage.setTitle(_("Welcome to calibre"))
        WizardPage.setSubTitle(_("The one stop solution to all your e-book needs."))
        self.label.setText(_("<p>If you use the <a href=\"http://www.lexcycle.com/download\">Stanza</a> e-book app on your iPhone/iTouch, you can access your calibre book collection directly on the device. To do this you have to turn on the calibre content server."))
        self.content_server.setText(_("Turn on the &content server"))
        self.instructions.setText(_("<p>Remember to leave calibre running as the server only runs as long as calibre is running.\n"
"<p>Stanza should see your calibre collection automatically. If not, try adding the URL http://myhostname:8080 as a new catalog in the Stanza reader on your iPhone. Here myhostname should be the fully qualified hostname or the IP address of the computer calibre is running on."))


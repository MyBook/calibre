# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/gugu/w/calibre/src/calibre/gui2/preferences/plugins.ui'
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
        Form.resize(723, 540)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.search = SearchBox2(Form)
        self.search.setObjectName(_fromUtf8("search"))
        self.horizontalLayout.addWidget(self.search)
        self.next_button = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_button.sizePolicy().hasHeightForWidth())
        self.next_button.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-down.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_button.setIcon(icon)
        self.next_button.setObjectName(_fromUtf8("next_button"))
        self.horizontalLayout.addWidget(self.next_button)
        self.previous_button = QtGui.QPushButton(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.previous_button.sizePolicy().hasHeightForWidth())
        self.previous_button.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(I("arrow-up.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previous_button.setIcon(icon1)
        self.previous_button.setObjectName(_fromUtf8("previous_button"))
        self.horizontalLayout.addWidget(self.previous_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.user_installed_plugins = QtGui.QCheckBox(Form)
        self.user_installed_plugins.setObjectName(_fromUtf8("user_installed_plugins"))
        self.verticalLayout.addWidget(self.user_installed_plugins)
        self.plugin_view = QtGui.QTreeView(Form)
        self.plugin_view.setAlternatingRowColors(True)
        self.plugin_view.setIconSize(QtCore.QSize(32, 32))
        self.plugin_view.setAnimated(True)
        self.plugin_view.setWordWrap(True)
        self.plugin_view.setHeaderHidden(True)
        self.plugin_view.setObjectName(_fromUtf8("plugin_view"))
        self.verticalLayout.addWidget(self.plugin_view)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.toggle_plugin_button = QtGui.QPushButton(Form)
        self.toggle_plugin_button.setObjectName(_fromUtf8("toggle_plugin_button"))
        self.horizontalLayout_6.addWidget(self.toggle_plugin_button)
        self.customize_plugin_button = QtGui.QPushButton(Form)
        self.customize_plugin_button.setObjectName(_fromUtf8("customize_plugin_button"))
        self.horizontalLayout_6.addWidget(self.customize_plugin_button)
        self.remove_plugin_button = QtGui.QPushButton(Form)
        self.remove_plugin_button.setObjectName(_fromUtf8("remove_plugin_button"))
        self.horizontalLayout_6.addWidget(self.remove_plugin_button)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.frame = QtGui.QFrame(Form)
        self.frame.setFrameShape(QtGui.QFrame.HLine)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.button_plugin_new = QtGui.QPushButton(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(I("plugins/plugin_new.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_plugin_new.setIcon(icon2)
        self.button_plugin_new.setObjectName(_fromUtf8("button_plugin_new"))
        self.horizontalLayout_7.addWidget(self.button_plugin_new)
        self.button_plugin_updates = QtGui.QPushButton(Form)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(I("plugins/plugin_updater.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_plugin_updates.setIcon(icon3)
        self.button_plugin_updates.setObjectName(_fromUtf8("button_plugin_updates"))
        self.horizontalLayout_7.addWidget(self.button_plugin_updates)
        self.button_plugin_add = QtGui.QPushButton(Form)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(I("document_open.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_plugin_add.setIcon(icon4)
        self.button_plugin_add.setObjectName(_fromUtf8("button_plugin_add"))
        self.horizontalLayout_7.addWidget(self.button_plugin_add)
        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_8.setText(_("Here you can customize the behavior of Calibre by controlling what plugins it uses."))
        self.next_button.setText(_("&Next"))
        self.previous_button.setText(_("&Previous"))
        self.user_installed_plugins.setToolTip(_("Show only those plugins that have been installed by you"))
        self.user_installed_plugins.setText(_("Show only &user installed plugins"))
        self.toggle_plugin_button.setText(_("Enable/&Disable plugin"))
        self.customize_plugin_button.setText(_("&Customize plugin"))
        self.remove_plugin_button.setText(_("&Remove plugin"))
        self.button_plugin_new.setText(_("Get &new plugins"))
        self.button_plugin_updates.setText(_("Check for &updated plugins"))
        self.button_plugin_add.setText(_("&Load plugin from file"))

from calibre.gui2.search_box import SearchBox2


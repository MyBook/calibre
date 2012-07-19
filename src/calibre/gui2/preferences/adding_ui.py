# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kovid/work/calibre/src/calibre/gui2/preferences/adding.ui'
#
# Created: Sun Jun 10 09:20:00 2012
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
        Form.resize(753, 547)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_6 = QtGui.QLabel(self.tab_3)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 3)
        self.opt_read_file_metadata = QtGui.QCheckBox(self.tab_3)
        self.opt_read_file_metadata.setObjectName(_fromUtf8("opt_read_file_metadata"))
        self.gridLayout_2.addWidget(self.opt_read_file_metadata, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.opt_swap_author_names = QtGui.QCheckBox(self.tab_3)
        self.opt_swap_author_names.setObjectName(_fromUtf8("opt_swap_author_names"))
        self.horizontalLayout.addWidget(self.opt_swap_author_names)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 2)
        self.opt_preserve_date_on_ctl = QtGui.QCheckBox(self.tab_3)
        self.opt_preserve_date_on_ctl.setObjectName(_fromUtf8("opt_preserve_date_on_ctl"))
        self.gridLayout_2.addWidget(self.opt_preserve_date_on_ctl, 2, 0, 1, 3)
        self.opt_add_formats_to_existing = QtGui.QCheckBox(self.tab_3)
        self.opt_add_formats_to_existing.setObjectName(_fromUtf8("opt_add_formats_to_existing"))
        self.gridLayout_2.addWidget(self.opt_add_formats_to_existing, 3, 0, 1, 2)
        self.opt_automerge = QtGui.QComboBox(self.tab_3)
        self.opt_automerge.setObjectName(_fromUtf8("opt_automerge"))
        self.gridLayout_2.addWidget(self.opt_automerge, 3, 2, 1, 1)
        self.label_230 = QtGui.QLabel(self.tab_3)
        self.label_230.setObjectName(_fromUtf8("label_230"))
        self.gridLayout_2.addWidget(self.label_230, 4, 0, 1, 1)
        self.opt_new_book_tags = QtGui.QLineEdit(self.tab_3)
        self.opt_new_book_tags.setObjectName(_fromUtf8("opt_new_book_tags"))
        self.gridLayout_2.addWidget(self.opt_new_book_tags, 4, 2, 1, 1)
        self.metadata_box = QtGui.QGroupBox(self.tab_3)
        self.metadata_box.setObjectName(_fromUtf8("metadata_box"))
        self.verticalLayout = QtGui.QVBoxLayout(self.metadata_box)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 363, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_2.addWidget(self.metadata_box, 5, 0, 1, 3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.opt_auto_add_check_for_duplicates = QtGui.QCheckBox(self.tab_4)
        self.opt_auto_add_check_for_duplicates.setObjectName(_fromUtf8("opt_auto_add_check_for_duplicates"))
        self.gridLayout_3.addWidget(self.opt_auto_add_check_for_duplicates, 3, 0, 1, 2)
        self.label = QtGui.QLabel(self.tab_4)
        self.label.setWordWrap(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.tab_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.tab_4)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.opt_blocked_auto_formats = QtGui.QListWidget(self.groupBox)
        self.opt_blocked_auto_formats.setAlternatingRowColors(True)
        self.opt_blocked_auto_formats.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.opt_blocked_auto_formats.setObjectName(_fromUtf8("opt_blocked_auto_formats"))
        self.verticalLayout_2.addWidget(self.opt_blocked_auto_formats)
        self.gridLayout_3.addWidget(self.groupBox, 5, 0, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(272, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.opt_auto_add_path = QtGui.QLineEdit(self.tab_4)
        self.opt_auto_add_path.setObjectName(_fromUtf8("opt_auto_add_path"))
        self.horizontalLayout_2.addWidget(self.opt_auto_add_path)
        self.auto_add_browse_button = QtGui.QToolButton(self.tab_4)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(I("document_open.png"))), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.auto_add_browse_button.setIcon(icon)
        self.auto_add_browse_button.setObjectName(_fromUtf8("auto_add_browse_button"))
        self.horizontalLayout_2.addWidget(self.auto_add_browse_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.opt_auto_add_auto_convert = QtGui.QCheckBox(self.tab_4)
        self.opt_auto_add_auto_convert.setObjectName(_fromUtf8("opt_auto_add_auto_convert"))
        self.gridLayout_3.addWidget(self.opt_auto_add_auto_convert, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.label_230.setBuddy(self.opt_new_book_tags)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.opt_add_formats_to_existing, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.opt_automerge.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_("Form"))
        self.label_6.setText(_("Here you can control how calibre will read metadata from the files you add to it. calibre can either read metadata from the contents of the file, or from the filename."))
        self.opt_read_file_metadata.setText(_("Read &metadata from file contents rather than file name"))
        self.opt_swap_author_names.setToolTip(_("Swap the firstname and lastname of the author. This affects only metadata read from file names."))
        self.opt_swap_author_names.setText(_("&Swap author firstname and lastname"))
        self.opt_preserve_date_on_ctl.setText(_("When using the  \"&Copy to library\" action to copy books between libraries, preserve the date"))
        self.opt_add_formats_to_existing.setToolTip(_("Automerge: If books with similar titles and authors found, merge the incoming formats automatically into\n"
"existing book records. The box to the right controls what happens when an existing record already has\n"
"the incoming format. Note that this option also affects the Copy to library action.\n"
"\n"
"Title match ignores leading indefinite articles (\"the\", \"a\", \"an\"), punctuation, case, etc. Author match is exact."))
        self.opt_add_formats_to_existing.setText(_("&Automerge added books if they already exist in the calibre library:"))
        self.opt_automerge.setToolTip(_("Automerge: If books with similar titles and authors found, merge the incoming formats automatically into\n"
"existing book records. This box controls what happens when an existing record already has\n"
"the incoming format: \n"
"\n"
"Ignore duplicate incoming files - means that existing files in your calibre library will not be replaced\n"
"Overwrite existing duplicate files - means that existing files in your calibre library will be replaced\n"
"Create new record for each duplicate file - means that a new book entry will be created for each duplicate file\n"
"\n"
"Title matching ignores leading indefinite articles (\"the\", \"a\", \"an\"), punctuation, case, etc.\n"
"Author matching is exact."))
        self.label_230.setText(_("&Tags to apply when adding a book:"))
        self.opt_new_book_tags.setToolTip(_("A comma-separated list of tags that will be applied to books added to the library"))
        self.metadata_box.setTitle(_("&Configure metadata from file name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _("The Add &Process"))
        self.opt_auto_add_check_for_duplicates.setToolTip(_("If set, this option will causes calibre to check if a file\n"
" being auto-added is already in the calibre library.\n"
" If it is, a meesage will pop up asking you whether\n"
" you want to add it anyway."))
        self.opt_auto_add_check_for_duplicates.setText(_("Check for &duplicates when auto-adding files"))
        self.label.setText(_("Specify a folder. Any files you put into this folder will be automatically added to calibre (restart required)."))
        self.label_2.setText(_("<b>WARNING:</b> Files in the above folder will be deleted after being added to calibre."))
        self.label_3.setText(_("Ignore files with the following extensions when automatically adding "))
        self.opt_auto_add_path.setPlaceholderText(_("Folder to auto-add files from"))
        self.auto_add_browse_button.setToolTip(_("Browse for folder"))
        self.auto_add_browse_button.setText(_("..."))
        self.opt_auto_add_auto_convert.setText(_("Automatically &convert added files to the current output format"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _("&Automatic Adding"))



# Form implementation generated from reading ui file 'ui/replaceInValuesDialog.ui'
#
# Created by: PyQt6 UI code generator 6.11.0
#
# Automatically generated - do not edit.
# Use `python setup.py build_ui` to update it.

from PyQt6 import (
    QtCore,
    QtGui,
    QtWidgets,
)

from picard.i18n import gettext as _


class Ui_ReplaceInValuesDialog(object):
    def setupUi(self, ReplaceInValuesDialog):
        ReplaceInValuesDialog.setObjectName("ReplaceInValuesDialog")
        ReplaceInValuesDialog.resize(401, 194)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=ReplaceInValuesDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=ReplaceInValuesDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 371, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.replace_text = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.replace_text.setObjectName("replace_text")
        self.verticalLayout.addWidget(self.replace_text)
        self.label_2 = QtWidgets.QLabel(parent=self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.with_text = QtWidgets.QLineEdit(parent=self.verticalLayoutWidget)
        self.with_text.setObjectName("with_text")
        self.verticalLayout.addWidget(self.with_text)

        self.retranslateUi(ReplaceInValuesDialog)
        self.buttonBox.accepted.connect(ReplaceInValuesDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(ReplaceInValuesDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(ReplaceInValuesDialog)

    def retranslateUi(self, ReplaceInValuesDialog):
        ReplaceInValuesDialog.setWindowTitle(_("Replace in Values"))
        self.label.setText(_("Replace"))
        self.label_2.setText(_("With"))

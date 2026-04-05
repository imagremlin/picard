from PyQt6 import QtWidgets

# Correct import for generated UI class
from picard.ui.forms.ui_replaceInValuesDialog import Ui_ReplaceInValuesDialog


class ReplaceInValuesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ReplaceInValuesDialog()
        self.ui.setupUi(self)

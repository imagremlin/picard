from PyQt6 import QtWidgets

# Correct import for generated UI class
from picard.ui.forms.ui_replaceInValuesDialog import Ui_ReplaceInValuesDialog


class ReplaceInValuesDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ReplaceInValuesDialog()
        self.ui.setupUi(self)
        self._initialize_ui()

    def _initialize_ui(self):
        self.replace_text = self.ui.replace_text
        self.with_text = self.ui.with_text
        self.ui.replace_text.textChanged.connect(self._update_ok_button_state)
        self._update_ok_button_state()
        self.replace_text.setFocus()

    def _update_ok_button_state(self):
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Ok).setEnabled(
            bool(self.ui.replace_text.text())
        )

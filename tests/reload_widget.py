import importlib

from PySide6 import QtWidgets
import sys

from pathlib import Path
CURRENT = Path(__file__).resolve().parent

sys.path.insert(0, str(CURRENT.parent))

import tests.widget as widget  # noqa: E402

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QtWidgets.QWidget()
        self.setCentralWidget(self._widget)

        self._layout = QtWidgets.QVBoxLayout()
        self._widget.setLayout(self._layout)

        self.widget = widget.Widget()
        self._layout.addWidget(self.widget)

        self.button = QtWidgets.QPushButton("reload")
        self._layout.addWidget(self.button)

        self.button.clicked.connect(self.reload)

    def reload(self):
        importlib.reload(widget)
        self.layout().removeWidget(self.widget)
        self._layout.removeWidget(self.button)

        self.widget.setParent(None)
        self.widget = widget.Widget()
        self._layout.addWidget(self.widget)
        self._layout.addWidget(self.button)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()

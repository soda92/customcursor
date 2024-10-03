import importlib

from PySide6 import QtWidgets, QtCore
import sys

from pathlib import Path

CURRENT = Path(__file__).resolve().parent

sys.path.insert(0, str(CURRENT.parent))

import main #noqa: E402
import os  # noqa: E402


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._widget = QtWidgets.QWidget()
        self.setCentralWidget(self._widget)

        self._layout = QtWidgets.QVBoxLayout()
        self._widget.setLayout(self._layout)

        self.widget = main.Widget()
        self._layout.addWidget(self.widget)

        self.button = QtWidgets.QPushButton("reload")
        self._layout.addWidget(self.button)

        self.button.clicked.connect(self.reload)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)
        self.timer.timeout.connect(self.reload)
        self.timer.start()
        self.mtime = os.path.getmtime("main.py")

    def reload(self):
        self.mtime2 = os.path.getmtime("main.py")
        if self.mtime2 == self.mtime:
            return
        else:
            self.mtime = self.mtime2
        try:
            importlib.reload(main)
        except Exception as _:
            pass
        else:
            self.layout().removeWidget(self.widget)
            self._layout.removeWidget(self.button)

            self.widget.setParent(None)
            self.widget = main.Widget()
            self._layout.addWidget(self.widget)
            self._layout.addWidget(self.button)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    window = MainWindow()
    window.show()
    app.exec()

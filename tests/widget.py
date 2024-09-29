from PySide6 import QtWidgets

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self._layout = QtWidgets.QHBoxLayout()
        self._layout.addWidget(QtWidgets.QLabel("bbb"))
        self._layout.addWidget(QtWidgets.QLabel("bbb"))
        self._layout.addWidget(QtWidgets.QLabel("ccc"))

        self.setLayout(self._layout)

from PySide6 import QtWidgets
from pathlib import Path

CURRENT = Path(__file__).resolve().parent


class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.data = bytearray(
            CURRENT.joinpath("Cursors_ico/aero_arrow.ico").read_bytes()
        )

        self._layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QTextBrowser()
        self.label.setText(str(self.data))
        self._layout.addWidget(self.label)
        self.setLayout(self._layout)

        self.widget_2 = QtWidgets.QWidget()
        self.layout_2 = QtWidgets.QHBoxLayout()
        self.widget_2.setLayout(self.layout_2)
        self.edit = QtWidgets.QLineEdit()
        self.layout_2.addWidget(self.edit)

        self.text_area2 = QtWidgets.QTextBrowser()
        self.result = []
        def get_data(s, start, len):
            return int(s[start:start+len][::-1].hex(), 16)
        self.result.append(f"image type: {int(self.data[2:4][::-1].hex(), 16)}")
        entries = int(self.data[4:6][::-1].hex(), 16)
        self.result.append(f"image entries: {entries}")
        for i in range(entries):
            header = self.data[6+16*i: 6+16*(i+1)]
            print(f"width: {header[0]}")
            print(f"height: {header[1]}")
            print(f"size: {get_data(header, 8, 4)}")
            print(f"offset: {get_data(header, 12, 4)}")
        self.text_area2.setText("\n".join(map(str, self.result)))

        self._layout.addWidget(self.text_area2)
        self._layout.addWidget(self.widget_2)

        self.edit.returnPressed.connect(self.eval)

    def eval(self):
        expr = self.edit.text()
        self.edit.clear()
        result = eval(expr)
        self.result.append(expr)
        self.result.append(result)
        self.text_area2.setText("\n".join(map(str, self.result)))

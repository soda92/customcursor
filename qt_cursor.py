from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import QObject, QCoreApplication, QTimer
import sys


app = QApplication()


class Obj(QWidget):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)

        #  # Get the global mouse position
        # global_pos = QCursor.pos()

        # # Extract x and y coordinates
        # x = global_pos.x()
        # y = global_pos.y()

        # print(f"Mouse position: ({x}, {y})")

        QTimer.singleShot(5000, self, app.quit)

    def mouseMoveEvent(self, event):
        pos = event.globalPosition()
        print(pos.x(), pos.y())
        super().mouseMoveEvent(event)


if __name__ == "__main__":
    obj = Obj()
    obj.show()
    app.exec()

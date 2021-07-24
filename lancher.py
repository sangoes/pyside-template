import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from src.views.lancher_widget import LancherWidget

# main
if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = LancherWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

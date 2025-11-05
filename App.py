from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from UI.MainWindowEx import MainWindowEx

qApp=QApplication([])
qmainWindow=QMainWindow()
window=MainWindowEx()
window.setupUi(qmainWindow)
window.show()
qApp.exec()
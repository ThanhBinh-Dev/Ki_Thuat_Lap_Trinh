from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from Chuong4_file.Project85.ui.LoginMainWindowExt import LoginMainWindowExt

app=QApplication(sys.argv)
mainwindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
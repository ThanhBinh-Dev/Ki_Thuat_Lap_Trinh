from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

from Chuong4_file.Project80.ui.MainWindow80Ext import MainWindow80Ext

app=QApplication(sys.argv)
mainwindow=QMainWindow()
myui=MainWindow80Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
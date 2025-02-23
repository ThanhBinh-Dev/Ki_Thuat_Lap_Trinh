from PyQt6.QtWidgets import QApplication, QMainWindow
import sys
from Chuong4_file.Project81.ui.MainWindow81Ext import MainWindow81Ext

app=QApplication(sys.argv)
mainwindow=QMainWindow()
myui=MainWindow81Ext()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
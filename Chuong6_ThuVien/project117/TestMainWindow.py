import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong6_ThuVien.project117.ui.MainWindow117Ext import MainWindow117Ext

app=QApplication(sys.argv)
mainwinddow=QMainWindow()
myui=MainWindow117Ext()
myui.setupUi(mainwinddow)
myui.showWindow()
app.exec()
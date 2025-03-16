import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from Chuong6_ThuVien.project_120.ui.Project120_Ext import Project120ext

app=QApplication(sys.argv)
myui=Project120ext()
myui.showWindow()
app.exec()
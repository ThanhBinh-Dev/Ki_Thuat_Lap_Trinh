from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


from Chuong3_HDT.Bai59.ui.MainWindow59Ex import MainWindow59EX

app=QApplication(sys.argv)
mainwindow=QMainWindow()
myui=MainWindow59EX()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
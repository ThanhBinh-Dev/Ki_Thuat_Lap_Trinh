import numpy as np
from numpy.random import random

from Chuong6_ThuVien.project117.ui.MainWindow117 import Ui_MainWindow


class MainWindow117Ext(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButton_calculate.clicked.connect(self.do_task)
    def do_task(self):
        s=self.lineEdit_Data.text()
        arr=s.split(",")
        print("Arr before casting integer")
        print(arr)
        for i in range(len(arr)):
            arr[i]=int(arr[i])
        print("Arr after casting integer")
        print(arr)
        result=""
        result+="min="+str(np.min(arr))+"\n"
        result+="argmin="+str(np.argmin(arr))+"\n"
        result+="max="+str(np.max(arr))+"\n"
        result+="argmax="+str(np.argmax(arr))+"\n"
        result+="mean="+str(np.mean(arr))+"\n"
        result+="median="+str(np.median(arr))+"\n"
        result+="std="+str(np.std(arr))+"\n"
        self.label_2.setText(result)
from PyQt6.QtWidgets import QMessageBox

from Chuong3_HDT.Bai59.models.PhanSo import PhanSo
from Chuong3_HDT.Bai59.ui.MainWindow59 import Ui_MainWindow


class MainWindow59EX(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.SetupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def SetupSignalAndSlot(self):
        self.pushButton_cong.clicked.connect(self.xuly_cong)
        self.pushButton_tru.clicked.connect(self.xuly_tru)
        self.pushButton_nhan.clicked.connect(self.xuly_nhan)
        self.pushButton_chia.clicked.connect(self.xuly_chia)
    def get_cacphanso(self):
        tu1=int(self.lineEdit_Tu1.text())
        mau1=int(self.lineEdit_Mau1.text())
        tu2=int(self.lineEdit_Tu2.text())
        mau2=int(self.lineEdit_Mau2.text())
        ps1=PhanSo(tu1,mau1)
        ps2=PhanSo(tu2,mau2)
        return ps1,ps2
    def kiemtra(self):
        ps1,ps2 = self.get_cacphanso()
        if ps1.mau==0:
            self.lineEdit_Mau1.clear()
            self.lineEdit_Mau1.setFocus()
            if ps2.mau==0:
                self.lineEdit_Mau2.clear()
        elif ps2.mau==0:
            self.lineEdit_Mau2.clear()
            self.lineEdit_Mau2.setFocus()
        else: pass
    def xuly_cong(self):
        ps1,ps2=self.get_cacphanso()
        self.kiemtra()
        ps3=ps1.cong(ps2).toigian()
        self.lineEdit_Tu3.setText(f"{ps3.tu}")
        self.lineEdit_Mau3.setText(f"{ps3.mau}")
        self.label_Dau.setText("+")
    def xuly_tru(self):
        ps1,ps2=self.get_cacphanso()
        self.kiemtra()
        ps3=ps1.tru(ps2).toigian()
        self.lineEdit_Tu3.setText(f"{ps3.tu}")
        self.lineEdit_Mau3.setText(f"{ps3.mau}")
        self.label_Dau.setText("-")
    def xuly_nhan(self):
        ps1,ps2=self.get_cacphanso()
        self.kiemtra()
        ps3=ps1.nhan(ps2).toigian()
        self.lineEdit_Tu3.setText(f"{ps3.tu}")
        self.lineEdit_Mau3.setText(f"{ps3.mau}")
        self.label_Dau.setText("x")
    def xuly_chia(self):
        ps1,ps2=self.get_cacphanso()
        self.kiemtra()
        if ps2.tu==0:
            self.lineEdit_Tu2.clear()
            self.lineEdit_Tu2.setFocus()
        ps3=ps1.chia(ps2).toigian()
        self.lineEdit_Tu3.setText(f"{ps3.tu}")
        self.lineEdit_Mau3.setText(f"{ps3.mau}")
        self.label_Dau.setText("/")





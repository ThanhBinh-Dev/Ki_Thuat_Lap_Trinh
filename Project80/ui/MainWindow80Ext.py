import functools


from PyQt6.QtWidgets import QPushButton, QMessageBox

from Chuong4_file.Project80.FileFactory import FileFactory
from Chuong4_file.Project80.Model.Product import Product
from Chuong4_file.Project80.ui.MainWindow80 import Ui_MainWindow


class MainWindow80Ext(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.products = []
        self.selected_product = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.scrollAreaWidgetContents.setLayout(self.verticalLayout_Button)
        self.hienthi_sanpham_len_giaodien()
        self.doc_file("database.txt")
        self.setupSignalAndSlot()
    def showWindow(self):
            self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.ProcessSave)
        self.pushButtonRemove.clicked.connect(self.ProcessRemove)
        self.pushButtonAsc.clicked.connect(self.ProcessAsc)
        self.pushButtonDesc.clicked.connect(self.ProcessDesc)
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def hienthi_sanpham_len_giaodien(self):
        self.clearLayout(self.verticalLayout_Button)
        for i in range(len(self.products)):
            sp=self.products[i]
            btn=QPushButton(text=str(sp))
            self.verticalLayout_Button.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet,sp))
    def doc_file(self,filename):
        self.products = []
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(";")
                if len(parts) == 3:
                    product = Product(id=parts[0], name=parts[1], price=float(parts[2]))
                    self.products.append(product)
        self.hienthi_sanpham_len_giaodien()
    def xem_chi_tiet(self,sp):
        self.lineEditId.setText(sp.id)
        self.lineEdit_Name.setText(sp.name)
        self.lineEdit_Price.setText(str(sp.price))
        self.selected_product = sp
    def ProcessSave(self):
        id=self.lineEditId.text()
        name=self.lineEdit_Name.text()
        price=float(self.lineEdit_Price.text())
        product=Product(id,name,price)
        self.products.append(product)
        FileFactory.Writedata("database.txt",product)
        self.hienthi_sanpham_len_giaodien()
    def ProcessRemove(self):
        pro = self.lineEdit_Name.text()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xóa")
        dlg.setText(f"Ê, muốn xóa sản phẩm {pro} hả?")
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()
        if button == QMessageBox.StandardButton.No:
            return  # ngừng hàm xóa, ko làm gì cả
        if self.selected_product in self.products:
            self.products.remove(self.selected_product)
            with open("database.txt", "w", encoding="utf-8") as file:
                for product in self.products:
                    FileFactory.Writedata("database.txt", product)
            self.lineEditId.clear()
            self.lineEdit_Name.clear()
            self.lineEdit_Price.clear()
            self.selected_asset = None
            self.hienthi_sanpham_len_giaodien()
    def ProcessAsc(self):
        n=len(self.products)
        for i in range (n):
            for j in range (n):
                pi = self.products[i]
                pj = self.products[j]
                if pi.price < pj.price:
                    self.products[i] = pj
                    self.products[j] = pi
        self.hienthi_sanpham_len_giaodien()
    def ProcessDesc(self):
        n=len(self.products)
        for i in range (n):
            for j in range (n):
                pi = self.products[i]
                pj = self.products[j]
                if pi.price > pj.price:
                    self.products[i] = pj
                    self.products[j] = pi
        self.hienthi_sanpham_len_giaodien()
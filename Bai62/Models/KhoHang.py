from Chuong3_HDT.Bai62.Models.DanhMuc import DanhMuc
from Chuong3_HDT.Bai62.Models.SanPham import SanPham


class KhoHang:
    def __init__(self):
        self.database=[]
    def add_danhmuc(self,dm):
        self.database.append(dm)
    def fakedata(self):
        dm1 = DanhMuc("DM1", "Laptop")
        dm2 = DanhMuc("DM2", "Laptop")
        dm3 = DanhMuc("DM3", "Tivi")
        self.add_danhmuc(dm1)
        self.add_danhmuc(dm2)
        self.add_danhmuc(dm3)
        dm1.addproduct(SanPham("SP1", "DELL 113", 1100, "Trung Quoc"))
        dm1.addproduct(SanPham("SP2", "LENOVO 796", 900, "Han Quoc"))
        dm1.addproduct(SanPham("SP3", "HP 495", 200, "Trung Quoc"))

        dm2.addproduct(SanPham("SP4", "IPHONE 19 PROMAX", 400, "Meo"))
        dm2.addproduct(SanPham("SP5", "IPAD APPLE 895", 500, "Campuchia"))

        dm3.addproduct(SanPham("SP6", "TIVI ASUS", 7200, "Indonesia"))
    def xuat_danhsach_danhmuc(self):
        for dm in self.database:
            print("-" * 30)
            print(dm)
            print("-" * 30)
            for sp in dm.listproducts:
                print(sp)
    def loc_sanpham_xuatxu(self,xuatxu):
        list_sanphams=[]
        for dm in self.database:
            for sp in dm.listproducts:
                if sp.xuatxu==xuatxu:
                    list_sanphams.append(sp)
        return list_sanphams
    def xoa_sanpham_batky(self,ma):
        for dm in self.database:
            for sp in dm.listproducts:
                if sp.ma==ma:
                    dm.listproducts.remove(sp)
        return dm.listproducts
    def nhapthongtin_danhmuc(self,Mamoi,Tenmoi):
        DMNew=DanhMuc(Mamoi,Tenmoi)
        self.add_danhmuc(DMNew)
    def nhapthongtin_sanpham(self):
        madm=input("Nhập mã danh mục cần thêm sản phẩm: ")
        for dm in self.database:
            if dm.Ma==madm:
                selected_dm=dm
                print("Đã chuyển hướng tới danh mục cần nhập")
                break
            else:
                print("Không tìm thấy danh mục")
        mamoi=input("Nhập mã sản phẩm mới: ")
        tenmoi=input("Nhập tên sản phẩm mới: ")
        giamoi=input("Nhập giá sản phẩm mới: ")
        xuatxumoi=input("Nhập xuất xứ sản phẩm mới: ")
        new_product=SanPham(mamoi,tenmoi,giamoi,xuatxumoi)
        selected_dm.listproducts.append(new_product)
    def capnhap_sanpham(self,ma,mamoi,tenmoi,giamoi,xuatxumoi):
        for dm in self.database:
            for sp in dm.listproducts:
                if sp.ma == ma:
                    sp.ma = mamoi
                    if tenmoi is not None:
                        sp.ten = tenmoi
                    if giamoi is not None:
                        sp.gia = giamoi
                    if xuatxumoi is not None:
                        sp.xuatxu = xuatxumoi
    def thongke_giatrisp(self):
        k=0
        for dm in self.database:
            for sp in dm.listproducts:
                if sp.gia!=0:
                    k+=sp.gia
        print(k)




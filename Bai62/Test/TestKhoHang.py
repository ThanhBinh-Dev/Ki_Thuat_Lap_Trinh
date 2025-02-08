from Chuong3_HDT.Bai62.Models.DanhMuc import DanhMuc
from Chuong3_HDT.Bai62.Models.KhoHang import KhoHang

kho_binhduong=KhoHang()
kho_binhduong.fakedata() #Gia lap 1 so du lieu de thu nghiem
print("Danh sách sản phẩm trong kho bình dương")
kho_binhduong.xuat_danhsach_danhmuc()
i=1
while i==1:
    print("="*50)
    print("Bảng Menu Chức Năng - Nhập số trong ngoặc để thực hiện chức năng")
    print("Nhập thêm thông tin Danh Mục (1)")
    print("Nhập thêm thông tin Sản Phẩm (2)")
    print("Cập nhật thông tin Sản Phẩm (3)")
    print("Xóa sản phẩm (4)")
    print("Thống kê giá trị kho (5)")
    print("Liệt kê sản phẩm theo xuất xứ (6)")
    print("Thoát (7)")
    print("="*50)
    p=int(input("Nhập chức năng muốn thực hiện: "))
    if p==1:
        i=1
        Mamoi=input("Nhập Mã Danh Mục mới: ")
        Tenmoi=input("Nhập Tên Danh Mục mới: ")
        DanhMucMoi=DanhMuc(Mamoi,Tenmoi)
        kho_binhduong.add_danhmuc(DanhMucMoi)
        print("Danh sách mới")
        kho_binhduong.xuat_danhsach_danhmuc()
    if p==2:
        i=1
        kho_binhduong.nhapthongtin_sanpham()
        print("Danh sach sau cap nhat")
        kho_binhduong.xuat_danhsach_danhmuc()
    if p==3:
        i=1
        ma=input("Mã sản phẩm cần cập nhật: ")
        mamoi=input("Nhập mã sản phẩm mới: ")
        tenmoi=input("Nhập tên sản phẩm mới: ")
        giamoi=input("Nhập giá sản phẩm mới: ")
        xuatxumoi=input("Nhập xuất xứ sản phẩm mới: ")
        kho_binhduong.capnhap_sanpham(ma,mamoi,tenmoi,giamoi,xuatxumoi)
        print("Danh sách sau cập nhật")
        kho_binhduong.xuat_danhsach_danhmuc()
    if p==4:
        i==1
        MaXoa=input("Nhập mã sản phẩm cần xóa: ")
        kho_binhduong.xoa_sanpham_batky(MaXoa)
        print("Danh sách sau xóa sản phẩm SP1")
        kho_binhduong.xuat_danhsach_danhmuc()
    if p==5:
        i==1
        print("Tổng giá trị của các mặt hàng:", end="")
        kho_binhduong.thongke_giatrisp()
    if p==6:
        i==1
        xuatxu=input("Nhập xuất xứ cần tìm")
        lsp=kho_binhduong.loc_sanpham_xuatxu(xuatxu)
        print(f"Các sản phẩm có xuất sứ từ {xuatxu}")
        for sp in lsp:
           print(sp)
    if p==7:
        i==0
        print("CẢM ƠN ĐÃ SỬ DỤNG")
        break














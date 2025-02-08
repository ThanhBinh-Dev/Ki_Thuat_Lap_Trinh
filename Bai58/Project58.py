from Chuong3_HDT.Bai58.NhanVien import Nhanvien

Ho1=input("Nhập họ nhân viên 1: ")
Ten1=input("Nhập tên nhân viên 1:")
Sosanpham1=int(input("Nhập số sản phẩm nhân viên 1: "))
nv1=Nhanvien(Ho1,Ten1,Sosanpham1)

Ho2=input("Nhập họ nhân viên 2: ")
Ten2=input("Nhập tên nhân viên 2:")
Sosanpham2=int(input("Nhập số sản phẩm nhân viên 2: "))
nv2=Nhanvien(Ho2,Ten2,Sosanpham2)

print("="*50)
print(nv1)
print(nv2)
print("="*50)

i=1
while i==1:
    print("Bảng Menu - Nhấn kí tự trong ngoặc để thực hiện tính năng")
    print("Tính lương nhân viên (l)")
    print("So sánh lương nhân viên (ss)")
    print("Dừng (x)")
    f = input("Nhập chức năng: ")
    if f=="l":
        print("=" * 50)
        nv1.inluong()
        nv2.inluong()
        print("=" * 50)
        i=1
    elif f=="ss":
        print("=" * 50)
        nv1.inluong()
        nv2.inluong()
        print("Kết quả so sánh số sản phẩm nhân viên 1 có lớn hơn nhân viên 2 là: ")
        nv1.set_nv2(nv2)
        nv1.Result_Ishigher(nv2)
        print("=" * 50)
        i = 1
    elif f=="x":
        print("=" * 50)
        print("CẢM ƠN")
        print("=" * 50)
        i = 0
    else:
        print("=" * 50)
        print("Vui lòng chọn lại chức năng bạn muốn dùng")
        print("=" * 50)
        i = 1



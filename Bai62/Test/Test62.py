from Chuong3_HDT.Bai62.Models.DanhMuc import DanhMuc
from Chuong3_HDT.Bai62.Models.SanPham import SanPham

kho_hang=[]
dm1=DanhMuc("DM1","Laptop")
dm2=DanhMuc("DM2","Laptop")
dm3=DanhMuc("DM3","Tivi")
kho_hang.extend([dm1,dm2,dm3])
print("Danh sach danh muc san pham trong kho hang")
for dm in kho_hang:
    print(dm)
dm1.addproduct(SanPham("SP1","DELL 113",1100,"Trung Quoc"))
dm1.addproduct(SanPham("SP2","LENOVO 796",900,"Han Quoc"))
dm1.addproduct(SanPham("SP3","HP 495",200,"Trung Quoc"))

dm2.addproduct(SanPham("SP4","IPHONE 19 PROMAX",400,"Meo"))
dm2.addproduct(SanPham("SP5","IPAD APPLE 895",500,"Campuchia"))

dm3.addproduct(SanPham("SP6","DELL 113",7200,"Indonesia"))
print("*"*50)
print("San pham phan loai theo danh muc:")
for dm in kho_hang:
    print("-"*30)
    print(dm)
    print("-" * 30)
    for sp in dm.listproducts:
        print(sp)
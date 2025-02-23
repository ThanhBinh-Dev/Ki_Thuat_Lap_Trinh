from Chuong4_file.Project85.Library.Dataconnector import DataConnector

dc=DataConnector()
# Lấy toàn bộ nhân viên:
employees=dc.get_all_employees()
print("Danh sách nhân viên:")
for e in employees:
    print(e)

# Laấy toàn bộ tài sản
assets=dc.get_all_assets()
print("Danh sách tài sản:")
for a in assets:
    print(a)
aes=dc.get_all_employee_assets()
print("Danh sách pha công quản lý tài sản:")
for ae in aes:
    print(ae)

# Tét Chức năng đăng nhập hệ thống
uid="ti"
pwd="545"
emp=dc.login(uid,pwd)
if emp!=None:
    print("Dang nhap thanh cong")
else:
    print("Dang nhap that bai")
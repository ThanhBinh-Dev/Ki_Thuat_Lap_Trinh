from Chuong4_file.Project85.Library.JsonFileFactory import JsonFileFactory
from Chuong4_file.Project85.Model.Employee_asset import Employee_Asset

jff=JsonFileFactory()
filename="../Dataset/employee_assets.json"
eas=jff.read_data(filename,Employee_Asset)
print("Danh sách phân công quản lý tài sản độc từ file:")
for ea in eas:
    print(ea)
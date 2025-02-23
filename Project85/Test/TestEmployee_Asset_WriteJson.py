from Chuong4_file.Project85.Library.JsonFileFactory import JsonFileFactory
from Chuong4_file.Project85.Model.Employee_asset import Employee_Asset

eas=[]
eas.append(Employee_Asset("E1","AS1","Main"))
eas.append(Employee_Asset("E2","AS2","Main"))
eas.append(Employee_Asset("E3","AS3","Main"))
eas.append(Employee_Asset("E4","AS4","Main"))
eas.append(Employee_Asset("E5","AS5","Main"))
eas.append(Employee_Asset("E6","AS6","Main"))
eas.append(Employee_Asset("E1","AS3","Main"))
eas.append(Employee_Asset("E1","AS7","Main"))
eas.append(Employee_Asset("E3","AS2","Main"))
eas.append(Employee_Asset("E5","AS5","Main"))
eas.append(Employee_Asset("E4","AS3","Main"))

print("Danh sách phân công quản lý tài sản:")
for ea in eas:
    print(ea)

jff=JsonFileFactory()
filename="../Dataset/employee_assets.json"
jff.write_data(eas,filename)

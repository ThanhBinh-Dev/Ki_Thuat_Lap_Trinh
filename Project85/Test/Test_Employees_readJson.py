from Chuong4_file.Project85.Library.JsonFileFactory import JsonFileFactory
from Chuong4_file.Project85.Model.Employee import Employee

jff=JsonFileFactory()
filename="../Dataset/employees.json"
employees=jff.read_data(filename,Employee)
print("Danh sách Employees sau khi đọc file:")
for e in employees:
    print(e)
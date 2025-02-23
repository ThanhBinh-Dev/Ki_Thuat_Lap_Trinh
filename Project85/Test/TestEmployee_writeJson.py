from Chuong4_file.Project85.Library.JsonFileFactory import JsonFileFactory
from Chuong4_file.Project85.Model.Employee import Employee

employees=[]
employees.append(Employee("E1","Tèo","teo","123"))
employees.append(Employee("E2","Tí","ti","545"))
employees.append(Employee("E3","Tủn","tun","456"))
employees.append(Employee("E4","Bin","bin","789"))
employees.append(Employee("E5","Bo","bo","12/"))
employees.append(Employee("E6","Nu","nu","123dfs"))
employees.append(Employee("E7","Na","na","234sdf"))

print("Danh sách Employee:")
for e in employees:
    print(e)
jff=JsonFileFactory()
filename="../Dataset/employees.json"
jff.write_data(employees,filename)

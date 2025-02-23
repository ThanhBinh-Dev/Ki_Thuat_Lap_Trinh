from Chuong4_file.Project85.Library.JsonFileFactory import JsonFileFactory
from Chuong4_file.Project85.Model.Employee import Employee
from Chuong4_file.Project85.Model.Asset import Asset
from Chuong4_file.Project85.Model.Employee_asset import Employee_Asset



class DataConnector:
    def get_all_employees(self):
        jff = JsonFileFactory()
        filename = "../Dataset/employees.json"
        employees = jff.read_data(filename, Employee)
        return employees
    def get_all_assets(self):
        jff = JsonFileFactory()
        filename = "../Dataset/assets.json"
        assets = jff.read_data(filename, Asset)
        return assets
    def get_all_employee_assets(self):
        jff = JsonFileFactory()
        filename = "../Dataset/employee_assets.json"
        eas = jff.read_data(filename, Employee_Asset)
        return eas
    def login(self,username,password):
        employees=self.get_all_employees()
        for e in employees:
            if e.UserName == username and e.Password == password:
                return e
        return None
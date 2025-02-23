import functools
import xml.etree.ElementTree as ET
from PyQt6.QtWidgets import QPushButton

from Chuong4_file.Project81.Employee import Employee
from Chuong4_file.Project81.ui.MainWindow81 import Ui_MainWindow


class MainWindow81Ext(Ui_MainWindow):
    def __init__(self):
        self.employees=[]
        self.selected_emp=None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
        self.doc_file_xml("employees.xml")
        self.hienthi_nhanvien_len_giaodien()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.ProcessSave)
        self.pushButtonRemove.clicked.connect(self.ProcessRemove)
        self.pushButtonsearch.clicked.connect(self.ProcessSearch)
        self.pushButtonSort.clicked.connect(self.ProcessSort)
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def hienthi_nhanvien_len_giaodien(self):
        self.clearLayout(self.verticalLayout_Button)
        for i in range(len(self.employees)):
            sp=self.employees[i]
            btn=QPushButton(text=str(sp))
            self.verticalLayout_Button.addWidget(btn)
            btn.clicked.connect(functools.partial(self.xem_chi_tiet,sp))
    def doi_mau_button(self, emp_id):
        for i in range(self.verticalLayout_Button.count()):
            widget = self.verticalLayout_Button.itemAt(i).widget()
            if isinstance(widget, QPushButton):
                if emp_id in widget.text():
                    widget.setStyleSheet("background-color: yellow; color: black; ")
                else:
                    widget.setStyleSheet("")
    def doc_file_xml(self,filename):
        self.employees=[]
        tree=ET.parse(filename)
        root=tree.getroot()
        for emp in root.findall("employee"):
            id_ = emp.find("id").text
            name = emp.find("name").text
            self.employees.append(Employee(id_, name))
        self.hienthi_nhanvien_len_giaodien()
    def xem_chi_tiet(self,sp):
        self.lineEditId.setText(sp.id)
        self.lineEdit_Name.setText(sp.name)
        self.selected_emp = sp
    def ProcessSave(self):
        tree = ET.parse("employees.xml")
        root = tree.getroot()
        emp = ET.Element("employee")
        empId = ET.Element("id")
        empId.text = self.lineEditId.text()
        emp.append(empId)
        empName = ET.Element("name")
        empName.text = self.lineEdit_Name.text()
        emp.append(empName)
        root.append(emp)
        tree.write('employees.xml', encoding='utf-8')
        self.doc_file_xml("employees.xml")
    def ProcessRemove(self):
        tree = ET.parse("employees.xml")
        root = tree.getroot()
        itemDelete = None
        for item in root.findall('employee'):
            id = item.find("id").text.strip()
            if id == self.selected_emp.id:
                itemDelete = item
                break
        if itemDelete != None:
            root.remove(itemDelete)
            tree.write('employees.xml', encoding='utf-8')
            self.doc_file_xml("employees.xml")
            self.lineEditId.clear()
            self.lineEdit_Name.clear()
            self.selected_emp = None
    def ProcessSearch(self):
        id_search = self.lineEditId.text().strip()  # Lấy ID nhập vào
        if not id_search:
            pass
        found = None  # Biến lưu nhân viên tìm thấy
        for emp in self.employees:
            if emp.id == id_search:
                found = emp
                break
        if found:
            self.doi_mau_button(found.id)
    def ProcessSort(self):
        self.employees.sort(key=lambda emp: int(emp.id))
        self.hienthi_nhanvien_len_giaodien()
        self.update_file_xml("employees.xml")

    def update_file_xml(self, filename):
        root = ET.Element("employees")

        for emp in self.employees:
            emp_element = ET.Element("employee")

            emp_id = ET.Element("id")
            emp_id.text = emp.id
            emp_element.append(emp_id)

            emp_name = ET.Element("name")
            emp_name.text = emp.name
            emp_element.append(emp_name)

            root.append(emp_element)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
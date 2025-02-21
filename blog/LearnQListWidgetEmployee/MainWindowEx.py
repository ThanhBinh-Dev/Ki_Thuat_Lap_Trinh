import json
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QListWidgetItem, QMessageBox
import os.path
from blog.LearnQListWidgetEmployee.Employee import Employee
from blog.LearnQListWidgetEmployee.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.dataset=[]
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButton_new.clicked.connect(self.processNew)
        self.pushButton_save.clicked.connect(self.processSave)
        self.listWidgetEmployee.itemSelectionChanged.connect(self.processItemSelectionChanged)
        self.pushButton_delete.clicked.connect(self.processDelete)
        self.pushButton_close.clicked.connect(self.processClose)
        self.readEmployeeFromJson()
    def show(self):
        self.MainWindow.show()
    def processNew(self):
        self.lineEditname.setText("")
        self.lineEdit_email.setText("")
        self.lineEditname.setFocus()
    def processSave(self):
        insertEmployee=Employee(self.lineEditname.text(),self.lineEdit_email.text(),self.radioButonWoman.isChecked())
        isDuplicated=False
        for i in range(0,self.listWidgetEmployee.count()):
            item=self.listWidgetEmployee.item(i)
            data=item.data(Qt.ItemDataRole.UserRole)
            if insertEmployee.email.lower()==data.email.lower():
                isDuplicated=True
                break
        if not isDuplicated:
            item=QListWidgetItem()
        item.setData(Qt.ItemDataRole.UserRole,insertEmployee)
        item.setText(str(insertEmployee))
        item.setCheckState(Qt.CheckState.Unchecked)
        if self.radioButonWoman.isChecked():
            item.setIcon(QIcon("Images/female.ico"))
        else:
            item.setIcon(QIcon("Images/male.ico"))
        if not isDuplicated:
            self.listWidgetEmployee.addItem(item)
        self.writeEmployeeToJson()
    def processItemSelectionChanged(self):
        current_row=self.listWidgetEmployee.currentRow()
        if current_row<0:
            return
        item=self.listWidgetEmployee.item(current_row)
        emp=item.data(Qt.ItemDataRole.UserRole)
        self.lineEditname.setText(emp.name)
        self.lineEdit_email.setText(emp.email)
        if emp.gender==True:
            self.radioButonWoman.setChecked(True)
        else:
            self.radioButtonMan.setChecked(True)
    def processDelete(self):
        answer = QMessageBox.question(
            self.MainWindow,
            'Confirmation',
            'Do you want to remove checked Items?',
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )
        if answer == QMessageBox.StandardButton.No:
            return
        for index in range(self.listWidgetEmployee.count()-1,-1,-1):
            item=self.listWidgetEmployee.item(index)
            if item.checkState()==Qt.CheckState.Checked:
                current_item = self.listWidgetEmployee.takeItem(index)
                del current_item
        self.processNew()
        self.writeEmployeeToJson()
    def processClose(self):
        msg = QMessageBox()
        msg.setText(f"Are you sure you want to exit ?")
        msg.setWindowTitle("Exit Confirmation")
        msg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        msg.setStandardButtons(buttons)
        result = msg.exec()
        if result == QMessageBox.StandardButton.Yes:
           self.MainWindow.close()
    def writeEmployeeToJson(self):
        dataset=[]
        for i in range(0,self.listWidgetEmployee.count()):
            item=self.listWidgetEmployee.item(i)
            emp=item.data(Qt.ItemDataRole.UserRole)
            dataset.append(emp)
        jsonString=json.dumps([emp.__dict__ for emp in dataset])
        jsonFile=open("database.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
    def readEmployeeFromJson(self):
        if os.path.isfile("database.json") ==False:
            return
        file = open('database.json', "r")
        # Reading from file
        self.dataset = json.loads(file.read(), object_hook=lambda d: Employee(**d))
        file.close()
        for emp in self.dataset:
            item = QListWidgetItem()
            item.setData(Qt.ItemDataRole.UserRole, emp)
            item.setText(str(emp))
            item.setCheckState(Qt.CheckState.Unchecked)
            if emp.gender==True:
                item.setIcon(QIcon("images/ic_woman.png"))
            else:
                item.setIcon(QIcon("images/ic_man.png"))
            self.listWidgetEmployee.addItem(item)
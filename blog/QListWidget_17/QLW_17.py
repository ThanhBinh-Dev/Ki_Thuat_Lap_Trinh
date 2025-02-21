import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QGridLayout, QListWidget, QListWidgetItem, QPushButton, QApplication, QInputDialog


class MainWindow(QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.setWindowTitle("QListWidgetDemo_DuongThanhBinh_K244060766")
        self.setWindowIcon(QIcon("K244060766.jpg"))
        self.setGeometry(100,100,400,100)
        layout=QGridLayout(self)
        self.setLayout(layout)
        self.listWidget=QListWidget(self)
        # Tạo QlistWidgetItem và set thuộc tính
        newItem=QListWidgetItem()
        newItem.setText("Metaverse")
        newItem.setIcon(QIcon("metaverse.png"))
        newItem.setForeground(Qt.GlobalColor.red)
        newItem.setBackground(Qt.GlobalColor.yellow)
        self.listWidget.addItem(newItem)
        #Tạo mới QListWidgetItem
        self.listWidget.addItem(newItem)
        #Thêm phần tử mới cho QListWidgetItem mới
        self.listWidget.addItem("Smart Contract")
        # Đặt SmartContract ở dòng 1 và set icon
        self.listWidget.item(1).setIcon(QIcon('container.png'))
        # TẠo mảng cho QListWidget
        self.listWidget.addItems(["Learn Python", "Machine Learning", "Deep Learning"])
        layout.addWidget(self.listWidget, 0, 0, 5, 1)
        # Tạo nút và signal slot cho các nút:
        add_button = QPushButton('Add New Item')
        add_button.clicked.connect(self.addItem)

        update_button = QPushButton('Update Item')
        update_button.clicked.connect(self.updateItem)

        insert_button = QPushButton('Insert New Item')
        insert_button.clicked.connect(self.insertItem)

        remove_button = QPushButton('Remove Selected Item')
        remove_button.clicked.connect(self.removeItem)

        clear_button = QPushButton('Clear All')
        clear_button.clicked.connect(self.clearAll)

        layout.addWidget(add_button, 0, 1)
        layout.addWidget(update_button, 1, 1)
        layout.addWidget(insert_button, 2, 1)
        layout.addWidget(remove_button, 3, 1)
        layout.addWidget(clear_button, 4, 1)
        # tín hiệu chuột cho QListWidger
        self.listWidget.itemClicked.connect(self.processItemClicked)
        self.listWidget.itemDoubleClicked.connect(self.processItemDoubleClicked)
        # Signal chọn phần tử trong list
        self.listWidget.itemSelectionChanged.connect(self.processItemSelectionChanged)
        # hiện window
        self.show()
        # Hiện thị tên đối tượng được chọn được vào làm tiêu các thẻ tương tác khi nhấn các nút tính năng
    def processItemSelectionChanged(self):
        current_row = self.listWidget.currentRow()
        item = self.listWidget.item(current_row)
        self.setWindowTitle(item.text())
        # hiện thị giao diện update item khi double click vào đối tượng trong QListWidget

    def processItemDoubleClicked(self):
        self.updateItem()
        # chọn item

    def processItemClicked(self):
        current_row = self.listWidget.currentRow()
        data = self.listWidget.item(current_row)
        print("itemClicked=", data.text())
    # Hiển thị đối tượng được chọn khi click vào
    # Hàm xử lý thêm
    def addItem(self):
        text, ok = QInputDialog.getText(self, 'Add a New Data', 'New Data:')
        if ok and text:
            self.listWidget.addItem(text)

        # Hàm xử lý update

    def updateItem(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 0:
            item = self.listWidget.item(current_row)
            text, ok = QInputDialog.getText(self, 'Update Data', 'New Data:', text=item.text())
            if ok and text:
                item.setText(text)

        # Hàm xử lý thêm

    def insertItem(self):
        text, ok = QInputDialog.getText(self, 'Insert a New Data', 'New Data:')
        if ok and text:
            current_row = self.listWidget.currentRow()
            self.listWidget.insertItem(current_row + 1, text)

    # Hàm xử lý xóa
    def removeItem(self):
        current_row = self.listWidget.currentRow()
        if current_row >= 0:
            current_item = self.listWidget.takeItem(current_row)
            del current_item
        # slot to remove all item from QListWidget
    # Hàm xử lý xóa hết
    def clearAll(self):
        self.listWidget.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
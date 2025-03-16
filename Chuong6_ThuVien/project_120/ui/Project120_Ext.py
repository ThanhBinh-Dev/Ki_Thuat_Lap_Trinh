import pandas as pd
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem

from Chuong6_ThuVien.project_120.ui.Project120 import Ui_MainWindow


class Project120ext(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_data()
        self.setupSignalAndSlot()
    def showWindow(self):
        self.show()
    def setupSignalAndSlot(self):
        self.pushButton_close.clicked.connect(self.filter_close)
        self.pushButton_low.clicked.connect(self.filter_low)
        self.pushButton_ngay.clicked.connect(self.filter_by_date)
        self.tableWidget.cellClicked.connect(self.on_cell_clicked)
    def load_data(self):
        try:
            self.df = pd.read_csv("./Dataset/TCB_2018_2020.csv")
            self.display_data(self.df)
        except FileNotFoundError:
            print("Không tìm thấy file CSV.")
    def display_data(self, df):
        if df.empty:
            self.tableWidget.setRowCount(0)
            return
        self.tableWidget.setRowCount(len(df))
        self.tableWidget.setColumnCount(len(df.columns))
        self.tableWidget.setHorizontalHeaderLabels(df.columns)
        for row, rowData in enumerate(df.itertuples(index=False, name=None)):
            for col, data in enumerate(rowData):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(data)))
    def on_cell_clicked(self, row, col):
        if self.df is None or self.df.empty:
            return
        # Lấy dữ liệu từng cột theo hàng được chọn
        date = str(self.df.iloc[row, 0])
        high = str(self.df.iloc[row, 1])
        low = str(self.df.iloc[row, 2])
        open_price = str(self.df.iloc[row, 3])
        close = str(self.df.iloc[row, 4])
        avg = str(self.df.iloc[row, 5])
        volume = str(self.df.iloc[row, 6])
        # Hiển thị vào các QLineEdit trong groupBox "Details"
        self.lineEditDate.setText(date)
        self.lineEdit_High.setText(high)
        self.lineEdit_low.setText(low)
        self.lineEdit_open.setText(open_price)
        self.lineEdit_close.setText(close)
        self.lineEdit_avg.setText(avg)
        self.lineEdit_volumn.setText(volume)
    def filter_close(self):
        try:
            x = float(self.lineEdit_close1.text())
            y = float(self.lineEdit_close2.text())
            filtered_df = self.df[(self.df['Close'] < x) & (self.df['Close'] > y)]
            self.display_data(filtered_df)
        except ValueError:
            print("Vui lòng nhập giá trị số hợp lệ cho Close.")
    def filter_low(self):
        try:
            x = float(self.lineEdit_theolow.text())
            y = float(self.lineEdit_theolow_2.text())
            filtered_df = self.df[['Date', 'High', 'Low']][(self.df['Low'] >= x) & (self.df['Low'] <= y)]
            self.display_data(filtered_df)
        except ValueError:
            print("Vui lòng nhập giá trị số hợp lệ cho Low.")
    def filter_by_date(self):
        date_input = self.lineEdit_theongay.text().strip()
        date_list = [date.strip() for date in date_input.split(",")]
        filtered_df = self.df[self.df['Date'].astype(str).isin(date_list)]
        if filtered_df.empty:
            print("Không tìm thấy dữ liệu cho các ngày đã nhập.")
        self.display_data(filtered_df)


from PyQt6.QtWidgets import QMessageBox

from blog.LearnQTableWidger.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.tableWidget.itemSelectionChanged.connect(self.processSelectedItem)
        self.pushButtonClose.clicked.connect(self.processClose)
    def processSelectedItem(self):
        row=self.tableWidget.currentRow()
        songId=self.tableWidget.item(row,0)
        songName=self.tableWidget.item(row,1)
        singer=self.tableWidget.item(row,2)
        self.lineEditID.setText(songId.text())
        self.lineEdit_Name.setText(songName.text())
        self.lineEdit_Singer.setText(singer.text())
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
    def show(self):
        self.MainWindow.show()
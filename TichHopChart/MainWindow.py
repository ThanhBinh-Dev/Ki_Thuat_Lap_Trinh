# Form implementation generated from reading ui file 'D:\DTB\uel\HK1\tu duy lap trinh\DuongThanhBinh_K244060766_Module28\Chuong6_ThuVien\TichHopChart\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 547)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_bar = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_bar.setGeometry(QtCore.QRect(20, 20, 101, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\Chuong6_ThuVien\\TichHopChart\\Images/ic_barchart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_bar.setIcon(icon)
        self.pushButton_bar.setObjectName("pushButton_bar")
        self.pushButton_line = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_line.setGeometry(QtCore.QRect(140, 20, 101, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\Chuong6_ThuVien\\TichHopChart\\Images/ic_linechart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_line.setIcon(icon1)
        self.pushButton_line.setObjectName("pushButton_line")
        self.pushButton_pie = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_pie.setGeometry(QtCore.QRect(260, 20, 101, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\Chuong6_ThuVien\\TichHopChart\\Images/ic_piechart.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_pie.setIcon(icon2)
        self.pushButton_pie.setObjectName("pushButton_pie")
        self.pushButton_exit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_exit.setGeometry(QtCore.QRect(440, 20, 91, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("D:\\DTB\\uel\\HK1\\tu duy lap trinh\\DuongThanhBinh_K244060766_Module28\\Chuong6_ThuVien\\TichHopChart\\Images/ic_shutdown.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButton_exit.setIcon(icon3)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 511, 421))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DuongThanhBinh-K244060766"))
        self.pushButton_bar.setText(_translate("MainWindow", "Bar Chart"))
        self.pushButton_line.setText(_translate("MainWindow", "Line Chart"))
        self.pushButton_pie.setText(_translate("MainWindow", "Pie Chart"))
        self.pushButton_exit.setText(_translate("MainWindow", "Exit"))
        self.groupBox.setTitle(_translate("MainWindow", "Chart Visualization"))

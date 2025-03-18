import sys
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from Chuong6_ThuVien.TichHopChart.MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupPlot()
        self.pushButton_bar.clicked.connect(self.showBarChart)
        self.pushButton_line.clicked.connect(self.showLinePlotChart)
        self.pushButton_pie.clicked.connect(self.showPieChart)
        self.pushButton_exit.clicked.connect(self.processExit)
    def show(self):
        self.MainWindow.show()
    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)
        self.verticalLayout.addWidget(self.toolbar)
        # adding canvas to the layout
        self.verticalLayout.addWidget(self.canvas)
    def showBarChart(self):
        df = pd.read_csv('./data/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style="plain")
        ax.grid()
        ax.bar(df["Year"],df["VNM"])
        ax.set_title("Bar chart title")
        #ax.set_xlabel(columnX)
        #ax.set_ylabel(columnY)
        self.canvas.draw()
    def showLinePlotChart(self):
        df = pd.read_csv('./data/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False,style="plain")
        ax.grid()
        sns.lineplot(data=df,x="Year", y="VNM", marker='o', color='orange')
        ax.set_xlabel("Year")
        ax.set_ylabel("VNM")
        ax.set_title("SNS Line Plot Title")
        ax.legend(loc ='lower right')
        self.canvas.draw()
    def showPieChart(self):
        df = pd.read_csv('./data/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.pie(df["Year"], labels=df["VNM"], autopct='%1.2f%%')
        ax.legend(df["Year"],loc ='lower right')
        ax.set_title("Pie Chart Title")
        self.canvas.draw()
    def processExit(self):
        sys.exit(0)
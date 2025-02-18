from Chuong4_file.pickle_file.util.FileUtil import FileUtil

list=FileUtil.loadModel("mydata.dat")
for sp in list:
    print(sp)
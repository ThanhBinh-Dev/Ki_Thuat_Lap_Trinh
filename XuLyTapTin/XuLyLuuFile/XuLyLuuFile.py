def LuuFile(path):
    file=open(path,'w',encoding="utf-8")
    file.writelines("SV001;Trần Thị Tẹt; 1/1/1998\n")
    file.writelines("SV002;Hồ Thị Tủn; 2/2/1999\n")
    file.writelines("SV003;Phạm Văn Thẹo; 3/3/1999\n")
    file.close()
LuuFile("csdlsinhvien.txt")
# a: Nối đuôi
# r: Đọc file

from XuLyFile import *

masp=input("Nhập mã SP: ")
tensp=input("Nhập tên SP: ")
dongia=float(input("Nhập giá:"))
line=masp+";"+tensp+";"+str(dongia)
LuuFile("database.txt",line)
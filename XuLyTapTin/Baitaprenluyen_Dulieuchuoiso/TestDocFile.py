from XuLyFIle import *
arrSo=DocFile("csdl_so.txt")
print(arrSo)
def XuatSoAmTrenMoiDong(arrSo):
    for row in arrSo:
        for element in row:
            number=int(element)
            if number<0:
                print(number,end='\t')
        print()
print("Các só âm trên mỗi dòng")
XuatSoAmTrenMoiDong(arrSo)
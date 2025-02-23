from Chuong4_file.Project85.Library.JsonFileFactory import JsonFileFactory
from Chuong4_file.Project85.Model.Asset import Asset

assets=[]
assets.append(Asset("AS1","Máy chiếu 1",2017,10))
assets.append(Asset("AS2","Máy chiếu 2",2017,8))
assets.append(Asset("AS3","Máy tính 1",2024,15))
assets.append(Asset("AS4","Máy tính 2",2019,20))
assets.append(Asset("AS5","Máy ảnh 1",2018,5))
assets.append(Asset("AS6","Máy ảnh 2",2020,50))
assets.append(Asset("AS7","Xe hơi",2012,100))

print("Danh sách tài sản")
for a in assets:
    print(a)
jff=JsonFileFactory()
filename="../Dataset/assets.json"
jff.write_data(assets,filename)
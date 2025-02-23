from Chuong4_file.Project85.Library.JsonFileFactory import JsonFileFactory
from Chuong4_file.Project85.Model.Asset import Asset

jff=JsonFileFactory()
filename="../Dataset/assets.json"
assets=jff.read_data(filename,Asset)
print("Tài sản sau khi đọc File")
for a in assets:
    print(a)
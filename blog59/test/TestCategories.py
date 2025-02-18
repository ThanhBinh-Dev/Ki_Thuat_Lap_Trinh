from Chuong4_file.blog59.models.Categories import Categories
from Chuong4_file.blog59.models.Category import Category
from Chuong4_file.blog59.models.Product import Product
from Chuong4_file.blog59.utils.JsonFactory import JsonFactory



#Bước 1: Tạo một đối tượng database có kiểu Categories()
database=Categories()

#Bước 2: Tạo danh mục 1 và các sản phẩm liên quan
cate1=Category("c1","phone")
cate1.add_product(Product("p1","Samsung 1",100))
cate1.add_product(Product("p2","Samsung 2",400))
cate1.add_product(Product("p3","Samsung 3",200))

#Bước 3: Tạo danh mục 2 và các sản phẩm liên quan
cate2=Category("c2","computer")
cate2.add_product(Product("p4","DELL 1",2500))
cate2.add_product(Product("p5","DELL 2",3561))
cate2.add_product(Product("p6","DELL 3",4560))

#Bước 4: Tạo danh mục 3 và các sản phẩm liên quan
cate3=Category("c3","television")
cate3.add_product(Product("p7","Tele 1",6324))
cate3.add_product(Product("p8","Tele 2",1203))
cate3.add_product(Product("p9","Tele 3",2536))

#Bước 5: Đưa các danh mục vào database
database.add_cate(cate1)
database.add_cate(cate2)
database.add_cate(cate3)

#Bước 6: Xuất toàn bộ Danh sách dữ liệu mẫu:
database.print_all_categories()

#Bước 7: Parse đối tượng ra Json:
json_data = JsonFactory.parse_json(database)
print(json_data)

#Bước 8: Restore lại đối tượng từ Json:
restoreObject= JsonFactory.restore_object(json_data)
print("Dữ liệu sau khi Restore từ Json:")
restoreObject.print_all_categories()

#Bước 9: Gọi hàm serialize để chụp dữ liệu xuống ổ cứng với định dạng Json:
JsonFactory.serialize(database,"../assets/database.json")
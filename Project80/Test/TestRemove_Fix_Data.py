from Chuong3_HDT.Overloading.Product import Product
from Chuong4_file.Project80.FileFactory import FileFactory

products=FileFactory.Readdata("database.txt")
def fixData(id):
    found = False
    for product in products:
        if product.id == id:
            print(f"Sản phẩm cũ: {product.id} - {product.name} - {product.price}")
            product.name = input("Nhập tên sp mới: ").strip()
            product.price = float(input("Nhập giá sp mới: ").strip())

            found = True
            break

    if found:
        with open("database.txt", "w", encoding="utf-8") as file:
            for p in products:
                file.write(f"{p.id};{p.name};{p.price}\n")
        print("Cập nhật sản phẩm thành công!")
    else:
        print("Không tìm thấy sản phẩm có ID:", id)
fixData(str(112))
def RemoveData(id):
    for product in products:
        if product.id == id:
            products.remove(product)
            with open("database.txt", "w", encoding="utf-8") as file:
                for product in products:
                    FileFactory.Writedata("database.txt", product)
            print("Đã xóa thành công")
            break
        else:
            print("Không tìm thấy id")
            break
RemoveData("12")

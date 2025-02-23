from Chuong4_file.Project80.FileFactory import FileFactory
from Chuong4_file.Project80.Model.Product import Product

print("Input Products:")
while True:
    id=input("Input Product ID:")
    name=input("Input Product Name:")
    price=float(input("Input Product Price:"))
    product=Product(id,name,price)
    FileFactory.Writedata("database.txt",product)
    ans=input("Do you want to continue?(y/n)")
    if ans=="n" or ans=="N":
        break
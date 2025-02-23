from Chuong4_file.Project80.FileFactory import FileFactory

products=FileFactory.Readdata("database.txt")
def printProducts(products):
    for product in products:
        print(product)
    print()
printProducts(products)
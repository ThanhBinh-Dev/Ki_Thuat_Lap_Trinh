from Chuong4_file.Project80.FileFactory import FileFactory

products=FileFactory.Readdata("database.txt")
def printProducts(products):
    for product in products:
        print(product)
    print()
def  sortProductsIncrease(products):
    for i in range (len(products)):
        for j in range(len(products)):
            pi=products[i]
            pj=products[j]
            if pi.price<pj.price:
                products[i]=pj
                products[j]=pi
def updateDatabase(filename, products):
    with open(filename, "w", encoding="utf-8") as file:
        for product in products:
            FileFactory.Writedata(filename, product)
sortProductsIncrease(products)
updateDatabase("database.txt", products)
print("Products after UnitPrice Sorting:")
printProducts(products)
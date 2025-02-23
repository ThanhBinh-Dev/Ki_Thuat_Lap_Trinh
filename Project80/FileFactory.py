import traceback

from Chuong4_file.Project80.Model.Product import Product


class FileFactory:
    @staticmethod
    def Writedata(path,product):
        try:
            line = (product.id +";" + product.name + ";" +
                    str(product.price))
            file=open(path,'a',encoding='utf-8')
            file.writelines(line)
            file.writelines("\n")
            file.close()
            return True
        except:
            traceback.print_exc()
            return False
    @staticmethod
    def Readdata(path):
        products=[]
        try:
            file = open(path, 'r', encoding='utf-8')
            for line in file:
                data=line.strip()
                arr=data.split(';')
                product=Product(arr[0],arr[1],float(arr[2]))
                products.append(product)
            file.close()
            return products
            pass
        except:
            traceback.print_exc()
            return []

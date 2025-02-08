class DanhMuc:
    def __init__(self,Ma=None,Ten=None):
        self.Ma=Ma
        self.Ten=Ten
        self.listproducts=[] #luudanhsachsanpham
    def __str__(self):
        return f"{self.Ma}\t{self.Ten}"
    def addproduct(self,p):
        self.listproducts.append(p)
    def print_products(self):
        for p in self.listproducts:
            print()

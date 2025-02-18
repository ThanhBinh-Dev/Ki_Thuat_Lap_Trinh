class ListProducts:
    def __init__(self):
        self.list_products = []
    def print_all_product(self):
        for sp in self.list_products:
            print(sp)
    def add_product(self,arr):
        self.list_products.extend(arr)
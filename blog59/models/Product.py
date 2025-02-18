from Chuong4_file.blog59.utils.JsonFactory import JsonFactory

@JsonFactory.register
class Product(object):
    def __init__(self,product_id=None,product_name=None,unit_price=None):
        self.product_id=product_id
        self.product_name=product_name
        self.unit_price=unit_price
    def __str__(self):
        return f"{self.product_id}\t{self.product_name}\t{self.unit_price}"

class SanPham:
    def __init__(self,ma,ten,gia,xuatxu):
        self.ma=ma
        self.ten=ten
        self.gia=gia
        self.xuatxu=xuatxu
    def __str__(self):
        info=f"{self.ma}\t{self.ten}\t{self.gia}\t{self.xuatxu}"
        return info

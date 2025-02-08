class Nhanvien:
    def __init__(self,Ho=None, Ten=None, Sosanpham=None):
        self.__Ho=Ho
        self.__Ten=Ten
        self.Sosanpham=Sosanpham
        self.nv2=None
    def get_Ho(self):
        return self.__Ho
    def set_Ho(self,Ho):
        self.__Ho=Ho
    def get_Ten(self):
        return self.__Ten
    def set_Ten(self,Ten):
        self.__Ten=Ten
    def get_Sosanpham(self):
        return self.__Sosanpham
    def set_Sosanpham(self, Sosanpham):
        if Sosanpham is None or Sosanpham < 0:
            self.__Sosanpham = 0
        else:
            self.__Sosanpham = Sosanpham
    Ho = property(get_Ho, set_Ho)
    Ten = property(get_Ten, set_Ten)
    Sosanpham = property(get_Sosanpham, set_Sosanpham)
    def __str__(self):
        return f"Họ: {self.Ho}\t Tên: {self.Ten}\t Số sản Phẩm: {self.Sosanpham}"
    def bangdongia(self):
        if self.Sosanpham<=0:
            dongia=0
        if 1<= self.Sosanpham <200:
            dongia=0.5
        elif 200<= self.Sosanpham <400:
            dongia=0.55
        elif 400 <= self.Sosanpham < 600:
            dongia=0.6
        elif self.Sosanpham>=600:
            dongia=0.65
        return dongia
    def get_luong(self):
        dongia=self.bangdongia()
        return round(dongia*self.Sosanpham,3)
    def inluong(self):
        print(f"Họ: {self.Ho} Tên: {self.Ten} Số sản phẩm: {self.Sosanpham} Lương:{self.get_luong()} VND")
    def set_nv2(self, nv2):
        self.nv2 = nv2
    def IsHigher(self,nv2):
        if self.Sosanpham is None:
            SoSP1=0
        else:
            SoSP1=self.Sosanpham
        if nv2.Sosanpham is None:
            SoSP2=0
        else:
            SoSP2=nv2.Sosanpham
        if SoSP1>SoSP2:
            return True,SoSP1-SoSP2
        else:
            return False," "
    def Result_Ishigher(self,nv2):
        if self.nv2 is None:
            print("Lỗi: Chưa đặt nhân viên để so sánh!")
            return
        k,h=self.IsHigher(nv2)
        print(f"{k} {h}")






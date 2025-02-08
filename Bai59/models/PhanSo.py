class PhanSo:
    def __init__(self,tu=None,mau=None):
        self.__tu=tu
        self.__mau=mau
    def get_tu(self):
        return self.__tu
    def set_tu(self,tu):
        self.__tu=tu
    def get_mau(self):
        return self.__mau
    def set_mau(self,mau):
        self.__mau=mau
    tu=property(get_tu,set_tu,"tu")
    mau=property(get_mau,set_mau,"mau")
    def cong(self,ps2):
        tu3=self.__tu*ps2.mau+ps2.tu*self.__mau
        mau3=self.__mau*ps2.mau
        return PhanSo(tu3,mau3)
    def tru(self,ps2):
        tu3=self.__tu*ps2.mau-ps2.tu*self.__mau
        mau3=self.__mau*ps2.mau
        return PhanSo(tu3,mau3)
    def nhan(self,ps2):
        tu3=self.__tu*ps2.tu
        mau3=self.__mau*ps2.mau
        return PhanSo(tu3,mau3)
    def chia(self,ps2):
        tu3=self.__tu*ps2.mau
        mau3=self.__mau*ps2.tu
        return PhanSo(tu3,mau3)
    def toigian(self):
        so_min=self.tu
        if so_min<self.mau:
            so_min=self.mau
        uscln=1
        for i in range(so_min,1,-1):
            if self.tu%i==0 and self.mau%i==0:
                uscln=i
                break
        return PhanSo(self.tu/uscln,self.mau/uscln)


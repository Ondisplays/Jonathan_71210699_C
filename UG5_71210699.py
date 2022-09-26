class Mobil:
    _merk = ""
    _tipe = ""
    _KapasitasBBM = None
    _JenisBahanBakar = None

    def __init__(self, merk, tipe):
        self._merk = merk
        self._tipe = tipe

    def setKapasitasBBM(self, KapasitasBBM):
        self._KapasitasBBM = KapasitasBBM

    def setJenisBahanBakar(self, JenisBahanBakar):
        self._JenisBahanBakar = JenisBahanBakar

    def getKapasitasBBM(self):
        return self._KapasitasBBM

    def getJenisBahanBakar(self):
        return self._JenisBahanBakar

    def getMerk(self):
        return self._merk

    def getTipe(self):
        return self._tipe

    def printInfo(self):
        print('============INfO============')
        print(f'Merk\t\t : {self.getMerk()}')
        print(f'Jenis\t\t : {self.getTipe()}')
        print(f'Bahan Bakar\t : {self.getJenisBahanBakar()}')
        print(f'Kapasitas BBM\t : {self.getKapasitasBBM()}')

    def isiBBM(self,harga):
        if self.getKapasitasBBM() is None or self.getJenisBahanBakar() is None:
            print('ERROR! Kapasitas BBM atau Jenis Bahan Bakar belum diinputkan')
        else:
            print(f'Mengisi {self.getKapasitasBBM()} Liter')
            print(f'Total Harga : Rp{harga*self.getKapasitasBBM()}')

if __name__ == "__main__":
    mobil1 = Mobil("Toyota", "Avanza")
    mobil1.printInfo()
    mobil2 = Mobil("Nissan", "Grand Livina")
    mobil2.setJenisBahanBakar("Bensin")
    mobil2.setKapasitasBBM(20)
    mobil2.printInfo()
    mobil1.isiBBM(14500)
    mobil2.isiBBM(14500)
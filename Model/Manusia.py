#encapsulasi
class Manusia:
    def __init__(self):
        self.nama = 'Unamed'
        self.usia = 25
        self.alamat = 'Jogja'


    def __repr__(self):
        return 'Nama {},usia {},alamat {}'.format(self.nama,self.usia,self.alamat)

    def bicara(self):
        print('Hoi! Nama saya {}'.format(self.nama))


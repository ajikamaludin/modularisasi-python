title = 'Penampilan Data Peserta Seminar'

print(title)

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



class PesertaSeminar(Manusia):
    def bicara(self):
        print('My name is {}'.format(self.nama))

#instantiatian
adam = Manusia()
adam.nama = 'Adam'
fulan = PesertaSeminar()
fulanah = PesertaSeminar()

fulan.nama = 'Susi'
fulan.usia = 28
fulan.alamat = 'Bali'

fulanah.nama = 'Joko'
fulanah.usia = 53
fulanah.alamat = 'Solo'

#polymorpisem
adam.bicara()
fulanah.bicara()
fulan.bicara()
from Model.Manusia import Manusia
from Model.PesertaSeminar import PesertaSeminar

title = 'Penampilan Data Peserta Seminar'

print(title)



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
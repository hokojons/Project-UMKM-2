class Mahasiswa():
    def __init__(self, nama=None, alamat=None):
        self.nama = nama
        self.alamat = alamat

mhs1 = Mahasiswa('Supri', 'Surabaya')
mhs2 = Mahasiswa('Jarwo', 'Sidoarjo')
mhs3 = Mahasiswa('Somat', 'Gresik')

print(f"Nama: {mhs1.nama}, Alamat: {mhs1.alamat},{mhs2.alamat},{mhs3.alamat}")
print(f"Nama: {mhs2.nama}, Alamat: {mhs2.alamat}")
print(f"Nama: {mhs3.nama}, Alamat: {mhs3.alamat}")
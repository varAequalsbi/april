class mhs:
    institusi = "Institut Teknologi dan bisnis Asia Malang"
    jumlah_mhs = 0

    def __init__(self, nama, nim, nilai):
        self._nama = nama
        self._nim = nim
        self._nilai = nilai
        mhs.jumlah_mhs += 1
    
    @property
    def nama(self):
        return self._nama
    @property
    def nim(self):
        return self._nim
    @property
    def nilai(self):
        return self._nilai
    
    @nama.setter
    def nama (self, value):
        self._nama = value

    @nim.setter
    def nim (self, value):
        self._nim = value

    @nilai.setter
    def nilai (self, value):
        if 0<= value <= 100:
            self._nilai = value
    
    @nilai.deleter
    def nilai(self):
        print(f"Menghapus nilai untuk {self._nama}")
        self._nilai = 0

    @staticmethod
    def cek_kelulusan(skor):
        return "LULUS" if skor >= 60 else "TIDAK LULUS"
    
    @classmethod
    def Ubah_institusi(cls, nama_institusi):
        cls.institusi = nama_institusi

mhs1 = mhs("Farabi", "12345", 0)
mhs1.nilai = 85
print(f"Nama: {mhs1.nama}, Nilai: {mhs1.nilai}")
status = mhs.cek_kelulusan(mhs1.nilai)
print(f"Status kelulusan: {status}")

mhs.Ubah_institusi("Universitas Malang")


del mhs1.nilai
print(f"Nama: {mhs1.nama}, Nilai: {mhs1.nilai}")

#object 2

mhs2 = mhs("Sera", "5432132", 0)
mhs2.nilai = 55
print(f"Nama: {mhs2.nama}, Nilai: {mhs2.nilai}")
status = mhs.cek_kelulusan(mhs2.nilai)
print(f"Status kelulusan: {status}")
print("Institusi Mahasiswa:", mhs2.nama, "adalah di ", mhs.institusi)
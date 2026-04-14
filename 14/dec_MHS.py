class mhs:
    def __init__(self, nama, nim):
        self._nama = nama
        self._nim = nim
    
    @property
    def nama(self):
        return self._nama
    
    @nama.setter
    def nama (self, value):
        if not value:
            raise ValueError("nama tidak boleh kosong")
        self._nama = value

    @property
    def nim(self):
        return self._nim
    
    @nim.setter
    def nim (self, value):
        if not value:
            raise ValueError("nim tidak boleh kosong")
        self._nim = value

mhs_asia = mhs("Asia", "12345")
print(f"Nama: {mhs_asia.nama}, NIM: {mhs_asia.nim}")

mhs_asia.nama = "Asia Rahma"
print(f"Nama: {mhs_asia.nama}, NIM: {mhs_asia.nim}")
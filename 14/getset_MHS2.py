class Mhs:
        __jumlah = 0;
        def __init__(self, nama, umur):
                self.__nama = nama
                self.__umur = umur
                Mhs.__jumlah += 1

        def get_nama(self):
            return self.__nama
        
        def set_nama(self, new_nama):
            self.__nama = new_nama

        def set_umur(self, new_umur):
            self.__umur = new_umur
        
        def get_umur(self):
            return self.__umur
        
        def get_jumlah1(self):
            return Mhs.__jumlah
        
        def get_jumlah2():
            return Mhs.__jumlah
        
        @staticmethod
        def get_jumlah3():
            return Mhs.__jumlah
        

mhs_asia =  Mhs("Varabi", 18)

print(mhs_asia.get_nama())
print(mhs_asia.get_umur())

mhs_asia.set_nama("Farabi")
mhs_asia.set_umur(19)

print("============")

print(mhs_asia.get_nama())
print(mhs_asia.get_umur())

print(f"Jumlah mahasiswa: {mhs_asia.get_jumlah3()}")
print(f"Jumlah mahasiswa: {Mhs.get_jumlah3()}")

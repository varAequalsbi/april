class Mhs:
        def __init__(self, nama, umur):
                self.__nama = nama
                self.__umur = umur

        def get_nama(self):
            return self.__nama
        
        def set_nama(self, new_nama):
            self.__nama = new_nama

        def set_umur(self, new_umur):
            self.__umur = new_umur
        
        def get_umur(self):
            return self.__umur
        
        
mhs_asia =  Mhs("Varabi", 18)

print(mhs_asia.get_nama())
print(mhs_asia.get_umur())

mhs_asia.set_nama("Farabi")
mhs_asia.set_umur(19)

print("============")

print(mhs_asia.get_nama())
print(mhs_asia.get_umur())


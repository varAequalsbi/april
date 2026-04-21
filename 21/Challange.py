class mhs:
    institusi = "Institut Teknologi dan bisnis Asia Malang"
    jumlah_mhs = 0
    def __init__(self, nama, nim, nilai):
        if not (0 <= nilai <= 100):
            raise ValueError("Nilai must be between 0 and 100")
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
    def nama(self, value):
        self._nama = value
    @nim.setter
    def nim(self, value):
        self._nim = value
    @nilai.setter
    def nilai(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Nilai must be between 0 and 100")
        self._nilai = value

    @staticmethod
    def cek_grade(skor):
        if skor >= 80:
            return "A"
        elif skor >= 65:
            return "B"
        elif skor >= 55:
            return "C"
        elif skor >= 50:
            return "D"
        else:
            return "E"

mylist = []
jumlah_mhs = int(input("Masukan jumlah Mahasiswa yang ingin diinput: "))

for i in range(jumlah_mhs):
    print(" ")
    print(f"Masukan data mahasiswa ke-{i + 1}")
    nama = input("Masukan nama: ")
    nim = input("Masukan nim: ")

    while True:
        try:
            nilai = int(input("Masukan nilai (0-100): "))
            mhs1 = mhs(nama, nim, nilai)
            break
        except ValueError:
            print("⚠️  Nilai harus antara 0 dan 100. Silakan coba lagi.")

    mylist.append(mhs1)

print(f"\nData seluruh Mahasiswa {mhs.institusi}")
print("=============================================")
headers = ["NIM", "Nama", "Nilai", "Grade"]
rows = [(m.nim, m.nama, m.nilai, mhs.cek_grade(m.nilai)) for m in mylist]
widths = [12, 20, 5, 5]
header_line = " ".join(f"{h:<{w}}" for h, w in zip(headers, widths))
print(header_line)
print("-" * len(header_line))
for row in rows:
    print(" ".join(f"{str(r):<{w}}" for r, w in zip(row, widths)))
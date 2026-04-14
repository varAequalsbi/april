class Hero2:
    jumlah_hero = 0

    def __init__(self, name, health, power, armor):
        self.name=name
        self.health: int=health
        self.power=power
        self.armor=armor
        Hero2.jumlah_hero +=1

suparman = Hero2("suparman", 100, 10, 6)
print('========== Memanggil var jumlah =========')
print('punya object : ', suparman.jumlah_hero)
print('punya class : ', Hero2.jumlah_hero)
print('== nilai jumlah hero di object rubah ==')
suparman.jumlah_hero = 10
print('punya object : ', suparman.jumlah_hero)
print('punya class : ', Hero2.jumlah_hero)
print('== nilai jumlah hero di object rubah ==')
Hero2.jumlah_hero = 20
print('punya object : ', suparman.jumlah_hero)
print('punya class : ', Hero2.jumlah_hero)



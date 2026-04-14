class Hero2:
    jumlah_hero = 0

    def __init__(self, name, health, power, armor):
        self.name=name
        self.health: int=health
        self.power=power
        self.armor=armor
        Hero2.jumlah_hero +=1
        self.__age = 70 #this variable is private
        self._weight = 110 # this variable is protected

suparman = Hero2("suparman", 100, 10, 6)
#print("umur suparman = ", suparman.__age)
print(suparman.__dict__)
suparman.__age=17
print(suparman.__dict__)
suparman._weight=100


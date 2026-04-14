class Hero:
    def __init__(self, name, health, power, armor):
        self.name=name
        self.health: int=health
        self.power=power
        self.armor=armor

    def siapa (self):
        print("nama hero = "+self.name)
    def healthup (self,up):
        self.health += up
    def gethealth(self):
        return self.health

suparman=Hero('superman', 1000, 100, 10)
adiwijaya=Hero('superman', 1000, 100, 10)            


suparman.siapa()
suparman.healthup(10)
print("health ammount : ", suparman.gethealth())
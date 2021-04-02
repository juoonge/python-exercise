from weapon import Weapon


class Knife(Weapon):
    def __init__(self, name, power, durability):
        super().__init__(name, power)
        self.durability = durability

    def attack(self):
        if self.durability <= 0:
            print("공격 불가!")
        else:
            super().attack()
            self.durability -= 1
            print("내구성 : ", self.durability)

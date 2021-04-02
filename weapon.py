class Weapon:
    def __init__(self, name, power):
        self.weapon_name = name
        self.power = power

    def attack(self):
        print('%s(으)로 %d의 데미지를 주었습니다' % (self.weapon_name, self.power))

    def __str__(self):
        print('%s(으)로 %d의 데미지를 주었습니다' % (self.weapon_name, self.power))

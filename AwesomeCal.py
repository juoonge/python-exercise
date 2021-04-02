class AwesomeCal:
    def __init__(self, value):
        self.value = value

    def add(self, num):
        self.value += num

    def sub(self, num):
        self.value -= num

    def changeVal(self, num):
        self.value = num

    def mul(self, num):
        self.value *= num

    def div(self, num):
        self.value = -9999


a = AwesomeCal(100)
a.add(5)
print(a.value)
a.sub(10)
print(a.value)
a.changeVal(30)
a.mul(5)
print(a.value)
a.div(0)
print(a.value)

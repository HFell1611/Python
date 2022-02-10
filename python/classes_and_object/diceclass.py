from random import randint as rand



class Dice():
    def __init__(self, sides):
        self.sides = sides
    def roll(self):
        return rand(1, self.sides)

    def __add__(self, dice2):
        return self.roll(), dice2.roll()



d6 = Dice(6)
d20 = Dice(20)




print(d6 + d20)
import random


class Dice(object):

    def __init__(self, *args):
        self.faces = [None]
        self.faces.extend(args)
        self.top = self.faces[1]
        self.up = self.faces[5]
        self.down = self.faces[2]
        self.left = self.faces[4]
        self.right = self.faces[3]
        self.back = self.faces[6]

    def roll(self, direction):
        if direction == "N":
            self.top, self.up, self.down, self.back = self.down, self.top, self.back, self.up
        elif direction == "S":
            self.top, self.up, self.down, self.back = self.up, self.back, self.top, self.down
        elif direction == "W":
            self.top, self.left, self.right, self.back = self.right, self.top, self.back, self.left
        elif direction == "E":
            self.top, self.left, self.right, self.back = self.left, self.back, self.top, self.right
        else:
            raise ValueError("{} is not valid direction.".format(direction))

    def __eq__(self, other):
        return (
           self.top, self.up, self.left, self.down, self.right, self.back
        ) == (
            other.top, other.up, other.left, other.down, other.right, other.back
        )


f1 = [int(i) for i in input().split()]
f2 = [int(i) for i in input().split()]
dice1 = Dice(*f1)
dice2 = Dice(*f2)
ans = "No"
i = 0
while i < 10000:
    if dice1 == dice2:
        ans = "Yes"
        break
    dice2.roll(random.choice(["N", "S", "W", "E"]))
    i += 1
print(ans)


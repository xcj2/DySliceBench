class Dice(object):

    def __init__(self, *args):
        self.faces = [None]
        self.faces.extend(args)
        self.top = self.faces[1]
        self.up = self.faces[5]
        self.down = self.faces[2]
        self.left = self.faces[4]
        self.right = self.faces[3]

    def roll(self, direction):
        if direction == "N":
            self.top, self.up, self.down = self.down, self.top, self.faces[7 - self.faces.index(self.top)]
        elif direction == "S":
            self.top, self.up, self.down = self.up, self.faces[7 - self.faces.index(self.top)], self.top
        elif direction == "W":
            self.top, self.left, self.right = self.right, self.top, self.faces[7 - self.faces.index(self.top)]
        elif direction == "E":
            self.top, self.left, self.right = self.left, self.faces[7 - self.faces.index(self.top)], self.top
        else:
            raise ValueError("{} is not valid direction.".format(direction))

    def get_top(self):
        return self.top


f = [int(i) for i in input().split()]
dice = Dice(*f)
for d in input():
    dice.roll(d)

print(dice.get_top())


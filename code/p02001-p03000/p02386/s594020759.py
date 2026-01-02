class Dice:
    def __init__(self):
        self.side = {"top": 0, "front": 0, "right": 0, "left": 0, "back": 0, "bottom": 0}

    # サイコロを東西南北、どちらか一方に転がした時、それぞれの面の変化
    def roll(self, direction):
        self.direction = direction
        if self.direction == "N":
            w = self.side["top"]
            self.side["top"] = self.side["front"]
            self.side["front"] = self.side["bottom"]
            self.side["bottom"] = self.side["back"]
            self.side["back"] = w
        elif self.direction == "S":
            w = self.side["top"]
            self.side["top"] = self.side["back"]
            self.side["back"] = self.side["bottom"]
            self.side["bottom"] = self.side["front"]
            self.side["front"] = w
        elif self.direction == "E":
            w = self.side["top"]
            self.side["top"] = self.side["left"]
            self.side["left"] = self.side["bottom"]
            self.side["bottom"] = self.side["right"]
            self.side["right"] = w
        elif self.direction == "W":
            w = self.side["top"]
            self.side["top"] = self.side["right"]
            self.side["right"] = self.side["bottom"]
            self.side["bottom"] = self.side["left"]
            self.side["left"] = w

    # サイコロの目を作成
    def create(self):
        for s, n in zip(dice.side, input().split()):
            dice.side[s] = int(n)

def simulation():
    for line in a:
        dir = random.sample("NSEW"*5, 20)
        for direction in dir:
            dice.roll(direction)
            if dice.side == line:
                return "No"
    else:
        a.append(dict(dice.side))

import random
n = int(input())
dice = Dice()
dice.create()
a = []; a.append(dict(dice.side))
    
for i in range(1, n):
    dice.create()
    judge = simulation()
    if judge == "No":
        print("No")
        break
else:
    print("Yes")


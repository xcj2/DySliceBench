import sys

class Dice(object):
    def __init__(self, dice):
        self.__dice = tuple(dice)

    def roll_north(self):
        self.__dice = (self.__dice[1], self.__dice[5], self.__dice[2],
                       self.__dice[3], self.__dice[0], self.__dice[4])

    def roll_south(self):
        self.__dice = (self.__dice[4], self.__dice[0], self.__dice[2],
                       self.__dice[3], self.__dice[5], self.__dice[1])

    def roll_west(self):
        self.__dice = (self.__dice[2], self.__dice[1], self.__dice[5],
                       self.__dice[0], self.__dice[4], self.__dice[3])

    def roll_east(self):
        self.__dice = (self.__dice[3], self.__dice[1], self.__dice[0],
                       self.__dice[5], self.__dice[4], self.__dice[2])

    def number(self, face_id):
        return self.__dice[face_id - 1]

    def equals(self, dice):
        for i in range(4):
            for j in range(4):
                if self.__dice == dice.__dice:
                    return True
                dice.roll_north()
            dice.roll_west()
        return False

n = int(sys.stdin.readline())
dices = []
for i in range(n):
    dices.append(Dice([int(a) for a in sys.stdin.readline().split()]))

for i in range(n):
    for j in range(i + 1, n):
        if dices[i].equals(dices[j]):
            print("No")
            exit(0)
print("Yes")
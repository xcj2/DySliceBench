from collections import deque

def is_equal(dice1, dice2):

    equal = "No"

    if dice1.min != dice2.min or dice1.max != dice2.max:
        return "No"

    top0 = dice1.disp_top_face()
    front0 = dice1.disp_front_face()

    flag = 1

    for _ in range(100):

        if dice2.disp_top_face() == top0:
            flag = 0
            break

        for _ in range(4):
            dice2.lotate("S")

            if dice2.disp_top_face() == top0:
                flag = 0
                break

        if flag :
            dice2.lotate("E")
        else:
            break

    for _ in range(4):

        if dice2.disp_front_face() == front0:
            break

        dice2.lotate("E")
        dice2.lotate("S")
        dice2.lotate("W")

    if dice1.disp_top_face() == dice2.disp_top_face() and \
       dice1.disp_bottom_face() == dice2.disp_bottom_face() and \
       dice1.disp_front_face() == dice2.disp_front_face() and \
       dice1.disp_left_face() == dice2.disp_left_face() and \
       dice1.disp_right_face() == dice2.disp_right_face() and \
       dice1.disp_back_face() == dice2.disp_back_face():

       equal = "Yes"

    return equal

class Dice():
    def __init__(self, seq):
        self.v = deque([seq[5], seq[4], seq[0], seq[1]])
        self.h = deque([seq[3], seq[0], seq[2], seq[5]])

        self.max = max(seq)
        self.min = min(seq)

    def lotate(self, direction):

        if   direction == "E":
            self.h.rotate()
            self.v[2] = self.h[1]
            self.v[0] = self.h[3]

        elif direction == "W":
            self.h.rotate(-1)
            self.v[2] = self.h[1]
            self.v[0] = self.h[3]

        elif direction == "N":
            self.v.rotate(-1)
            self.h[1] = self.v[2]
            self.h[3] = self.v[0]

        elif direction == "S":
            self.v.rotate()
            self.h[1] = self.v[2]
            self.h[3] = self.v[0]

        else:
            pass

    def disp_top_face(self):
        return self.v[2]

    def disp_front_face(self):
        return self.v[3]

    def disp_back_face(self):
        return self.v[1]

    def disp_right_face(self):
        return self.h[2]

    def disp_left_face(self):
        return self.h[0]

    def disp_bottom_face(self):
        return self.h[3]

if __name__ == "__main__":

    param = input()
    n = int(param)

    dices = list()

    for _ in range(n):
        param = input().split(" ")
        seq = [int(a) for a in param]
        d = Dice(seq)
        dices.append(d)

    different = "Yes"

    for i in range(len(dices)-1):

        if len(dices) - 1 < 2:
            if is_equal(dices[i], dices[i+1]) == "Yes":
                different = "No"
        else:
            for j in range( i + 1, len(dices) - 1 ):
                if is_equal(dices[i], dices[j]) == "Yes":
                    different = "No"

    print(different)


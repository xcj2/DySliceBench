def create_dice(nums):
    a, b, c, d, e, f = nums
    vertical = [a, b, f, e]
    horizontal = [b, c, e, d]
    return Dice(vertical, horizontal)


class Dice:
    def __init__(self, v, h):
        self.vertical = v
        self.horizontal = h

    def v2h(self):
        self.horizontal[0] = self.vertical[1]
        self.horizontal[2] = self.vertical[3]

    def h2v(self):
        self.vertical[1] = self.horizontal[0]
        self.vertical[3] = self.horizontal[2]

    def roll(self, direction):
        if direction == 'N':
            tmp1 = self.vertical[0]
            tmp2 = self.vertical[1:]
            self.vertical = tmp2 + [tmp1]
            self.v2h()
        elif direction == 'S':
            tmp1 = self.vertical[-1]
            tmp2 = self.vertical[:-1]
            self.vertical = [tmp1] + tmp2
            self.v2h()
        elif direction == 'E':
            tmp1 = self.horizontal[0]
            tmp2 = self.horizontal[1:]
            self.horizontal = tmp2 + [tmp1]
            self.h2v()
        elif direction == 'W':
            tmp1 = self.horizontal[-1]
            tmp2 = self.horizontal[:-1]
            self.horizontal = [tmp1] + tmp2
            self.h2v()


s1 = map(int, input().split(" "))
d1 = create_dice(s1)

s2 = map(int, input().split(" "))
d2 = create_dice(s2)


def match(l1, l2):
    lenlist = len(l1)
    lenset = len(set(l1))
    if lenlist == lenset:
        return l1[0] == l2[0]
    else:
        diff = 4 - (lenlist - lenset) + 1
        for i in range(diff):
            if l1[i] != l2[i]:
                return False
        return True

r = 0
while d1.vertical != d2.vertical and d1.horizontal != d2.horizontal and r < 4:
    # 強制的に一つ回す
    d2.roll("E")

    v = 0
    while not match(d1.vertical, d2.vertical) and v < 4:
        d2.roll("N")
        v += 1

    h = 0
    while not match(d1.horizontal, d2.horizontal) and v < 4:
        d2.roll("E")
        h += 1

    r += 1

if d1.vertical == d2.vertical and d1.horizontal == d2.horizontal:
    print("Yes")
else:
    print("No")


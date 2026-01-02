def create_dice(nums):
    a, b, c, d, e, f = nums
    ver = [a, b, f, e]
    hor = [b, c, e, d]
    return Dice(ver, hor, nums)


class Dice:
    def __init__(self, v, h, r):
        self.ver = v
        self.hor = h
        self.raw = r

    def __str__(self):
        l = [self.ver[0], self.ver[1], self.hor[1],
             self.hor[3], self.ver[3], self.ver[2]]
        s = map(str, l)
        return "".join(s)

    def v2h(self):
        self.hor[0] = self.ver[1]
        self.hor[2] = self.ver[3]

    def h2v(self):
        self.ver[1] = self.hor[0]
        self.ver[3] = self.hor[2]

    def roll(self, direction):
        if direction == 'N':
            tmp1 = self.ver[0]
            tmp2 = self.ver[1:]
            self.ver = tmp2 + [tmp1]
            self.v2h()
        elif direction == 'S':
            tmp1 = self.ver[-1]
            tmp2 = self.ver[:-1]
            self.ver = [tmp1] + tmp2
            self.v2h()
        elif direction == 'E':
            tmp1 = self.hor[0]
            tmp2 = self.hor[1:]
            self.hor = tmp2 + [tmp1]
            self.h2v()
        elif direction == 'W':
            tmp1 = self.hor[-1]
            tmp2 = self.hor[:-1]
            self.hor = [tmp1] + tmp2
            self.h2v()


def match_dice(d1, d2):
    if str(d1) == str(d2):
        return True
    return False


def test(d1, d2):
    s1 = set(d1.raw)
    s2 = set(d2.raw)
    if s1 != s2:
        return False

    for v in range(2):
        if match_dice(d1, d2):
            return True

        for h in range(3):
            if match_dice(d1, d2):
                return True
            d2.roll("E")

        d2.roll("N")

    for v in range(2):
        if match_dice(d1, d2):
            return True

        for h in range(3):
            if match_dice(d1, d2):
                return True
            d2.roll("E")

        d2.roll("S")

    for v in range(2):
        if match_dice(d1, d2):
            return True

        for h in range(3):
            if match_dice(d1, d2):
                return True
            d2.roll("E")

        d2.roll("N")

    return False


def check(dices):
    for i in range(len(dices) - 1):
        for j in range(i + 1, len(dices)):
            t = test(dices[i], dices[j])
            if t:
                return True

    return False

data_count = int(input())
dices = []
for _ in range(data_count):
    s = list(map(int, input().split(" ")))
    d = create_dice(s)
    dices.append(d)

result = check(dices)
if not result:
    print("Yes")
else:
    print("No")


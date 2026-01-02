id1 = list(map(int, input().split()))
id2 = list(map(int, input().split()))


class die:
    face = [0, 0, 0, 0, 0, 0]

    def __init__(self, nums):
        self.face = [nums[f] for f in [0, 3, 1, 2, 4, 5]]

    def roll(self, dirs):

        for di in dirs:
            c_face = list(self.face)
            if di == 'S':
                self.face = [c_face[f] for f in [4, 1, 0, 3, 5, 2]]
            elif di == 'N':
                self.face = [c_face[f] for f in [2, 1, 5, 3, 0, 4]]
            elif di == 'W':
                self.face = [c_face[f] for f in [3, 0, 2, 5, 4, 1]]
            elif di == 'E':
                self.face = [c_face[f] for f in [1, 5, 2, 0, 4, 3]]
            # print(di, self.face)

        return list(self.face)


def four_roll(d, d2):
    for r in 'SSSS':
        d.roll(r)
        if d.face == d2.face:
            print('Yes')
            return True


d2 = die(id2)
for md in (' ', 'W', 'E', 'NW', 'NE', 'WW'):
    d1 = die(id1)
    d1.roll(md)
    if four_roll(d1, d2):
        break
else:
    print('No')

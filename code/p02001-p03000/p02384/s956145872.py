nums = list(map(int, input().split()))
cases = int(input())


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


def four_roll(d, t, f):
    for r in 'SSSS':
        d.roll(r)
        if d.face[0] == t and d.face[2] == f:
            print(d.face[3])
            return True


for _ in range(cases):
    t, f = map(int, input().split())
    for md in (' ', 'W', 'E', 'NW', 'NE', 'WW'):
        d = die(nums)
        d.roll(md)
        four_roll(d, t, f)

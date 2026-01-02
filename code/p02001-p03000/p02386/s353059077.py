nums = int(input())
dice = []
for _ in range(nums):
    dice.append(list(map(int, input().split())))


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


def search():
    for i, d1 in enumerate(dice):
        dice_set_01 = set()
        for md in (' ', 'W', 'E', 'NW', 'NE', 'WW'):
            d_1 = die(d1)
            d_1.roll(md)
            for r in 'SSSS':
                dice_set_01.add(tuple(d_1.roll(r)))

        for j, d2 in enumerate(dice[i+1:], start=i+1):
            dice_set_02 = set()
            for md in (' ', 'W', 'E', 'NW', 'NE', 'WW'):
                d_2 = die(d2)
                d_2.roll(md)
                for r in 'SSSS':
                    dice_set_02.add(tuple(d_2.roll(r)))
            if dice_set_01 - dice_set_02 == set():
                return False
    return True


print(['No', 'Yes'][search()])

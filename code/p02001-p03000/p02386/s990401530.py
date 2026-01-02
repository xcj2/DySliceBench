class Dice:
    D = {'E': (3, 1, 0, 5, 4, 2),
         'W': (2, 1, 5, 0, 4, 3),
         'S': (4, 0, 2, 3, 5, 1),
         'N': (1, 5, 2, 3, 0, 4)}
    def __init__(self, a, b, c, d, e, f):
        self.nbrs = [a, b, c, d, e, f]
    def rll(self, dr):
        self.nbrs = [self.nbrs[i] for i in self.D[dr]]
    def issame(self, othrdice):
        for i in 'NNNN':
            self.rll(i)
            for j in 'EEEE':
                self.rll(j)
                for k in 'NNNN':
                    self.rll(k)
                    if self.nbrs == othrdice.nbrs:
                        return True
        return False


n = int(input())
dices = []
for _ in range(n):
    a, b, c, d, e, f = input().split()
    dice = Dice(a, b, c, d, e, f)
    dices.append(dice)
for x in range(n - 1):
    for y in range(x + 1, n):
        if dices[y].issame(dices[x]):
            print('No')
            exit()
print('Yes')

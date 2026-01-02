import sys
sys.setrecursionlimit(700000)
from itertools import product

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

h, w, k = l_in()
S = list(map(lambda _: s_in(), range(h)))

sums = [[0 for _ in range(w)] for _ in range(h)]

sums[0][0] = int(S[0][0])

for i in range(1, h):
    sums[i][0] = sums[i-1][0] + int(S[i][0])

for j in range(1, w):
    sums[0][j] = sums[0][j-1] + int(S[0][j])

for i in range(1, h):
    for j in range(1, w):
        sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + int(S[i][j])

def sq(x1, x2, y1, y2):
    if x1 > 0 and y1 > 0:
        return -sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1] + sums[x2][y2]
    if x1 > 0 and y1 == 0:
        return -sums[x1-1][y2] + sums[x2][y2]
    if x1 == 0 and y1 > 0:
        return -sums[x2][y1-1] + sums[x2][y2]
    if x1 == 0 and y1 == 0:
        return sums[x2][y2]

def exec(i, list):
    current = i
    while current < h:
        exec(current, )

        current += 1

res = h*w

# print(S)
# print(sums)

for ss in product('01', repeat=h-1):
    lis = []
    start = 0
    current = 0
    for s in ss:
        if s == '1':
            lis.append((start, current))
            start = current + 1
        current += 1
    lis.append((start, h-1))

    # print(lis)
    j1 = 0
    cut = 0
    for j2 in range(w-1):
        for i1, i2 in lis:
            if sq(i1, i2, j1, j2) <= k and sq(i1, i2, j1, j2+1) > k:
                # print("cut", j1, j2)
                cut += 1
                j1 = j2+1


    # for i1, i2 in lis:
    #     print(i1,i2,j1,w-1, sq(i1, i2, j1, w-1) <= k)
    # print(j1, all(sq(i1, i2, j1, w-1) <= k for i1, i2 in lis))
    if all(sq(i1, i2, j1, w-1) <= k for i1, i2 in lis):
        cut += 1
        res = min(res, cut-1+len(lis)-1)

print(res)

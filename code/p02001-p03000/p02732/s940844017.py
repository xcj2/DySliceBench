import sys
from functools import reduce
sys.setrecursionlimit(700000)

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


N = n_in()
A = l_in()

C = [0 for _ in range(N)]

for a in A:
    C[a-1] += 1

res = reduce(lambda memo, c: memo+c*(c-1)//2, C, 0)

for a in A:
    c = C[a-1]
    print(res - c*(c-1)//2 + (c-1)*(c-2)//2)


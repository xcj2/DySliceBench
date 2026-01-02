import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def printlist(lst, k='\n'): print(k.join(list(map(str, lst))))
INF = float('inf')

from math import log2

class Doubling:
    def __init__(self, lst, max_step):
        self.lst = lst
        self.max_step = max_step
        self.k = int(log2(max_step * 2 - 1)) + 1
        # print(self.k)
        self.D = self.create()

    def create(self):
        len_ = len(self.lst)
        D = [[-1] * len_ for _ in range(self.k)]
        D[0] = self.lst
        d = 2
        for i in range(1, self.k):
            for j in range(len_):
                D[i][j] = D[i - 1][D[i - 1][j]]
            d *= 2
        # print(D)
        return D

    def step(self, start, step):
        v = start
        for i in range(self.k, -1, -1):
            l = 1 << i
            if l <= step:
                v = self.D[i][v]
                # print(i, l)
                step -= l
        return v

def solve():
    n, k = MI()

    A = LI1()
    d = Doubling(A, k)

    v = d.step(0, k)
    print(v+1)







if __name__ == '__main__':

    solve()

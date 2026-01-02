import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

class BitMax:
    def __init__(self, n):
        self.n = n + 3
        self.table = [0] * (self.n + 1)

    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.table[i] = max(self.table[i], x)
            i += i & -i

    def max(self, i):
        i += 1
        res = 0
        while i > 0:
            res = max(res, self.table[i])
            i -= i & -i
        return res

def main():
    n=int(input())
    hh=LI()
    aa=LI()
    dp=BitMax(n+1)
    for h,a in zip(hh,aa):
        dp.update(h,dp.max(h-1)+a)
    print(dp.max(n))

main()
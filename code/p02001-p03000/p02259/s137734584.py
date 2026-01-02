import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

class BitSum:
    def __init__(self, n):
        self.n = n + 3
        self.table = [0] * (self.n + 1)

    def update(self, i, x):
        i += 1
        while i <= self.n:
            self.table[i] += x
            i += i & -i

    def sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.table[i]
            i -= i & -i
        return res

def main():
    n = int(input())
    aa = list(map(int, input().split()))
    bit=BitSum(105)
    swap_n=0
    for i,a in enumerate(aa):
        swap_n+=i-bit.sum(a)
        bit.update(a,1)
    aa.sort()
    print(*aa)
    print(swap_n)

main()


import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class BitSum:
    def __init__(self, n):
        self.n = n + 3
        self.table = [0] * (self.n + 1)

    def add(self, i, x):
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
    n = II()
    bits = [BitSum(n) for _ in range(26)]
    s = list(SI())
    a = ord("a")
    for i, c in enumerate(s):
        code = ord(c) - a
        bits[code].add(i, 1)
    q = II()
    for _ in range(q):
        op, x, y = input().split()
        if op == "1":
            i = int(x) - 1
            now = s[i]
            s[i] = y
            bits[ord(now) - a].add(i, -1)
            bits[ord(y) - a].add(i, 1)
        else:
            l, r = int(x) - 2, int(y) - 1
            print(sum(bits[i].sum(r) - bits[i].sum(l) > 0 for i in range(26)))

main()

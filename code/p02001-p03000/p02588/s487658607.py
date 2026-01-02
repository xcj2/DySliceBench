import sys
from itertools import chain

readline = sys.stdin.readline
class Bit:
    def __init__(self, lst):
        t = 1
        while (t << 1) <= len(lst):
            for i in range(t, len(lst) - t + 1, t << 1):
                lst[i + t - 1] += lst[i - 1]
            t <<= 1
        self.lst = lst

    def add(self, pos, value):
        pos += 1
        while pos <= len(self.lst):
            self.lst[pos - 1] += value
            pos += pos & (-pos)

    def update(self, pos, value):
        diff = value - self.at(pos)
        self.add(pos, diff)

    def at(self, pos):
        return self.sum(pos + 1) - self.sum(pos)
    
    def sum(self, pos):
        # sum of [0, pos)
        if pos == 0:
            return 0
        s = 0
        while pos > 0:
            s += self.lst[pos - 1]
            #pos -= pos & (-pos)
            pos &= ~(-pos)
        return s
    
def solve():
    N = int(readline())
    A = [float(readline()) for i in range(N)]

    C = [0] * N
    c5s = set()

    for i, a in enumerate(A):
        #b = int(a * (10 ** 9))
        #b = a * (10 ** 9)
        b = round(a * (10 ** 9))
        c2, c5 = -9, -9
        while b % 2 == 0:
            b //= 2
            c2 += 1
        while b % 5 == 0:
            b //= 5
            c5 += 1
        
        C[i] = (c2, c5)
    
    Q = [(-a, -b) for a,b in C]

    count0 = sum(a >= 0 and b >= 0 for a,b in C)

    # Coordinate compression
    xs = sorted(set(chain((a for a,b in C), (a for a,b in Q))))
    ys = sorted(set(chain((b for a,b in C), (b for a,b in Q))))
    compA = {v: i for i, v in enumerate(xs)}
    compB = {v: i for i, v in enumerate(ys)}
    C = [(compA[a], compB[b]) for a,b in C]
    Q = [(compA[a], compB[b]) for a,b in Q]
    H, W = len(xs), len(ys)

    C.sort()
    Q.sort(reverse=True)

    bit = Bit([0] * W)
    ans = 0

    j = N - 1
    for x, y in Q:
        while j >= 0 and C[j][0] >= x:
            bit.add(C[j][1], 1)
            j -= 1
        ans += bit.sum(W) - bit.sum(y)

    print((ans - count0) // 2)


solve()
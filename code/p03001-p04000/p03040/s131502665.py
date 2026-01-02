from heapq import heappop, heappush
import sys

input = sys.stdin.readline


class median_o1:
    def __init__(self):
        self.count = 0
        self.al = []
        self.ar = []
        self.sl = 0
        self.sr = 0
        self.b = 0

    def update_b(self, b):
        self.b += b

    def insert(self, x):
        if self.count % 2 == 0:
            if self.count == 0:
                heappush(self.al, -x)
                self.sl += x
            else:
                t = heappop(self.ar)
                self.sr -= t
                tl, tr = min(x, t), max(x, t)
                heappush(self.al, -tl)
                self.sl += tl
                heappush(self.ar, tr)
                self.sr += tr
        else:
            t = heappop(self.al)
            t *= (-1)
            self.sl -= t
            tl, tr = min(x, t), max(x, t)
            heappush(self.ar, tr)
            self.sr += tr
            heappush(self.al, -tl)
            self.sl += tl
        self.count += 1

    def get_median(self):
        return -self.al[0]

    def calc_min_value(self):
        # print(self.al, self.ar, self.b, self.sl, self.sr)
        m = self.get_median()
        return (m * ((self.count + 1) // 2) - self.sl) + (self.sr - m * (self.count // 2)) + self.b


q = int(input())

m = median_o1()

for _ in range(q):
    q_typ, *x = map(int, input().split())
    # 1, [a, b]
    # 2, []
    if q_typ == 1:
        m.update_b(x[1])
        m.insert(x[0])
    else:
        print(m.get_median(), m.calc_min_value())

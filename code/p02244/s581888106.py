from itertools import product
from copy import deepcopy, copy
class QueenMAP():
    def __init__(self):
        self.yoko = set()
        self.tate = set()
        self.naname1 = set()
        self.naname2 = set()
        self.MAP = [["."] * 8 for _ in range(8)]
    def add(self, y, x):
        self.MAP[y][x] = "Q"
        self.yoko.add(y)
        self.tate.add(x)
        self.naname1.add(y - x)
        self.naname2.add(x + y)
    def check(self, y, x):
        if y in self.yoko or x in self.tate or (y - x) in self.naname1 or (x + y) in self.naname2:
            return False
        return True
    def allcheck(self):
        for i in range(8):
            if not "Q" in self.MAP[i]:
                return False
        return True
def nuri(m, a, b):
    for i in range(8):
        m[a][i] = "1"
        m[i][b] = "1"
    if a + b < 8:
        y = a + b
        x = 0
        l = a + b + 1
    else:
        y = 7
        x = a + b - 7
        l = 15 - a - b
    for i in range(l):
        m[y - i][x + i] = "1"
    if a <= b:
        ny = 0
        nx = b - a
        l = 8 - (b + a)
    else:
        ny = a - b
        nx = 0
        l = 8 - (a - b)
    for i in range(l):
        m[ny + i][nx + i] = "1"
    return m
def solve(MAP0, MAP, n):
    dp = [(deepcopy(MAP0), deepcopy(MAP), n)]
    while dp:
        m0, m, cnt = dp.pop()
        if cnt == 8:
            flg = True
            for r in range(8):
                if "".join(map(str, m0[r])).find("0"):
                    flg = False
                    break
            if flg:
                return m
        for i in range(8):
            for j in range(8):
                if m0[i][j] == "0":
                    dp.append((nuri(deepcopy(m0), i, j), deepcopy(m), cnt + 1))
    return m
def MAIN():
    f = lambda M: "\n".join("".join(map(str, m)) for m in M)
    QM = QueenMAP()
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        QM.add(a, b)
    dp = [(deepcopy(QM), n)]
    while dp:
        Q, cnt = dp.pop()
        if cnt == 8:
            if Q.allcheck():
                print(f(Q.MAP))
                break
            continue
        cnt += 1
        for i in range(8):
            for j in range(8):
                if Q.check(i, j):
                    CQ = deepcopy(Q)
                    CQ.add(i, j)
                    dp.append((CQ, cnt))
MAIN()


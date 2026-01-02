
import sys
inf = 10 ** 20; INF = float("INF"); ans = 0
"""for dx, dy in dd:
        nx = j + dx; ny = i + dy
            if 0 <= nx < w and 0 <= ny < h:"""
def wi(): return list(map(int, sys.stdin.readline().split()))
def wip(): return [int(x) - 1 for x in sys.stdin.readline().split()]#WideIntPoint
def ws(): return sys.stdin.readline().split()
def i(): return int(sys.stdin.readline())
def s(): return input()
def hi(n): return [i() for _ in range(n)]
def hs(n): return [s() for _ in range(n)]#HeightString
def mi(n): return [wi() for _ in range(n)]#MatrixInt
def mip(n): return [wip() for _ in range(n)]
def ms(n): return [ws() for _ in range(n)]

h, w = wi()
s = []
for i in range(h):#h:高さ
    s.append([str(m) for m in list(input())])

numj = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if j == 0:
            if s[i][j] != "#":
                numj[i][j] += 1
        elif s[i][j] != "#":
            numj[i][j] += numj[i][j - 1] + 1
        else:
            numj[i][j] = 0
    for j2 in range(w - 2, -1, -1):
        if s[i][j2] != "#":
            if s[i][j2 + 1] != "#":
                numj[i][j2] = numj[i][j2 + 1]

numi = [[0 for _ in range(w)] for _ in range(h)]
for j in range(w):
    for i in range(h):
        if i == 0:
            if s[i][j] != "#":
                numi[i][j] += 1
        elif s[i][j] != "#":
            numi[i][j] += numi[i - 1][j] + 1
        else:
            numi[i][j] = 0
    for i2 in range(h - 2, -1, -1):
        if s[i2][j] != "#":
            if s[i2 + 1][j] != "#":
                numi[i2][j] = numi[i2 + 1][j]

for i in range(h):
    for j in range(w):
        ans = max(ans, numj[i][j] + numi[i][j])


print(ans - 1)
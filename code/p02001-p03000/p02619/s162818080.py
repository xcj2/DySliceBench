import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

D = I()
c = [0] + LI()
s = [0] + [[0] + LI() for i in range(D)]
t = [0] + [I() for i in range(D)]

last = [0]*27
manzokudo = 0

for i in range(1,D+1):
    last[t[i]] = i
    manzokudo += s[i][t[i]]
    r = 0
    for j in range(1,27):
        r += c[j]*(i-last[j])
    manzokudo -= r
    print(manzokudo)
import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


from collections import defaultdict

N = I()
D = LI()
d1 = defaultdict(int)
for d in D:
    d1[d] += 1

M = I()
T = LI()
d2 = defaultdict(int)
for t in T:
    d2[t] += 1

for key in d2.keys():
    if d2[key] > d1[key]:
        print('NO')
        break
else:
    print('YES')

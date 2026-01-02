import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
c = LS2()

w = [0]*N
r = [0]*N
for i in range(N):
    if i == 0:
        if c[i] == 'W':
            w[i] = 1
        else:
            r[i] = 1
    else:
        if c[i] == 'W':
            w[i] = w[i-1]+1
            r[i] = r[i-1]
        else:
            w[i] = w[i-1]
            r[i] = r[i-1]+1
a = w[-1]
b = r[-1]
if b == 0:
    print(0)
    exit()
for i in range(N):
    if w[i] == b-r[i]:
        print(w[i])
        exit()

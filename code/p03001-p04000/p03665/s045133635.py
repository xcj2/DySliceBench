import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N,P = MI()
A = LI()

x,y = 0,0
for a in A:
    if a % 2 == 0:
        x += 1
    else:
        y += 1

if y == 0:
    if P == 1:
        print(0)
    else:
        print(2**x)
else:
    print(2**(x+y-1))


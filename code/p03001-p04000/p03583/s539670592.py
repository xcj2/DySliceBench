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
for h in range(1,3501):
    for n in range(h,3501):
        if 4*h*n-N*n-N*h > 0 and (N*h*n) % (4*h*n-N*n-N*h) == 0:
            print(h,n,(N*h*n)//(4*h*n-N*n-N*h))
            exit()

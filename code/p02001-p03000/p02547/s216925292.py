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
D = [tuple(MI()) for _ in range(N)]
for i in range(N-2):
    if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
        print('Yes')
        break
else:
    print('No')

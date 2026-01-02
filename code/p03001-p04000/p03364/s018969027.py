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
S = [LS2() for _ in range(N)]
ans = 0
for a in range(N):
    X = [S[i] for i in range(a,N)] + [S[i] for i in range(a)]
    for i in range(N-1):
        for j in range(i+1,N):
            if X[i][j] != X[j][i]:
                break
        else:
            continue
        break
    else:
        ans += 1

print(ans*N)

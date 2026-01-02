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
S = [''] + LS2()

R = [0]*(N+1)
G = [0]*(N+1)
B = [0]*(N+1)
for i in range(1,N+1):
    s = S[i]
    R[i] = R[i-1]
    G[i] = G[i-1]
    B[i] = B[i-1]
    if s == 'R':
        R[i] += 1
    elif s == 'G':
        G[i] += 1
    else:
        B[i] += 1

ans = 0
for i in range(2,N):
    if S[i] == 'R':
        ans += G[i-1]*(B[-1]-B[i])
        ans += B[i-1]*(G[-1]-G[i])
        for j in range(1,N+1):
            if 1 <= i-j <= N and 1 <= i+j <= N:
                if (S[i-j] == 'G' and S[i+j] == 'B') or (S[i-j] == 'B' and S[i+j] == 'G'):
                    ans -= 1

    elif S[i] == 'G':
        ans += R[i-1]*(B[-1]-B[i])
        ans += B[i-1]*(R[-1]-R[i])
        for j in range(1,N+1):
            if 1 <= i-j <= N and 1 <= i+j <= N:
                if (S[i-j] == 'R' and S[i+j] == 'B') or (S[i-j] == 'B' and S[i+j] == 'R'):
                    ans -= 1
    else:
        ans += G[i-1]*(R[-1]-R[i])
        ans += R[i-1]*(G[-1]-G[i])
        for j in range(1,N+1):
            if 1 <= i-j <= N and 1 <= i+j <= N:
                if (S[i-j] == 'R' and S[i+j] == 'G') or (S[i-j] == 'G' and S[i+j] == 'R'):
                    ans -= 1

print(ans)

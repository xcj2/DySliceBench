import sys

sys.setrecursionlimit(10**7)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())  #空白あり
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N,K = MI()
V = LI()

ans = 0
for i in range(K+1):  # 操作回数
    for j in range(N+1):  # 左から
        for k in range(N+1):  # 右から
            if j + k > min(N,i):
                break
            l = i-j-k
            if l > j+k:
                continue
            A = [V[m] for m in range(j)] + [V[N-1-m] for m in range(k)]
            A.sort(reverse=True)
            ans = max(ans,sum(A[m] for m in range(j+k-l)))
print(ans)

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = LS2()
for i in range(N):
    S[i] = ord(S[i])-97

# Rolling Hash

mod = 10**9+7
base = 1234


def f(n):  # 長さnで条件を満たす部分列が存在するか
    A = []
    a = 0
    for i in range(n):
        a += S[i]*pow(base,i,mod)
        a %= mod
    A.append(a)
    for i in range(n,N):
        a -= S[i-n]
        a *= pow(base,mod-2,mod)
        a %= mod
        a += S[i]*pow(base,n-1,mod)
        a %= mod
        A.append(a)
    for i in range(N-n+1):
        for j in range(i+n,N-n+1):
            if A[i] == A[j]:
                return True
    return False


left = 0  # 可能
right = N+1  # 不可能
while left + 1 < right:
    mid = (left + right)//2
    if f(mid):
        left = mid
    else:
        right = mid
print(left)

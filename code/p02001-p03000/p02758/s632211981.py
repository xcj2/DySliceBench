import sys
sys.setrecursionlimit(10**9)

mod = 998244353

# segment tree
def init_max(init_max_val, n):
    #set_val
    for i in range(n):
        seg_max[i+num_max-1]=init_max_val[i]
    #built
    for i in range(num_max-2,-1,-1) :
        seg_max[i]=max(seg_max[2*i+1],seg_max[2*i+2])

def update_max(k,x):
    k += num_max-1
    seg_max[k] = x
    while k:
        k = (k-1)//2
        seg_max[k] = max(seg_max[k*2+1],seg_max[k*2+2])

def query_max(p,q):
    if q<=p:
        return ide_ele_max
    p += num_max-1
    q += num_max-2
    res=ide_ele_max
    while q-p>1:
        if p&1 == 0:
            res = max(res,seg_max[p])
        if q&1 == 1:
            res = max(res,seg_max[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = max(res,seg_max[p])
    else:
        res = max(max(res,seg_max[p]),seg_max[q])
    return res

#####単位元######
ide_ele_max = -1

#num_max:n以上の最小の2のべき乗
num_max = 1 << 18
seg_max=[ide_ele_max]*2*num_max



N = int(input())
tmpX = []
for i in range(N):
    x, d = list(map(int, input().split()))
    tmpX.append((x, d))
tmpX.sort()


X, D = [0] * N, [0] * N
for i in range(N):
    X[i] = tmpX[i][0]
    D[i] = tmpX[i][1]

to = [0] * N
for i in range(N):
    to[i] = i
init_max(to, N)

for i in range(N-1, -1, -1):
    ok = i
    ng = N
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if X[i] + D[i] > X[mid]:
            ok = mid
        else :
            ng = mid
    to[i] = query_max(i, ok+1)
    update_max(i, to[i])

dp = [0] * (N+1)
dp[0] = 1
for i in range(N):
    dp[i+1] += dp[i]
    dp[i+1] %= mod
    dp[to[i]+1] += dp[i]
    dp[to[i]+1] %= mod
print(dp[N])

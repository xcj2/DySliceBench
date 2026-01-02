N, K = (int(i) for i in input().split())
N += 1
l1 = []
l2 = []
n_ma = 0
for i in range(1, N):
    j = (N-1)//(i+1) + 1
    if i > j:
        break
    elif i == j:
        l1.append(i)
        break
    l1.append(i)
    l2.append(j)
l2.reverse()
L = l1 + l2 + [N]
M = len(L) - 1
DP = [[0] * (M+1) for counter1 in range(K+1)]

def BIT_query(BIT, idx):
    res_sum = 0
    while idx > 0:
        res_sum += BIT[idx]
        idx -= idx&(-idx)
    return res_sum

def BIT_update(BIT, idx, x):
    while idx <= M:
        BIT[idx] += x
        idx += idx&(-idx)
    return

def BIT_debug(BIT):
    return [BIT_query(BIT, i) - BIT_query(BIT, i-1) for i in range(1, M+1)]

MOD = 10**9 + 7
for i in range(M):
    BIT_update(DP[1], i+1, L[i+1]-L[i])
for i in range(1, K):
    for j in range(M):
        x = BIT_query(DP[i], M-j)
        x *= L[j+1]-L[j]
        x %= MOD
        BIT_update(DP[i+1], j+1, x)

print(BIT_query(DP[K], M)%MOD)
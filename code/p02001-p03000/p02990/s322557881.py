from functools import reduce

def cin():  return list(map(int,input().split()))

def cmb(n, r):
    INF = 10 ** 9 + 7
    r = min(n - r, r)
    if r == 0:  return 1
    numer = reduce(lambda x, y: (x * y) % INF, range(n, n - r, -1))
    denom = reduce(lambda x, y: (x * y) % INF, range(1, r + 1))
    return (numer * pow(denom, INF - 2, INF)) % INF

def nHr(n, r):  
    if n == 0:  return 1
    return cmb(n + r - 1, n)

INF = 10 ** 9 + 7

N, K = cin()
ans = [N - K + 1]
for i in range(2, K + 1):
    if N - K + 1 >= i:  cnt = cmb(N - K + 1, i) * nHr(K - i, i)
    else:  cnt = 0
    ans.append(cnt % INF)

for i in range(K):  print(ans[i])
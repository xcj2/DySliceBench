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

N, K = cin()

INF = 10 ** 9 + 7

ans = [N - K + 1]
for i in range(2, K + 1):
    b = nHr(K - i, i)
    cnt = 0
    tmp = N - K - (i + 1)
    if tmp >= 0:
        cnt += b * nHr(tmp, i + 1)
        cnt %= INF
    tmp += 1
    if tmp >= 0:
        cnt += 2 * b * nHr(tmp, i)
        cnt %= INF
    tmp += 1
    if tmp >= 0:
        cnt += nHr(tmp, i - 1) * b
        cnt %= INF
    ans.append(cnt)

for i in range(K):  print(ans[i])
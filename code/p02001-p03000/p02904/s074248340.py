NN = 18
MA = [-1] * ((1<<NN+1)-1)
MI = [1<<100] * ((1<<NN+1)-1)
 
def update(a, x):
    i = (1<<NN) - 1 + a
    MI[i] = x
    MA[i] = x
    while True:
        i = (i-1) // 2
        MI[i] = min(MI[2*i+1], MI[2*i+2])
        MA[i] = max(MA[2*i+1], MA[2*i+2])
        if i == 0:
            break
def rangemin(a, b):
    l = a + (1<<NN)
    r = b + (1<<NN)
    mi = 1<<100
    while l < r:
        if l%2:
            mi = min(mi, MI[l-1])
            l += 1
        if r%2:
            r -= 1
            mi = min(mi, MI[r-1])
        l >>= 1
        r >>= 1
    return mi
def rangemax(a, b):
    l = a + (1<<NN)
    r = b + (1<<NN)
    ma = -1
    while l < r:
        if l%2:
            ma = max(ma, MA[l-1])
            l += 1
        if r%2:
            r -= 1
            ma = max(ma, MA[r-1])
        l >>= 1
        r >>= 1
    return ma

N, K = map(int, input().split())
A = [int(a) for a in input().split()]
a = 0
l = -1
cnt = 0
for i in range(1, N):
    if A[i-1] > A[i]:
        a = i
    if i >= K-1 and a <= i - K + 1:
        if i - l > 1:
            cnt += 1
        l = i
ans = 1 - max(cnt-1, 0)
for i in range(N):
    update(i, A[i])
    if i >= K:
        mi = rangemin(i-K, i)
        ma = rangemax(i-K+1, i+1)
        if mi != A[i-K] or ma != A[i]:
            ans += 1

print(ans)
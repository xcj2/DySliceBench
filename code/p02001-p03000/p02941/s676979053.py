import heapq as hq
mod = 10**9+7
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())

def onon():
    n = onem()

    a = l()

    b = l()

    t = []

    for i in range(n):
        if b[i] != a[i]:
            hq.heappush(t,(-b[i],i))
    co = 0
    while t:
        k = hq.heappop(t)
        k = (-k[0],k[1])
        q,w = divmod(k[0] - a[k[1]], b[(k[1] - 1) % n] + b[(k[1] + 1) % n])
        co += q
        if q == 0:
            return -1
        w = a[k[1]] + w
        b[k[1]] = w
        if b[k[1]] != a[k[1]]:
            hq.heappush(t,(-w,k[1]))
    return co
print(onon())
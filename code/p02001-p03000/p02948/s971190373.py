import sys,collections as cl,bisect as bs,heapq as hq
sys.setrecursionlimit(100000)
mod = 10**9+7
Max = sys.maxsize

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0][0]
    su = [x[0]]
    for i in range(len(x)-1):
        if aa != x[i+1][0]:
            a.append(su)
            aa = x[i+1][0]
            su = [x[i+1]]
        else:
            su.append(x[i+1])
    a.append(su)
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))


n,m = l()

a = []

for i in range(n):
    z,x = l()
    a.append([z,x])

a.sort(key = lambda x:(x[0],-x[1]))
kkk = s(a)
co = 0
p = 0
al = []
for i in range(m):
    k = i + 1
    if p <= len(kkk)-1:
        if k >= kkk[p][0][0]:
            for ppp in kkk[p]:
                hq.heappush(al,-ppp[1])
            p += 1
    if len(al) != 0:
        an = hq.heappop(al)
        co -= an 
print(co)

import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10**9+7
Max = sys.maxsize
def l(): #intのlist
    return list(map(int,input().split()))
def m(): #複数文字
    return map(int,input().split())
def onem(): #Nとかの取得
    return int(input())
def s(x): #圧縮
    a = []
    aa = x[0]
    su = 1
    for i in range(len(x)-1):
        if aa != x[i+1]:
            a.append([aa,su])
            aa = x[i+1]
            su = 1
        else:
            su += 1
    a.append([aa,su])
    return a
def jo(x): #listをスペースごとに分ける
    return " ".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False
"""
def nibu(x,n,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2

    if rr == mid:
        return ll
    if (ここに評価入れる):
        rr = mid
    else:
        ll = mid+1
"""

n = onem()

tree = [[] for i in range(n)]

dp0 = [0 for i in range(n)]
dp1 = [0 for i in range(n)]

dp0[0] = 1
dp1[-1] = 1

for i in range(n-1):
    o,p = m()
    o -= 1
    p -= 1
    tree[o].append(p)
    tree[p].append(o)

de = cl.deque([0,-1])
co = 1
while de:
    po = de.popleft()
    if po == -1:
        co += 1
        if len(de) == 0:
            break
        de.append(-1)
        continue
    for i in tree[po]:
        if dp0[i] == 0:
            dp0[i] = co
            de.append(i)

de = cl.deque([n-1,-1])
co = 1
while de:
    po = de.popleft()
    if po == -1:
        co += 1
        if len(de) == 0:
            break
        de.append(-1)
        continue
    for i in tree[po]:
        if dp1[i] == 0:
            dp1[i] = co
            de.append(i)

dp0[0] = 0
dp1[-1] = 0

co = 0

for i in range(n):
    co += 1 if dp0[i] - dp1[i] <= 0 else -1
if co > 0:
    print("Fennec")
else:
    print("Snuke")




import sys,collections as cl,bisect as bs
sys.setrecursionlimit(100000)
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
    return "".join(map(str,x))
def max2(x): #他のときもどうように作成可能
    return max(map(max,x))
def In(x,a): #aがリスト(sorted)
    k = bs.bisect_left(a,x)
    if k != len(a) and a[k] ==  x:
        return True
    else:
        return False

def nibu(a,b,r):
    ll = 0
    rr = r
    while True:
        mid = (ll+rr)//2
        if ll == mid:
            return ll
        co = mid * a
        mm = mid
        while mm != 0:
            co += b
            mm //= 10 
        if co >= r:
            rr = mid-1
        else:
            ll = mid


n = onem()

kkk = [[] for i in range(n)]

for i in range(n-1):
    a,b = m()
    kkk[a-1].append([b-1,i+1])
    kkk[b-1].append([a-1,i+1])
de = cl.deque([[0,0,0]])
kk= []
while de:
    j,k,p = de.popleft()
    co = 1
    for i in range(len(kkk[j])):
        if not kkk[j][i][0] == k:
            if co == p:
                co += 1
            de.append([kkk[j][i][0],j,co])
            kk.append([co,kkk[j][i][1]])
            co += 1

kk.sort(key = lambda x:x[1])

print(max(kk,key = lambda x:x[0])[0])

for i in range(n-1):
    print(kk[i][0])




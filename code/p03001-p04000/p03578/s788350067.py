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
    if len(x) == 0:
        return []
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

def Topo_sort(x,y):
    co = cl.Counter(n for m in x.values() for n in m)
    S = cl.deque([i for i in range(y) if co[i] == 0])
    while S:
        n = S.popleft()
        yield n
        for i in x[n]:
            co[i] -= 1
            if co[i] <= 0:
                S.append(i)
    
    """
    if sum(co.values()) != 0:
        print(1)
        exit()
    else:
        print(0)
        exit()
    """
    #閉路検出(1が存在,0が存在しない)
# g = cl.dafaultdict(set)に有向グラフを作成し(g[~] != ~ ,yはノード数) リストが帰ってくる
n = onem()

d = l()


po = cl.defaultdict(int)

for i in range(n):
    po[str(d[i])] += 1

M = onem()

t = l()

for i in range(M):
    if po[str(t[i])]:
        po[str(t[i])] -= 1
    else:
        print("NO")
        break
else:
    print("YES")



        


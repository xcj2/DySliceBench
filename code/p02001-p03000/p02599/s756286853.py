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

def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

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


class SegmentTree:
    def segfunc(self,x,y):
        #ここに評価
        return x + y

    #nは総数、initがlist,ide_eleが元
    def __init__(self,n,init,ide_ele):
        self.n = n
        self.ide_ele = ide_ele
        self.num = 2**(n-1).bit_length()
        self.seg = [ide_ele]*2*self.num
        for i in range(n):
            self.seg[i+self.num-1] = init[i]
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2])
    
    
    def update(self,k,x):
        k += self.num-1
        self.seg[k] += x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[2*k+1],self.seg[2*k+2])
    
    def query(self,p,q):
        if q <= p:
            return self.ide_ele
        p += self.num-1
        q += self.num-2
        res = self.ide_ele
        while q-p > 1:
            if p & 1 == 0:
                res = self.segfunc(res,self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res,self.seg[q])
                q -= 1
            p //= 2
            q = (q-1)//2
        if p == q:
            res = self.segfunc(res,self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res,self.seg[p]),self.seg[q])
        return res


n,k = m()

Seg = SegmentTree(n,[0 for i in range(n)],0)
a = l()

data = []
for i in range(k):
    po = l()
    po.append(i)
    data.append(po)

data.sort(key = lambda x:x[1])

where = [-1 for i in range(n)]
ans = [0 for i in range(k)]
left = -1
for i in range(k):
    aaa = data[i]
    aaa[0] -= 1
    aaa[1] -= 1
    if aaa[1] > left:
        for j in range(left+1,aaa[1]+1):
            popopo = a[j]-1
            if where[popopo] != -1:
                Seg.update(where[popopo],-1)
            Seg.update(j,1)
            where[popopo] = j
        left = aaa[1]
    ans[aaa[2]] = Seg.query(aaa[0],aaa[1]+1)

for i in range(k):
    print(ans[i])

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
class SegmentTree:
    def segfunc(self,x,y):
        #ここに評価
        po = [0 for i in range(26)]
        for i in range(26):
            po[i] = x[i]+y[i]
        return po

    #nは総数、initがlist,ide_eleが元
    def __init__(self,n,init,ide_ele):
        self.n = n
        self.ide_ele = ide_ele
        self.num = 2**(n-1).bit_length()
        self.seg = [ide_ele for i in range(2*self.num)]
        for i in range(n):
            self.seg[i+self.num-1] = init[i]
        for i in range(self.num-2,-1,-1):
            self.seg[i] = self.segfunc(self.seg[2*i+1],self.seg[2*i+2])
    
    
    def update(self,k,x):
        k += self.num-1
        self.seg[k] = x
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[2*k+1],self.seg[2*k+2])
    
    def query(self,p,q):
        if q <= p:
            return [1 if i == 0 else 0 for i in range(26)]
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

def solver():
    n = onem()
    s = input().split()[0]
    po = onem()

    abc = [[0 for i in range(26)] for j in range(n)]

    for i in range(n):
        ppp = s[i]
        abc[i][ord(s[i]) - 97] += 1

    Se = SegmentTree(n,abc,[0 for i in range(26)])



    for i in range(po):
        a,b,c = input().split()
        a = int(a)
        b = int(b)
        if a == 1:
            ppp = [0] * 26
            ppp[ord(c) - 97] = 1
            Se.update(b-1,ppp)      
        else:
            c = int(c)
            op = Se.query(b-1,c)
            co = 0
            for i in range(26):
                if op[i] >= 1:
                    co += 1
            print(co)


if __name__ == "__main__":
    solver()


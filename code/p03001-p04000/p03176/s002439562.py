#!/usr/bin/env pypy3
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    #LIS
    N=I()
    h=LI()
    a=LI()
    
    #####segfunc######

    #評価関数（という言い方であっている？）
    def segfunc(x,y):
        return max(x,y)


    #初期化
    def init(init_val):
        #init_valは操作する数列
        for i in range(N):
            seg[i+num-1]=init_val[i]    
        #built
        for i in range(num-2,-1,-1) :
            seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
            

    #k番目の値をxに更新
    def update(k,x):
        k += num-1
        seg[k] = x
        while k:
            k = (k-1)//2
            seg[k] = segfunc(seg[k*2+1],seg[k*2+2])

            
    #[p,q)の区間に対するクエリへの応答
    def query(p,q):
        if q<=p:
            return ide_ele
        p += num-1
        q += num-2
        res=ide_ele
        while q-p>1:
            if p&1 == 0:
                res = segfunc(res,seg[p])
            if q&1 == 1:
                res = segfunc(res,seg[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = segfunc(res,seg[p])
        else:
            res = segfunc(segfunc(res,seg[p]),seg[q])
        return res


    #####単位元######
    ide_ele = 0

    #num:N以上の最小の2のべき乗
    num =2**(N-1).bit_length()
    seg=[ide_ele]*2*num
    
    ans=0
    for i in range(N):
        score=query(0,h[i]-1)+a[i]
        update(h[i]-1,score)
        ans=max(ans,score)
        
    print(ans)
    
    

main()

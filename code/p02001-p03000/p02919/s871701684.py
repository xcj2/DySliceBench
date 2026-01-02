import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    P=LI()
    #左右の自分より大きいものの位置を調べておく，2番目に近いやつまでまとめておけばよい
    #のだが，事前計算用の表を作るのにN^2かかるかも=>seg木で．
    

    #評価関数（という言い方であっている？）
    def segfunc1(x,y):
        #ここを書く！#########
        return max(x,y)

    #k番目の値をxに更新
    def update1(k,x):
        k += num-1
        seg1[k] = x
        while k:
            k = (k-1)//2
            seg1[k] = segfunc1(seg1[k*2+1],seg1[k*2+2])

            
    #[p,q)の区間に対するクエリへの応答
    def query1(p,q):
        if q<=p:
            return ide_ele1
        p += num-1
        q += num-2
        res=ide_ele1
        while q-p>1:
            if p&1 == 0:
                res = segfunc1(res,seg1[p])
            if q&1 == 1:
                res = segfunc1(res,seg1[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = segfunc1(res,seg1[p])
        else:
            res = segfunc1(segfunc1(res,seg1[p]),seg1[q])
        return res
    
    ######################################
    
    #評価関数（という言い方であっている？）
    def segfunc2(x,y):
        #ここを書く！#########
        return min(x,y)

    #k番目の値をxに更新
    def update2(k,x):
        k += num-1
        seg2[k] = x
        while k:
            k = (k-1)//2
            seg2[k] = segfunc2(seg2[k*2+1],seg2[k*2+2])

            
    #[p,q)の区間に対するクエリへの応答
    def query2(p,q):
        if q<=p:
            return ide_ele2
        p += num-1
        q += num-2
        res=ide_ele2
        while q-p>1:
            if p&1 == 0:
                res = segfunc2(res,seg2[p])
            if q&1 == 1:
                res = segfunc2(res,seg2[q])
                q -= 1
            p = p//2
            q = (q-1)//2
        if p == q:
            res = segfunc2(res,seg2[p])
        else:
            res = segfunc2(segfunc2(res,seg2[p]),seg2[q])
        return res

    #####単位元######
    ide_ele1 = 0
    ide_ele2 = 10**10



    #num:N+2以上の最小の2のべき乗
    num =2**(N+1).bit_length()
    seg1=[ide_ele1]*2*num#最大値を求める
    seg2=[ide_ele2]*2*num#最小値を求める
    
    #大きい順にみていく，みたらセグ木を更新しておく，座標=xならseg[x]=xにしておく，自分以下の最大値を見れば，左側にあるかつ自分より大きい一番近いやつの座標が取れる．
    #最小値ももてば左側でもできる．2番目に近いのも，直近から次の範囲で見ればok
    
    px=[[0,0]for _ in range(N)]
    for x in range(N):
        px[x]=[P[x],x+1]
    px.sort(reverse=True)
    
    a=[0]*(N+2)#左二番目
    b=[0]*(N+2)#左一番目
    c=[0]*(N+2)#右一番目
    d=[0]*(N+2)#右二番目

    
    update2(N+1,N+1)#他のinfよりは小さい
    
    for i in range(N):
        p=px[i][0]
        x=px[i][1]
        update1(x,x)
        update2(x,x)
        b[x]=query1(0,x)
        c[x]=query2(x+1,N+2)
        if b[x]<=0:
            a[x]=0
        else:
            a[x]=query1(0,b[x])
            
        if c[x]>=N+1:
            d[x]=N+1
        else:
            d[x]=query2(c[x]+1,N+2)
            
    ans=0
    
    
    for i in range(1,N+1):
        if b[i]!=0:
            cnt=(b[i]-a[i])*(c[i]-i)
            ans+=cnt*P[i-1]
        if c[i]!=(N+1):
            cnt=(i-b[i])*(d[i]-c[i])
            ans+=cnt*P[i-1]
            
    print(ans)
            
    
    

main()



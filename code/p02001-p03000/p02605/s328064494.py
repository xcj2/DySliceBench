import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

"""

上下 or 左右　それぞれの組はすぐ求まる．
同じライン上で上むきと下向きをまとめておいて，上向のaに対して，それよりも上にいて最も近い下向きのを探せば良い．
実際にはもっと早くできそうだけど二分探索で十分早いか

右+上　が当たる場合を考える．
u，rがそれぞれ約N個あるとして
uの中で一番左にあるやつ vs r全部
を考えて，uを左から順に見ていく？
微妙．

当たるとはdx=dyのこと
これ，右向きのやつを通る傾き-1の直線上（かつy座標が上の位置）に右向きのものがあれば当たれる．
45度回転させるか
X=x-y
Y=x+y
で反時計45度回転か．

uとrで，Y座標が同じで，rの方がX座標が小さい
dとlで，Y座標が同じで，dの方がX座標が小さい
dとrで，X座標が同じで，rの方がY座標が小さい
uとlで，X座標が同じで，uの方がY座標が小さい

だるすぎる，直線上の点をみよう，y=-x+kとすればx+y=kなので，kで場合わけ
各kでx座標が小さい順に並べておき，
u,rで，rの方がx座標が小さい
d,rで，rの方がx座標が小さい
u,lで，uの方がx座標が小さい
d,lで，dの方がx座標が小さい

"""
def main():
    import bisect
    
    mod=10**9+7
    N=I()
    M=200000 + 3
    inf = 10**10
    
    X=[0]*N
    Y=[0]*N
    U=[0]*N
    for i in range(N):
        xyu=input().split()
        X[i]=int(xyu[0])
        Y[i]=int(xyu[1])
        U[i]=xyu[2]
        
    # 同じ行/列のものを調べる
    
    # xu=[[-inf, inf]for _ in range(M)]
    xd=[[-inf, inf]for _ in range(M)]
    yl=[[-inf, inf]for _ in range(M)]
    # yr=[[-inf, inf]for _ in range(M)]
    
    for i in range(N):
        x=X[i]
        y=Y[i]
        if U[i] == "U":
            # xu[x].append(y)
            pass
        elif U[i] == "D":
            xd[x].append(y)
        elif U[i] == "L":
            yl[y].append(x)
        else:
            # yr[y].append(x)
            pass
    
    for i in range(M):
        # xu[i].sort()
        xd[i].sort()
        yl[i].sort()
        # yr[i].sort()
     
    ans_d=inf
    
    # uとかdで走査しても良いけど，全ての頂点を走査したいので此の形が楽
    for i in range(N):
        x=X[i]
        y=Y[i]
        u=U[i]
        
        if u=="U":
            num=bisect.bisect_left(xd[x], y)
            ne=xd[x][num]
            diff=ne-y
            ans_d=min(ans_d,diff)
            
        if u=="R":
            num=bisect.bisect_left(yl[y], x)
            ne=yl[y][num]
            diff=ne-x
            ans_d=min(ans_d,diff)
            
        """
        if u=="D":
            num=bisect.bisect_left(xu[x], y)
            pre=xu[x][num-1]
            diff=y-pre
            ans_d=min(ans_d,diff)

        if u=="L":
            num=bisect.bisect_left(yr[y], x)
            pre=yr[y][num-1]
            diff=x-pre
            ans_d=min(ans_d,diff)
        """
            
        # print(i,x,y,diff,ans_d)
    
    ################################################################        
    # ここから斜め

    ku=[[-inf, inf]for _ in range(M*2)]
    kd=[[-inf, inf]for _ in range(M*2)]
    kl=[[-inf, inf]for _ in range(M*2)]
    kr=[[-inf, inf]for _ in range(M*2)]  
    
    
    # y=x+k2のパターンもあるじゃん，k2=y-xなので適当に下駄を履かせる
    k2u=[[-inf, inf]for _ in range(M*2)]
    k2d=[[-inf, inf]for _ in range(M*2)]
    k2l=[[-inf, inf]for _ in range(M*2)]
    k2r=[[-inf, inf]for _ in range(M*2)]     

    for i in range(N):
        x=X[i]
        y=Y[i]
        k=x+y
        k2=y-x+M
        if U[i] == "U":
            ku[k].append(x)
            k2u[k2].append(x)
        elif U[i] == "D":
            kd[k].append(x)
            k2d[k2].append(x)
        elif U[i] == "L":
            kl[k].append(x)
            k2l[k2].append(x)
        else:
            kr[k].append(x)
            k2r[k2].append(x)
            
    for i in range(M*2):
        ku[i].sort()
        kd[i].sort()
        kl[i].sort()
        kr[i].sort()
        k2u[i].sort()
        k2d[i].sort()
        k2l[i].sort()
        k2r[i].sort()
       
    """     
    各kでx座標が小さい順に並べておき，
    u,rで，rの方がx座標が小さい
    d,rで，rの方がx座標が小さい
    u,lで，uの方がx座標が小さい
    d,lで，dの方がx座標が小さい
    """
    
    # print("---")    
    
    ans_d2=inf
    # uとかdで走査しても良いけど，全ての頂点を走査したいので此の形が楽
    for i in range(N):
        x=X[i]
        y=Y[i]
        k=x+y
        k2=y-x+M
        if U[i] == "U":
            num=bisect.bisect_left(kr[k],x)
            pre=kr[k][num-1]
            diff=x-pre
            ans_d2=min(ans_d2,diff)

            num=bisect.bisect_left(k2l[k2],x)
            ne=k2l[k2][num]
            diff=ne-x
            ans_d2=min(ans_d2,diff)
            
        elif U[i] == "D":
            num=bisect.bisect_left(k2r[k2],x)
            pre=k2r[k2][num-1]
            diff=x-pre
            ans_d2=min(ans_d2,diff)

            num=bisect.bisect_left(kl[k],x)
            ne=kl[k][num]
            diff=ne-x
            ans_d2=min(ans_d2,diff)
        
        # print(i,x,y,pre,ne,diff,ans_d2)
            
    
        
    ans = min(ans_d*5, ans_d2*10) #速度分で*10， ans_dは向かい合っているので/2
    
    if ans>=10**8:
        print("SAFE")
    else:
        print(ans)
        

# 本来safeではないものもsafeにしてしまっている，見落としがあるはず
        
        



        
        
            
    
            
            
        

main()

import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import bisect

    """
    各工事場所について，
    Dがどのレンジなら引っかかるかを記録しておく．
    最初全部のDに関して，infまで行けるものとして，
    Xが小さい順に工事区間を見て，引っかかるならば区間更新．
    一度値を決定した場所は飛ばしながら更新するようにすればO(Q)
    nxtを入れながら進めば各ノードを2回しか見ないからO(Q)
    事前のソートで NlogN
    """

    
    N,Q=MI()
    xst2=[]#x,ごとに，Dがどの範囲なら引っかかるか(s~t)
    xi=[[0,0]for _ in range(N)]
    for i in range(N):
        s,t,x=MI()
        xst2.append([x,s-x,t-x])
        xi[i]=[x,i]
    xi.sort()
    
    
    D=[0]*Q
    for i in range(Q):
        D[i]=I()
        
    inf=10**10
    ans=[inf]*(Q+4)#すこし多めにとっておく
    nxt=[0]*(Q+4)#次に見るべき番号
    for i in range(Q+4):
        nxt[i]=i+1
        
    """
    print(xi)
    print(xst2)"""
    
    
    for i in range(N):
        ii=xi[i][1]
        xx=xst2[ii][0]
        
        #0-index
        ss=bisect.bisect_left(D,xst2[ii][1])
        tt=bisect.bisect_left(D,xst2[ii][2])
        j=ss
        while j<tt:
            if ans[j]==inf:
                ans[j]=xx
            jj=j
            j=nxt[j]
            nxt[jj]=tt#次ここにきたら，ttのところまで移動するようにしておく
        """print(ii,xst2[ii][1],xst2[ii][2],xx,ss,tt)
        print(ans)
        print(nxt)"""

    
        
    for i in range(Q):
        res=ans[i]
        if res==inf:
            print(-1)
        else:
            print(res)
            
        
    
        

main()


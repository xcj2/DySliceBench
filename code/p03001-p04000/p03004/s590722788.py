import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    if N==1:
        print(0)
        exit()
    inf=10**10
    #xmax,xmin,ymax,yminそれぞれの時間変化のグラフを見ると上か下に凸ぽい，3本以下の直線で作れる
    #左右上下の値候補，-t,定数,tの時の定数部分
    #xminやxmaxなどが入れ替わるタイミングぐらいでしか最小を取り得ない
    
    X=[0]*N
    Y=[0]*N
    D=[0]*N
    
    for i in range(N):
        xyd=input().split()
        X[i]=int(xyd[0])
        Y[i]=int(xyd[1])
        D[i]=xyd[2]
        
    # x方向に-1,0,1の速度で動くそれぞれの最大値と最小値を求めるか，こいつらが交わるタイミングが大事
    # X方向か，Y方向か
    def calc_ts(S,XX):
        if S=="X":
            L="L"
            R="R"
        else:
            L="D"#min
            R="U"#max
        xmin=[inf,inf,inf]
        xmax=[-inf,-inf,-inf]
        for i in range(N):
            x=XX[i]
            d=D[i]
            if d==L:
                xmin[0]=min(xmin[0],x)
                xmax[0]=max(xmax[0],x)
            elif d==R:
                xmin[2]=min(xmin[2],x)
                xmax[2]=max(xmax[2],x)
            else:
                xmin[1]=min(xmin[1],x)
                xmax[1]=max(xmax[1],x)
        ts=[]
        
        t=xmin[0]-xmin[1]
        if t>0:
            ts.append(t)
            
        t=xmin[0]-xmin[2]
        if t>0:
            ts.append(t/2)
            
        t=xmin[1]-xmin[2]
        if t>0:
            ts.append(t)

        t=xmax[0]-xmax[1]
        if t>0:
            ts.append(t)
            
        t=xmax[0]-xmax[2]
        if t>0:
            ts.append(t/2)
            
        t=xmax[1]-xmax[2]
        if t>0:
            ts.append(t)
            
        return ts
    
    ts_all=[0]
    ts_all+=calc_ts("X",X)
    ts_all+=calc_ts("Y",Y)
    
    #t秒後の面積
    def calc(t):
        xmin=inf
        xmax=-inf
        ymin=inf
        ymax=-inf
        
        for i in range(N):
            x=X[i]
            y=Y[i]
            d=D[i]
            
            if d=="L":
                xmin=min(xmin,x-t)
                xmax=max(xmax,x-t)
                ymin=min(ymin,y)
                ymax=max(ymax,y)
            elif d=="R":
                xmin=min(xmin,x+t)
                xmax=max(xmax,x+t)
                ymin=min(ymin,y)
                ymax=max(ymax,y)
            elif d=="U":
                xmin=min(xmin,x)
                xmax=max(xmax,x)
                ymin=min(ymin,y+t)
                ymax=max(ymax,y+t)
            else:
                xmin=min(xmin,x)
                xmax=max(xmax,x)
                ymin=min(ymin,y-t)
                ymax=max(ymax,y-t)
        return (xmax-xmin)*(ymax-ymin)
    
    ans=inf**2
    for t in ts_all:
        temp=calc(t)
        ans=min(ans,temp)
        
    print(ans)
    

        
    


main()

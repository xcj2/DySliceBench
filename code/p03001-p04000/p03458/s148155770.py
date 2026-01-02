#[0,0]が白い一辺Kの四角の左下隅にあるとして，全部の希望ますが，市松模様のどの位置にいるか調べる？
#各希望マスに関して，[0,0]がどの範囲で動いても大丈夫かを調べる（グリッドが固定されているイメージ？）
#2次元累積和

import sys
input = sys.stdin.readline

N,K=map(int,input().split())
S=[[0]*(2*K+1) for _ in range(2*K+1)]


#スタート位置9箇所
dx=[0,0,K,2*K,K,0,-K,-2*K,-K,2*K,2*K,-2*K,-2*K]
dy=[0,2*K,K,0,-K,-2*K,-K,0,K,2*K,-2*K,2*K,-2*K]

#点aが(2K-1)の正方形の中にあるか?
def ch(a):
    ax=a[1]
    ay=a[0]
    if 0<=ax and ax<=2*K-1:
        if 0<=ay and ay<=2*K-1:
            return True
    return False

#4点a,b,c,dのいずれかは正方形内にある？
def ch4(a,b,c,d):
    Li=[a,b,c,d]
    for i in range(4):
        if ch(Li[i]):
            return True
    return False

#最小を0，最大を2K-1に丸める．
def app(a):
    aa=[0,0]
    for i in range(2):
        aa[i]=a[i]
        if aa[i]<0:
            aa[i]=0
        elif aa[i]>2*K-1:
            aa[i]=2*K-1
    return aa
    
#点aに対応するところにbwを与える
def paint(a,bw):
    S[a[0]][a[1]]+=bw
    return 0
    
    
    


for _ in range(N):
    sx,sy,sc=input().split()
    x=int(sx)%(2*K)
    y=int(sy)%(2*K)
    if sc=="W":
        bw=1
    else:
        bw=-1#該当箇所を-1する
        
    #スタート位置12箇所
    s=(x-(K-1),y-(K-1))
    for i in range(len(dx)):
        ld=[s[0]+dx[i],s[1]+dy[i]]#左下
        ru=[ld[0]+(K-1),ld[1]+(K-1)]#右上
        lu=[ru[0],ld[1]]
        rd=[ld[0],ru[1]]
        
        if ch4(ld,ru,lu,rd):#4点のどれかが正方形内なら
            ld=app(ld)
            ru=app(ru)
            ru[0]+=1#累積和で-1するところは領域外（1つ奥のところ）
            ru[1]+=1
            lu=[ru[0],ld[1]]
            rd=[ld[0],ru[1]]
            paint(ld,bw)
            paint(ru,bw)
            paint(lu,bw*-1)
            paint(rd,bw*-1)
            
    if bw==-1:#該当箇所が-1されているので，全部を+1する
        S[0][0]+=1
        S[-1][-1]+=1
        S[0][-1]-=1
        S[-1][0]-=1
            
            

#累積    
for i in range(2*K+1):
    for j in range(2*K):
        S[i][j+1]+=S[i][j]
        
for j in range(2*K+1):
    for i in range(2*K):
        S[i+1][j]+=S[i][j]
        
        
ans=0
for i in range(2*K+1):
    for j in range(2*K+1):
        if S[i][j]>ans:
            ans=S[i][j]
          
        
print(ans)
        


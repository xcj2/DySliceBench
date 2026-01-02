def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    from collections import deque
    
    H,W,K=MI()
    x1,y1,x2,y2=MI()
    
    C=[]
    C.append(["@"]*(W+2))
    for _ in range(H):
        c=["@"] + list(input()) + ["@"]
        C.append(c)
    C.append(["@"]*(W+2))
    
    # 各ますにつき4方向分のデータを持つ，コストは（移動回数，今直線で動いた数）でもつ，移動回数がより重要視される
    inf=10**10
    D=[[[(inf,inf)]*4 for _ in range(W+2)]for _ in range(H+2)]#下上右左の4方向
    # D[i][j][k]はi行j列k向き
    
    
    dq=deque()
    for k in range(4):
        D[x1][y1][k]=(0,0)
        dq.append((x1,y1,k,0,0))
    
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    
    
    #01BFSでいけそう
    
    while len(dq):
        x,y,d,cnt,k=dq.popleft()
        
        for nd in range(4):
            #方向そのまま
            if nd==d:
                nx=x+dx[nd]
                ny=y+dy[nd]
                nk=(k+1)%K
                ncnt=cnt
                if k+1>=K:
                    ncnt+=1
            #方向転換
            else:
                nk=0
                ncnt=cnt
                if k!=0:
                    ncnt+=1
                nx=x
                ny=y
            if C[nx][ny]==".":
                if D[nx][ny][nd] > (ncnt,nk):#更新する場合だけ
                    D[nx][ny][nd]=(ncnt,nk)
                    if ncnt==cnt:
                        dq.appendleft((nx,ny,nd,ncnt,nk))
                    else:
                        dq.append((nx,ny,nd,ncnt,nk))
                    
    ans=inf
    for d in range(4):
        temp=D[x2][y2][d][0]
        if D[x2][y2][d][1]:
            temp+=1
        ans=min(ans,temp)
        
    if ans>=inf:
        ans=-1
    print(ans)
    
    
    
    # for i in range(1,H+1):
    #     for j in range(1,W+1):
    #         print(D[i][j])
    
    
    
    
    
        
    
                    
            

main()

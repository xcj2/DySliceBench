import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    A=[]
    inf=10**6
    for _ in range(N):
        a=LI()+[inf]
        for j in range(N-1):
            a[j]-=1
        A.append(a)
        
        
    cur=[0]*N#i番目の人が何試合消化したか
    
    st=[]# stackに，みるべき人を入れていいく，変化があった人だけ見れば良い
    nxt=[]
    
    #初日は全員みる，N>=3より初日で終わることはない
    for i in range(N):
        for j in range(i+1,N):
            if A[i][0]==j and A[j][0]==i:
                cur[i]=1
                cur[j]=1
                st.append(i)
                st.append(j)
    day=1
    
    while st:
        used=[0]*N
        day+=1
        
        while st:
            i=st.pop()#みる人
            j=A[i][cur[i]]#相手候補
            
            if used[i]==0 and used[j]==0:
                if A[j][cur[j]]==i:#マッチング
                    cur[i]+=1
                    cur[j]+=1
                    nxt.append(i)
                    nxt.append(j)
                    used[i]=1
                    used[j]=1
               
        while nxt:
            a=nxt.pop()
            if cur[a]!=N-1:
                st.append(a)
        
    if sum(cur)==N*(N-1):
        print(day)
    else:
        print(-1)
        
            
        
        
    

main()

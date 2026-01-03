
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    s=input()
    t=len(s)
    #文字数が同じなら通り数は一緒なので文字数だけ見る
    
    now=[0]*(N+5)
    nxt=[0]*(N+5)
    #i回操作して，j文字になる
    
    now[0]=1
    for i in range(N):
        for j in range(i+1):
            if j!=0:
                nxt[j-1]=(nxt[j-1] + now[j])%mod
            else:
                nxt[0]=(nxt[0]+now[0])%mod
            nxt[j+1]=(nxt[j+1] + 2*now[j])%mod
        for j in range(i+2):
            now[j]=nxt[j]
            nxt[j]=0
            
    
    temp=pow(2,t,mod)            
    ans=(now[t]*pow(temp,mod-2,mod))%mod
    print(ans)

main()

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    s=input()
    s2=[0]*N
    for i in range(N):
        if s[i]=="x":
            s2[i]=1
        
    
    #0が羊，1が狼，最初の2匹を決めておく
    ans=-1
    for a in range(2):
        if ans==-1:
            for b in range(2):
                L=[0]*N
                L[0]=a
                L[1]=b
                for i in range(2,N):
                    L[i]=(L[i-2]+L[i-1]+s2[i-1])%2
                
                
                if L[0]==(L[-2]+L[-1]+s2[-1])%2 and L[1]==(L[-1]+L[0]+s2[0])%2:
                    ans=1
                    break
        
        
    if ans==-1:
        print(ans)
    else:
        ans=["S"]*N
        for i in range(N):
            if L[i]==1:
                ans[i]="W"
                
        print(''.join(map(str, ans)))
            
                
            

main()

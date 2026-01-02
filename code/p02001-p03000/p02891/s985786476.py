

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    S=list(input())
    K=I()
    
    S3=S*3
    S2=S*2
    
    ans=0
    
    N=len(S)
    
    flag=0
    if S.count(S[0])==N:
        flag=1
    
    if N==1 or flag:
        ans=(K*N)//2
    else:
        ans2=0
        for i in range(N*2-1):
            if S2[i]==S2[i+1]:
                S2[i+1]="#"
                ans2+=1
                
        ans3=0
        for i in range(N*3-1):
            if S3[i]==S3[i+1]:
                S3[i+1]="#"
                ans3+=1
                
        ansd=ans3-ans2
        if K==2:
            ans=ans2
        else:
            ans=ans2+(K-2)*ansd

        
    print(ans)

main()

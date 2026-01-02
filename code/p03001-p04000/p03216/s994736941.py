
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    S=input()
    Q=I()
    K=LI()
    ans=0
    
    
    
    for k in K:
        d=0
        m=0
        temp=0
        ans=0
        for i in range(k):
            if S[i]=="D":
                d+=1
            elif S[i]=="M":
                m+=1
                temp+=d
            elif S[i]=="C":
                ans+=temp
                #print(0,i,d,m)
        
        for i in range(k,N):
            if S[i-k]=="D":
                d-=1
                temp-=m
            elif S[i-k]=="M":
                m-=1
            
            if S[i]=="D":
                d+=1
            elif S[i]=="M":
                m+=1
                temp+=d
            elif S[i]=="C":
                ans+=temp
                #print(1,i,d,m)
                
        print(ans)
            
                
                
            
            
            

main()

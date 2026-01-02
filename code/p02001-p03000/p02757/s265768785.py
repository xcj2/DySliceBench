
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N,P=MI()
    s=input()
    ans=0
    if P==2 or P==5:
        for i in range(N):
            t=int(s[i])
            if t%P==0:
                ans+=i+1
            
    else:
        ans=0
        t=0
        mod=[0]*P
        mod[0]=1
        for i in range(N):
            t=t+int(s[N-i-1])*pow(10,i,P)
            t=t%P
            mod[t]+=1
            if mod[t]>=2:
                ans+=mod[t]-1
                

            

    print(ans)   
        
    
            
    
        
    

main()

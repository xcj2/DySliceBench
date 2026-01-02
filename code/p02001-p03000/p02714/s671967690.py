

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N=I()
    S=input()
    r=S.count("R")
    g=S.count("G")
    b=S.count("B")
    ans=r*g*b
    
    for i in range(N):
        for j in range(i+1,N):
            if S[i]!=S[j]:
                diff=j-i
                k=j+diff
                if k<N:
                    if S[i]!=S[k] and S[j]!=S[k]:
                        ans-=1
                        
                        
    print(ans)
                        
                
            

main()

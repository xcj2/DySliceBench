
def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    import bisect
    
    mod=10**9+7
    s=input()
    t=input()
    
    L=[[]for _ in range(26)]
    
    N=len(s)
    for i in range(N):
        c=ord(s[i])-97
        L[c].append(i)
        
    cur=-1
    rep=0
    
    M=len(t)
    for i in range(M):
        c=ord(t[i])-97
        if len(L[c])==0:
            print(-1)
            exit()
            
        num=bisect.bisect_right(L[c],cur)
        if num>=len(L[c]):
            rep+=1
            num=0
        cur=L[c][num]
        
    ans=N*rep + cur + 1
    print(ans)
        
        
        

main()

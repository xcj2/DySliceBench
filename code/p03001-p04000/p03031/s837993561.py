import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    s=[]
    for i in range(M):
        L=LI()
        s.append(L[1:])
    p=LI()
    
    import itertools
    
    ans=0
    for ite in itertools.product([0,1], repeat=N):
        flag=1
        for i in range(M):
            temp=0
            for ss in s[i]:
                if ite[ss-1]:
                    temp+=1
            if temp%2==p[i]:
                pass
            else:
                flag=0
        if flag:
            ans+=1
            
    print(ans)
                
                
            
        

main()

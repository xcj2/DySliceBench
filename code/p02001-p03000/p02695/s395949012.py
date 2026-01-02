import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M,Q=MI()
    a=[0]*Q
    b=[0]*Q
    c=[0]*Q
    d=[0]*Q
    
    for i in range(Q):
        a[i],b[i],c[i],d[i]=MI()
        
    import itertools
    ans=0
    
    
    
    for ite in itertools.combinations_with_replacement(range(1,M+1), N):
        temp=0
        for i in range(Q):
            if ite[b[i]-1]-ite[a[i]-1] == c[i]:
                temp+=d[i]
        ans=max(ans,temp)
        
    print(ans)
    
    
    
main()

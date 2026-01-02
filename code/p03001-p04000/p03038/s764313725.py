import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    N,M=MI()
    A=LI()
    B=[0]*M
    C=[0]*M
    for i in range(M):
        B[i],C[i]=MI()
    
    C,B=zip(*sorted(zip(C,B)))
    B=B[::-1]
    C=C[::-1]
    
    import heapq
    heapq.heapify(A)
    
    for i in range(M):
        b=B[i]
        c=C[i]
        for _ in range(b):
            a=heapq.heappop(A)
            if a>=c:
                heapq.heappush(A,a)
                break
            else:
                heapq.heappush(A,c)
                
    ans=0
    for i in range(N):
        a=heapq.heappop(A)
        ans+=a
        
    print(ans)

main()

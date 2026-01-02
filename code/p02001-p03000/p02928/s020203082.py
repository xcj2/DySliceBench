import sys
input = sys.stdin.readline

def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    mod=10**9+7
    import bisect
    
    N,K=MI()
    A=LI()
    

    rev0=0
    for i in range(N):
        for j in range(N):
            if A[i]>A[j]:
                if j>=i:
                    rev0+=(K*(K+1))//2
                else:
                    rev0+=(K*(K-1))//2
            rev0%=mod
                

        
    print(rev0)
        
               
    

main()

import sys
from bisect import bisect_left,bisect_right
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,M=map(int,input().split())
    A=sorted(list(map(int,input().split())))
    S=[0]*(N+1)
    for i in range(N):
        S[i+1]=S[i]+A[i]
    def nibutan(ok,ng):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve(mid):
        c=0
        for i in range(N):
            c+=N-bisect_left(A,mid-A[i])
        if c>=M:
            return True
        else:
            return False
        
    x=nibutan(0,10**11)
    ans=0
    count=0
    for i in range(N):
        b_l=bisect_left(A,x-A[i])
        count+=(N-b_l)
        ans+=S[N]-S[b_l]+A[i]*(N-b_l)
    if count==M:
        print(ans)
    else:
        print(ans+(M-count)*x)
    

if __name__ == '__main__':
    main()

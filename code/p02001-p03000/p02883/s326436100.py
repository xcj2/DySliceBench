import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    F=list(map(int,input().split()))
    F.sort(reverse=True)
    
    def nibutan(ok,ng):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve(mid):
        k=0
        for i in range(N):
            k+=max(0,-(-(A[i]*F[i]-mid)//F[i]))
        if k<=K:
            return True
        else:
            return False
    
    print(nibutan(10**18,-1))
        
    
    

if __name__ == '__main__':
    main()

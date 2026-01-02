import sys
from bisect import *
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    def nibutan(ok,ng):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    
    N,M,V,P=map(int,input().split())
    A=sorted(list(map(int,input().split())))
    
    def solve(mid):
        point=A[mid]+M
        z=0
        c=0
        i=1
        while c<P-1:
            if N-i!=mid:
                z+=max(min(M+A[N-i]-point,M),0)
                c+=1
            i+=1
        for i in range(N):
            if i!=mid:
                z+=min(M,max(point-A[i],0))
        if point>=A[N-P] and z>=M*(V-1):
            return True
        else:
            return False
        
    print(N-nibutan(N-1,-1))

if __name__ == '__main__':
    main()

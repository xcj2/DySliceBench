import sys
from bisect import bisect_left,bisect_right
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input(): return sys.stdin.readline().rstrip()

def main():
    N,K=map(int,input().split())
    A=list(map(int,input().split()))
    A.sort()
    A_minus,A_zero,A_plus=[],[],[]
    x=bisect_left(A,0)
    y=bisect_right(A,0)
    A_minus=A[:x]
    A_minus=list(reversed(list(map(lambda x: -x,A_minus))))
    A_zero=A[x:y]
    A_plus=A[y:]
    if K<=len(A_minus)*len(A_plus):
        def nibutan1(ok,ng):
            while abs(ok-ng) > 1:
                mid = (ok + ng) // 2
                if solve1(mid):
                    ok = mid
                else:
                    ng = mid
            return ok
        
        def solve1(mid):
            c=0
            z=bisect_left(A_plus,-(-mid//A_minus[0]))
            c+=len(A_plus)-z
            for x in A_minus[1:]:
                if z>0 and A_plus[z-1] >= -(-mid//x):
                    while z>0 and A_plus[z-1] >= -(-mid//x):
                        z-=1
                c+=len(A_plus)-z
            if c>=K:
                return True
            else:
                return False
        
        print(-nibutan1(0,10**18+1))
    K-=len(A_minus)*len(A_plus)
    if 0<K<=len(A_zero)*(N-len(A_zero))+(len(A_zero)*(len(A_zero)-1))//2:
        print(0)
    K-=len(A_zero)*(N-len(A_zero))+(len(A_zero)*(len(A_zero)-1))//2
    if K>0:
        def nibutan2(ok,ng):
            while abs(ok-ng) > 1:
                mid = (ok + ng) // 2
                if solve2(mid):
                    ok = mid
                else:
                    ng = mid
            return ok
        
        def solve2(mid):
            c=0
            if len(A_minus)>1:
                z=bisect_right(A_minus,mid//A_minus[0])
                c+=z
                if mid//A_minus[0]>=A_minus[0]:
                    c-=1
                for x in A_minus[1:]:
                    if z>0 and A_minus[z-1] > mid//x:
                        while z>0 and A_minus[z-1] > mid//x:
                            z-=1
                    c+=z
                    if mid//x>=x:
                        c-=1
            if len(A_plus)>1:
                z=bisect_right(A_plus,(mid//A_plus[0]))
                c+=z
                if (mid//A_plus[0])>=A_plus[0]:
                    c-=1
                for x in A_plus[1:]:
                    if z>0 and A_plus[z-1] > mid//x:
                        while z>0 and A_plus[z-1] > mid//x:
                            z-=1
                    c+=z
                    if mid//x>=x:
                        c-=1
            c//=2
            if c>=K:
                return True
            else:
                return False
        
        print(nibutan2(10**18+1,0))

    
        
    

if __name__ == '__main__':
    main()

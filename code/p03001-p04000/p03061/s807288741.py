import sys
from math import sqrt
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    N=int(input())
    A=list(map(int,input().split()))
    divisor=set()
    for x in range(1,int(sqrt(A[0]))+1):
        if A[0]%x==0:
            divisor.add(x)
            divisor.add(A[0]//x)
    for x in range(1,int(sqrt(A[1]))+1):
        if A[1]%x==0:
            divisor.add(x)
            divisor.add(A[1]//x)
    
    def solve(mid):
        f=False
        for x in A:
            if x%mid:
                if f:
                    return False
                else:
                    f=True
        return True
    
    ans=0
    for d in divisor:
        if solve(d):
            ans=max(ans,d)
    print(ans)
    

if __name__ == '__main__':
    main()

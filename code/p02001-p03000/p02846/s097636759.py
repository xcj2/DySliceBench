import sys
sys.setrecursionlimit(10**9)
INF=10**18
def input():
    return sys.stdin.readline().rstrip()

def main():
    def nibutan(ok,ng):
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve(mid,2):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve(mid,n):
        dif=(d_0+d_1)*(mid-1)
        c=0
        if dif*(dif+d_0) == 0:
            c+=1
        elif dif*(dif+d_0) < 0:
            c+=1
            if (dif+d_0)*(dif+d_0+d_1) < 0:
                c+=1
        if c==n:
            return True
        else:
            return False
    
    T=list(map(int,input().split()))
    A=list(map(int,input().split()))
    B=list(map(int,input().split()))
    d_0=T[0]*(A[0]-B[0])
    d_1=T[1]*(A[1]-B[1])
    if d_0==-d_1:
        print('infinity')
    elif d_0*(d_0+d_1)<0:
        if (d_0*2+d_1)*(d_0*2+d_1*2)<0:
            n=nibutan(2,10**40)
            ans=n*2-1
            ans+=solve(n+1,1)
            print(ans)
        else:
            print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()

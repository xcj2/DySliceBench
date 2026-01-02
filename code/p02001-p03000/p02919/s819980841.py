import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
def input():
    return sys.stdin.readline().rstrip()

def main():
    class BIT():
        def __init__(self,n):
            self.num=n
            self.dat=[0]*(self.num+1)
        
        def add(self,i,x):
            i+=1
            while i<=self.num:
                self.dat[i]+=x
                i+=i&-i
        
        def sum(self,i):
            i+=1
            s=0
            while i>0:
                s+=self.dat[i]
                i-=i&-i
            return s
    
    N=int(input())
    P=list(map(int,input().split()))
    P2=[(P[i],i) for i in range(N)]
    P2.sort(reverse=True)
    b=BIT(N)
    
    def nibutan(i,num,ok,ng):
        b_sum_i=b.sum(i)
        while abs(ok-ng) > 1:
            mid = (ok + ng) // 2
            if solve(b_sum_i,i,num,mid):
                ok = mid
            else:
                ng = mid
        return ok
    
    def solve(b_sum_i,i,num,mid):
        if i>mid:
            if b_sum_i-b.sum(mid-1) >= num:
                return True
        else:
            if b.sum(mid)-b_sum_i >= num:
                return True
        return False
    
    ans=0
    for p in P2:
        x=b.sum(p[1])
        y=b.sum(N-1)
        if x>=1 or y-x>=1:
            s=nibutan(p[1],1,-1,p[1])
            t=nibutan(p[1],2,-1,p[1])
            u=nibutan(p[1],1,N,p[1])
            v=nibutan(p[1],2,N,p[1])
            if x>=1:
                ans+=p[0]*(s-t)*(u-p[1]) if s>-1 else 0
            if y-x>=1:
                ans+=p[0]*(v-u)*(p[1]-s) if u<N else 0
        b.add(p[1],1)
    
    print(ans)
    

if __name__ == '__main__':
    main()

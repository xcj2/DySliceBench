from bisect import bisect_left
import sys
input = sys.stdin.readline

class SegmentTree():
    def __init__(self,size,func,default):
        self.leaf=2**(size-1).bit_length()
        self.data=[default]*(2*self.leaf-1)
        self.f=func; self.d=default
    def rangeupdate(self,l,r,x):
        l+=self.leaf-1; r+=self.leaf-1
        while l<r:
            if not l&1:
                self.data[l]=self.f(self.data[l],x)
                l+=1
            if not r&1:
                r-=1
                self.data[r]=self.f(self.data[r],x)
            l>>=1; r>>=1
    def getvalue(self,i):
        k=i+self.leaf-1
        ret=self.d
        while k>=0:
            ret=self.f(ret,self.data[k])
            k=(k-1)>>1
        return ret

#最大値            
def segfunc(x,y):
    return max(x,y)

#最小値
def segfunc2(x,y):
    return min(x,y)
#和
def segfunc3(x,y):
    return x | y


def main():
    N, Q = map(int, input().split())
    construction = []
    for _ in range(N):
        S, T, X = map(int, input().split())
        construction.append([S,T,X])

    D = [int(input()) for _ in range(Q)]
    seg = SegmentTree(Q,segfunc2,float('inf'))

    for i in range(N):
        S, T, X = construction[i]
        l = bisect_left(D, S - X)
        r = bisect_left(D, T - X)
        seg.rangeupdate(l, r, X)
    
    for q in range(Q):
        ans = seg.getvalue(q)
        if ans == float('inf'):
            print(-1)
        else:
            print(ans)

if __name__ == "__main__":
    main()
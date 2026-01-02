printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18
R = 998244353

def ddprint(x):
  if DBG:
    print(x)


class Segtree:
    # modify UNIT and oper depending on the reduce operation

    #UNIT = 0  # sum/or:0 and:fff..f min:BIG max:-BIG gcd:0 lcm:1 ..

    #@classmethod
    #def oper(c,x,y):
    #    return x|y  # sum:+ or/and/min/max/gcd/lcm:(same)

    # call like this: sgt = Segtree(n, 0, lambda x,y: max(x,y))

    def __init__(s,l,unit,oper):
        s.unit = unit
        s.oper = oper
        s.n = 1
        while s.n<l:
            s.n *= 2
        s.ary = [s.unit for i in range(2*s.n-1)]

    def get(s,i):
        return s.ary[i+s.n-1]

    def set(s,i,v):
        k = i+s.n-1
        s.ary[k] = v
        while k>0:
            k = (k-1)//2
            s.ary[k] = max( \
                        s.ary[2*k+1], s.ary[2*k+2])

    def setary(s,a):
        for i,v in enumerate(a):
            s.ary[i+s.n-1] = v
        for k in range(s.n-2,-1,-1):
            s.ary[k] = max( \
                        s.ary[2*k+1], s.ary[2*k+2])

    def query(s,x,y):
        l = x+s.n-1
        r = y+s.n-1
        res = s.unit
        while l<r:
            if not l%2:
                res = s.oper(res,s.ary[l])
                l += 1
            if not r%2:
                r -= 1
                res = s.oper(res,s.ary[r])
            l >>= 1
            r >>= 1
        return res


    def query2(s,x,y):
        return s.querycore(x,y,0,0,s.n)

    # x,y: from query  k: suffix at focus l,r: range for k
    # right ends (y,r) not included

    def querycore(s,x,y,k,l,r):
        if r<=x or y<=l:
            return s.unit
        if x<=l and r<=y:
            return s.ary[k]
        vl = s.querycore(x,y,2*k+1,l,(l+r)//2)
        vr = s.querycore(x,y,2*k+2,(l+r)//2,r)
        return max(vl, vr)

# # # #
from bisect import bisect_left
n = inn()
xd = []
for i in range(n):
    xx,dd = inm()
    xd.append((xx,dd))
xd.sort()
x = [xd[i][0] for i in range(n)]

#ddprint(xd)
#ddprint(x)

r = [i for i in range(n)]
sgt = Segtree(n,0,lambda x,y: max(x,y))
sgt.setary(r)
f = [0]*(n+1)
f[n] = 1
f[n-1] = 2
for i in range(n-2,-1,-1):
    xx,dd = xd[i]
    j = bisect_left(x,xx+dd)
    k = sgt.query(i,j)
    sgt.set(i,k)
    f[i] = (f[i+1] + f[k+1])%R
    #ddprint(f"i {i} x {xx} d {dd} j {j}")

#ddprint(f)
print(f[0])

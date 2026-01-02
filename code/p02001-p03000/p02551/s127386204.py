#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7
#R = 998244353

def ddprint(x):
  if DBG:
    print(x)


# # # # class Segtree # # # #

#      0
#   1     2
# 3   4  5  6
#       :
# leaf i - n-1+i
# parent   - (i-1)//2
# children - 2*i+1, 2*i+2

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
            s.ary[k] = s.oper( \
                        s.ary[2*k+1], s.ary[2*k+2])

    def setary(s,a):
        for i,v in enumerate(a):
            s.ary[i+s.n-1] = v
        for k in range(s.n-2,-1,-1):
            s.ary[k] = s.oper( \
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


# # # # class Segtree end # # # #


n,q = inm()
b = (n-2)**2
minx = x = n-1
miny = y = n-1
sx = Segtree(n,n-1,lambda x,y: min(x,y))
sy = Segtree(n,n-1,lambda x,y: min(x,y))
z = [n-1]*n
sx.setary(z)
sy.setary(z)
#ddprint(sx.ary)
#ddprint(sy.ary)
for i in range(q):
    t,k = inm()
    k -= 1
    if t==1:
        b -= sy.query(k,n)-1
        if k<minx:
            sx.set(miny,k)
            minx = k
    else:
        b -= sx.query(k,n)-1
        if k<miny:
            sy.set(minx,k)
            miny = k
    #ddprint(f"{i=} {b=} {minx=} {miny=}")
    #ddprint(sx.ary)
    #ddprint(sy.ary)
print(b)

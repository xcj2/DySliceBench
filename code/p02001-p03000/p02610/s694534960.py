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
t = inn()
for tt in range(t):
    #ddprint(f"{tt=}")
    n = inn()
    klr = []
    nl = 0
    for i in range(n):
        k,l,r = inm()
        klr.append((abs(l-r),(-k if l>r else -(n+1-k)),i,k,l,r))
        if l>r:
            nl += 1
    klrc = [z for z in klr]
    klr.sort(reverse=True)
    h = {}
    tol = Segtree(n,-1,lambda x,y: max(x,y))
    tor = Segtree(n,n+1,lambda x,y: min(x,y))
    tol.setary(list(range(n)))
    tor.setary(list(range(n)))
    for j in range(n):
        v,w,i,k,l,r = klr[j]
        if k==n:
            continue
        if l>r:
            x = min(nl-1,k-1)
            m = tol.query(0,x+1)
            if m<0:
                continue
            tol.set(m,-1)
            h[m] = i
        else:
            x = max(nl,k)
            m = tor.query(x,n)
            if m>n:
                continue
            tor.set(m,n+1)
            h[m] = i
        #ddprint(f"{j=} {i=} {x=} {m=} {k=} {l=} {r=} {v=} {w=}")
    #ddprint(f"h1 {h}")
    put = {}
    for x in h:
        put[h[x]] = 1
    top = 0
    for i in range(n):
        if i in put:
            continue
        while top in h:
            top += 1
        h[top] = i
    #ddprint(f"h2 {h}")
    rev = [-1]*n
    sm = 0
    for i in range(n):
        j = h[i]
        v,w,ii,k,l,r = klrc[j]
        sm += l if i<=k-1 else r
        #ddprint(f"{i=} {j=} {k=} {sm=}")
    print(sm)

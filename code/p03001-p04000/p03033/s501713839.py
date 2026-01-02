#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True  and False
BIG = 10**18 if not DBG else 99999
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
xs = set([])
stx = []
for i in range(n):
    s,t,x = inm()
    xs.add(x)
    xs.add(s-x)
    xs.add(t-x)
    stx.append((s-x,t-x,x))
stx.sort()

di = []
ans = [-1]*q
for i in range(q):
    d = inn()
    xs.add(d)
    di.append(d)

x2i = {}
i2x = list(xs)
m = len(xs)
i2x.sort()
for i,x in enumerate(i2x):
    x2i[x] = i

stx2 = []
for i in range(n):
    s,t,x = stx[i]
    stx2.append((x2i[s],x2i[t],x2i[x]))
d2 = [x2i[d] for d in di]

sgt = Segtree(m,BIG,lambda x,y: min(x,y))
top = 0
for j in range(q):
    d = d2[j]
    while top<n:
        s,t,x = stx2[top]
        if s>d:
            break
        if x<sgt.get(t-1):
            sgt.set(t-1,x)
        top += 1
    x = sgt.query(d,m)
    if x==BIG:
        print(-1)
    else:
        print(i2x[x])

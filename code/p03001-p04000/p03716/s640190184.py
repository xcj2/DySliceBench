#from collections import deque,defaultdict
printn = lambda x: print(x,end='')
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
ins = lambda : input().strip()
DBG = True # and False
BIG = 10**18
R = 10**9 + 7

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
import heapq
n = inn()
a = inl()

lmax = a[:n]
lsum = sum(lmax)
heapq.heapify(lmax)

r = a[n:]
r = [(r[i],i) for i in range(2*n)]
r.sort()
rsum = sum([x[0] for x in r[:n]])
rmax = [BIG]*(2*n)
h = {}
for v,i in r[n:]:
    if v not in h:
        h[v] = []
    h[v].append(i)
    rmax[i] = v
sgt = Segtree(2*n,BIG,lambda x,y: min(x,y))
sgt.setary(rmax)

if False:
    ddprint(a)
    #ddprint(f"{n=} {lsum=} {rsum=}")
    ddprint(lmax)
    ddprint(rmax)
    ddprint(h)

mx = lsum - rsum
for i in range(n):
    v = a[n+i]
    v2 = heapq.heappushpop(lmax,v)
    lsum += v-v2
    if sgt.get(i)==BIG:
        vnew = sgt.query(i+1,2*n)
        rsum += vnew-v
        suf = h[vnew].pop()
        sgt.set(suf,BIG)
        #ddprint(f"{i=} {v=} {v2=} {vnew=} {suf=} {lsum=} {rsum=}")
    mx = max(mx,lsum-rsum)

print(mx)

import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))
from functools import reduce

def segfunc(a,b):
    if a == 0 or b == 0:
        return 0
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    return segfunc(b, r)

def gcd_list(numbers):
    return reduce(segfunc, numbers)

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res


n = ii()
A = sorted(li())

#####単位元######
if n == 2:
    print(max(A))
    exit()
elif n == 3:
    ide_ele = max(segfunc(A[0], A[1]), segfunc(A[1], A[2]), segfunc(A[0], A[2]))
else:
    ide_ele = max(segfunc(A[-1], A[-2]), segfunc(A[-3], A[-4]))

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init(A)
ans = 0

#ans = max(query(1, n), ans)
#for i in range(1, n-1):
for i in range(n):
    #print(i, query(0, i), query(i+1, n))
    ans = max(segfunc(query(0, i), query(i+1, n)), ans)
#ans = max(query(0, n-1), ans)

print(ans)
import sys
input = sys.stdin.readline
N = int(input())
S = input()
Q = int(input())

ide_ele = 0

def segfunc(x,y):
    return x|y

def init(init_val):
    #set_val
    for i in range(N):
        seg[i+num-1]=1<<(ord(init_val[i])-ord('a'))
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    x = 1<<(ord(x)-ord('a'))
    if x == seg[k]: return
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

#num:n以上の最小の2のべき乗
num =2**(N-1).bit_length()
seg=[ide_ele]*2*num

init(S)

for _ in range(Q):
    t, a, b = input().split()
    if t == '1':
        a = int(a)
        update(a-1, b)
    else:
        a, b = int(a)-1, int(b)
        print(bin(query(a,b)).count('1'))

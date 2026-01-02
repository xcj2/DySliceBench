import sys
input = sys.stdin.readline

n = int(input())
s = list(str(input()))
q = int(input())

s = [ord(c)-ord('a') for c in s]

#def segfunc(x,y):
    #return x | y

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]={init_val[i]}
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=seg[2*i+1] | seg[2*i+2]

def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = seg[k*2+1] | seg[k*2+2]

def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = res | seg[p]
        if q&1 == 1:
            res = res | seg[q]
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = res | seg[p]
    else:
        res = (res | seg[p]) | seg[q]
    return res

#####単位元######
ide_ele = set()

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init(s)
#print(seg)

for i in range(q):
    t, x, y = map(str, sys.stdin.readline().split())
    if t == '2':
        l = int(x)-1
        r = int(y)-1
        print(len(query(l, r+1)))
    else:
        i = int(x)-1
        c = {ord(y)-ord('a')}
        update(i, c)

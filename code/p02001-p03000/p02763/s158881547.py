import sys
input = sys.stdin.readline
#####segfunc######
def segfunc(x,y):
    return x | y

def init(init_val):
    #set_val
    for i in range(len(init_val)):
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

#####単位元######
n = int(input())
s = list(input())[:-1]
ide_ele = 0
num =2**(n-1).bit_length()
seg=[ide_ele]*(2*num - 1)
s = [2 ** (ord(i) - ord('a')) for i in s]
init(s)
q = int(input())
for i in range(q):
    tmp = input()
    a,b,c = tmp[:-1].split()
    if a == "1":
        update(int(b)-1, 2 ** (ord(c) - ord('a')))
    else:
        if b == c:
            print(1)
        else:
            tmp = query(int(b)-1, int(c))
            tmp = format(tmp, 'b')
            print(tmp.count('1'))
n = int(input())
s = input()
q = int(input())
C = [0]*n
for i, k in enumerate(s):
  C[i] = 1<<(ord(k)-ord("a"))

#####segfunc######
#def segfunc(x,y):
#    return 

def segfunc(a,b):
  return a | b

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = 1<<x
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
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init(C)
for _ in range(q):
  t, a, b = input().split()
  if t == "1":
    w = ord(b) - ord("a")
    update(int(a)-1, w)
  else:
    ans = query(int(a)-1, int(b))
    print(bin(ans).count("1"))
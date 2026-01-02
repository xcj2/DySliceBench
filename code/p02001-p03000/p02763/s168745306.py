import sys
input = sys.stdin.readline
n = int(input())

ss = list(input())
s = []
for i in range(n):
    s.append(1<<(ord(ss[i])-97))

#####segfunc######
def segfunc(x,y):
    #print(x|y)
    return x | y

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
    
def query(p,q,k,l,r):
    if r<=p or q<=l:
        return ide_ele
    if p<=l and r<=q:
        return seg[k]
    else:
        vl = query(p,q,k*2+1,l,(r+l)//2)
        vr = query(p,q,k*2+2,(l+r)//2,r)
        return segfunc(vl,vr)

#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num
init(s)


def popcnt(n):
    c = (n & 0x5555555555555555) + ((n>>1) & 0x5555555555555555)
    c = (c & 0x3333333333333333) + ((c>>2) & 0x3333333333333333)
    c = (c & 0x0f0f0f0f0f0f0f0f) + ((c>>4) & 0x0f0f0f0f0f0f0f0f)
    c = (c & 0x00ff00ff00ff00ff) + ((c>>8) & 0x00ff00ff00ff00ff)
    c = (c & 0x0000ffff0000ffff) + ((c>>16) & 0x0000ffff0000ffff)
    c = (c & 0x00000000ffffffff) + ((c>>32) & 0x00000000ffffffff)
    return c

q = int(input())

for i in range(q):
    qq,xx,yy = map(str,input().split())
    if qq == '1':
        xx = int(xx)
        update(xx-1,1<<(ord(yy)-97))
    else:
        xx,yy = int(xx),int(yy)
        res = query(xx-1,yy,0,0,num)
        print(popcnt(res))

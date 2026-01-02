#####segfunc######
def segfunc(x,y):
    return x + y

def init(init_val,j):
    #set_val
    for i in range(n):
        seg[j][i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[j][i]=segfunc(seg[j][2*i+1],seg[j][2*i+2]) 
    
def update(k,x,j):
    k += num-1
    seg[j][k] = x
    while k:
        k = (k-1)//2
        seg[j][k] = segfunc(seg[j][k*2+1],seg[j][k*2+2])
    
def query(p,q,j):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[j][p])
        if q&1 == 1:
            res = segfunc(res,seg[j][q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[j][p])
    else:
        res = segfunc(segfunc(res,seg[j][p]),seg[j][q])
    return res


n = int(input())
s = list(input())
q = int(input())
al = []
l = [[0 for i in range(n)] for i in range(26)]
for i in range(n):
    l[ord(s[i])-97][i] = 1
seg = [[] for i in range(26)]
for i in range(26):
#####単位元######
    ide_ele = 0
#num:n以上の最小の2のべき乗
    num =2**(n-1).bit_length()
    seg[i]=[ide_ele]*2*num
    init(l[i],i)
for i in range(q):
    q1 = list(input().split())
    if q1[0] == "1":
        p = int(q1[1])
        r = ord(q1[2]) - 97
        for j in range(26):
            if l[j][p-1] == 1 and j != r:
                update(p-1,0,j)
            elif j == r:
                update(p-1,1,j)
            else:
                update(p-1,0,j)
    else:
        a = int(q1[1])
        b = int(q1[2])
        #print(a,b,seg)
        aa = 0
        for j in range(26):
            if query(a-1,b,j) > 0:
                aa += 1
        al.append(aa)
for i in al:
    print(i)
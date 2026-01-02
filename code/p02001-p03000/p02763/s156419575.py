n=int(input())
s=list(input())
q=int(input())
def segfunc(x,y):
    return x|y
def init(init_val,var):
    #set_val
    for i in range(n):
        seg[var][i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[var][i]=segfunc(seg[var][2*i+1],seg[var][2*i+2]) 
    
def update(k,x,var):
    k += num-1
    seg[var][k] = x
    while k:
        k = (k-1)//2
        seg[var][k] = segfunc(seg[var][k*2+1],seg[var][k*2+2])
    
def query(p,q,var):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[var][p])
        if q&1 == 1:
            res = segfunc(res,seg[var][q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[var][p])
    else:
        res = segfunc(segfunc(res,seg[var][p]),seg[var][q])
    return res

#####単位元######
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[[ide_ele]*2*num for i in range(26)]
for i in range(n):
    update(i,1,ord(s[i])-97)
for i in range(q):
    a,b,c=input().split()
    if a=="1":
        update(int(b)-1,0,ord(s[int(b)-1])-97)
        s[int(b)-1]=c
        update(int(b)-1,1,ord(c)-97)
    else:
        ans=0
        for j in range(26):
            ans+=query(int(b)-1,int(c),j)
        print(ans)
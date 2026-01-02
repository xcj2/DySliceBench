#'init(a)': 配列aで初期化。O(N)
#'update(k,x)': a[k]をxに変更 O(logN)
#'query(p,q)': [p,q)について "segfunc" したものを返す O(logN)
#'ide_ele' : 単位元。単位元(ide_ele)は、区間外の値などに設定する値です。

def gcd(x,y):
    if x==0:
        return y
    if y==0:
        return x
    if x==y:
        return x
    elif x>y:
        r=-1
        while r!=0:
            r=x%y
            x=y
            y=r
        return x
    else:
        r=-1
        while r!=0:
            r=y%x
            y=x
            x=r
        return y

#####segfunc######
def segfunc(x,y):
    return gcd(x,y)

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
    while k+1:
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
#単位元。単位元(ide_ele)は、区間外の値などに設定する値です。
#            ex) 最小値のセグ木 → +inf
#             　　和のセグ木 → 0
#　　             積のセグ木 → 1
#　　             gcdのセグ木 → 0
ide_ele = 0

n=int(input())
a=list(map(int,input().split()))

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init(a)
ans=0
for i in range(n):
    ans=max(ans,gcd(query(0,i),query(i+1,n)))

print(ans)

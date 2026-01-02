import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())
lst1 = list(map(int,readline().split()))
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a*b//gcd(a,b))
#####segfunc######
def segfunc(x,y):
    return gcd(x,y)

def init(init_val): #渡されたリストでsegを初期化
    #set_val
    for i in range(len(init_val)):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x): #segの要素kをxに変更(セグ木全体の更新)
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q): #区間[p,q)での、segfuncに準じた値を返す
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
"""
最小値のセグ木 → 10**9　(最小値の更新に影響しないため)
　　和のセグ木 → 0　(上の単位元の説明を参照)
　　積のセグ木 → 1　(上の単位元の説明を参照)
　　gcdのセグ木 → 0　(gcdを更新しない値は0)
"""
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num #単位元の配列(計算結果に影響を及ぼさない配列)
init(lst1)
ans = 0
for i in range(n):
    if i == 0:
        ans = max(ans,query(1,n))
    elif i == n-1:
        ans = max(ans,query(0,n-1))
    else:
        ans = max(ans,gcd(query(0,i),query(i+1,n)))

print(ans)
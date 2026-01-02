import sys
readline = sys.stdin.buffer.readline
kijun = ord("a")
n = int(readline())
s = readline().rstrip().decode('utf-8')
q = int(readline())
lst1 = [0]*n

def pow(n,p): #繰り返し二乗法(nのp乗)
    res = 1
    while p > 0:
        if p % 2 == 0:
            n = n ** 2
            p //= 2
        else:
            res = res * n
            p -= 1
    return res

for i in range(n):
    lst1[i] = pow(2,(ord(s[i])-kijun))
#####segfunc######
def segfunc(x,y):
    return x|y

def init(init_val): #渡されたリストでsegを初期化
    #set_val
    for i in range(n):
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
seg=[ide_ele]*2*num #単位元の配列(計算結果に影響を及ぼさない配列)を作成

init(lst1)

def judge(u):
    res = 0
    for i in range(27):
        if u>>i & 1:
            res += 1
    return res

for i in range(q):
    t,x,y = readline().rstrip().decode('utf-8').split()
    if t == "1":
        update(int(x)-1,pow(2,ord(y)-kijun))
    else:
        print(judge(query(int(x)-1,int(y))))

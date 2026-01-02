import math,bisect
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
n,d,a = map(int,readline().split())
lst1 = [list(map(int,readline().split())) for i in range(n)]
lst1.sort()

#####segfunc######
def segfunc(x,y):
    return x+y

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
　　和のセグ木 → 0
　　積のセグ木 → 1
　　gcdのセグ木 → 0　(gcdを更新しない値は0)
"""
ide_ele = 0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num


#process
x = []
for i in lst1:
    x.append(i[0])


ans = 0

for i in range(n):
    k = bisect.bisect_left(x,lst1[i][0]-2*d) #手前側にあるダメージ量を確認

    r = query(k,i) #kからiまでの合計ダメージを取得

    if lst1[i][1] > r:
        if (lst1[i][1]-r)/a%1==0:
            need = (lst1[i][1]-r)//a
        else:
            need = (lst1[i][1]-r)//a+1
        ans += need
        update(i,need*a)

print(ans)

#ABC157-E Simple String Queries
"""
英小文字26字が含まれるか否かを、2**26のint型で管理するセグ木。
これをbitwise-segment treeと言うらしい。
解法：
葉はその英小文字のbitで管理する。
segfuncにはx|yを登録することで、区間クエリをとった時に
2進数表記で1が出てくる回数が答えになる。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

#input
n = int(readline())
s = readline().rstrip().decode('utf-8')
lst1 = [0]*n
kijun = ord("a")
for i in range(n):
    res = ord(s[i])-kijun
    lst1[i] = 1<<res #A:1,B:10,C:100,D:1000

#####segfunc######
def segfunc(x,y):
    return x|y

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
seg=[ide_ele]*2*num #単位元の配列(計算結果に影響を及ぼさない配列)を作成

init(lst1)

#query
q = int(readline())
for i in range(q):
    kind,a,b = readline().rstrip().decode('utf-8').split()

    if kind == "1": #a文字目をbに変更
        res = ord(b)-kijun
        update(int(a)-1,1<<res)

    else: #[a,b]の区間に含まれる文字の種類を出力
        ans = 0
        a,b = int(a)-1,int(b)-1
        res = query(a,b+1)
        for i in range(26):
            if res >> i &1:
                ans += 1
        print(ans)
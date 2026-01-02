
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, K = map(int,input().split())
P = list(map(int,input().split()))

# 点更新，区間クエリ
class SegTree:
    # n : 元の配列の長さ
    # init_list: 元の配列
    # segfunc : 載せる関数（演算）
    # ide_ele : segfuncの単位元
        
    def __init__(self, n, init_list ,segfunc, ide_ele):
        #　num : 2**num >= n となる最小の整数 （葉の数）
        # seg : segtreeのリスト
        self.num = 2**((n-1).bit_length())
        self.seg = [ide_ele]*(2*self.num)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        # 葉の要素をセット
        for i in range(n):
            self.seg[i+self.num-1] = init_list[i]        
        # segtreeの構築
        for i in range(self.num-2, -1, -1):
            self.seg[i] = segfunc(self.seg[2*i+1],self.seg[2*i+2])
        
        #memo: 要素iの子ノードは要素2*i+1, 2*i+2
        #    : 要素iの親ノードは要素(i-1)//2
        
    # 要素の更新 (init_list[k]=x)
    def update(self,k,x):
        k += self.num-1 #葉のノードのインデックス
        self.seg[k] = x
        #末端から頂点まで更新
        while k:
            k = (k-1)//2
            self.seg[k] = self.segfunc(self.seg[2*k+1], self.seg[2*k+2])
     
    # 区間クエリ （区間[l,r)に対する演算結果）
    def query(self, l,r):
        if r<=l:
            return self.ide_ele
        
        l += self.num-1 #葉のノードのインデックス
        r += self.num-2 #半開区間から閉区間へ
        ret = self.ide_ele
        
        while r-l>1:
            if l&1 == 0:
                ret = self.segfunc(ret,self.seg[l])
            
            if r&1 == 1:
                ret = self.segfunc(ret,self.seg[r])
                r -= 1
            # 親ノードへ遷移
            l = l//2
            r = (r-1)//2
        if r==l:
            ret = self.segfunc(ret, self.seg[r])
        else:
            ret = self.segfunc(ret, self.seg[l])
            ret = self.segfunc(ret, self.seg[r])
        
        return ret
            
def segfunc(x,y):
    return min(x,y)
def segfunc2(x,y):
    return max(x,y)

INF = 10**9
segtree = SegTree(N, P, segfunc, INF)
segtree_max = SegTree(N, P, segfunc2, 0)
from queue import Queue 

zouka = [1]
num = 1
for i in range(N-1):
    if P[i+1]>P[i]:
        num += 1
    else:
        num = 1
    zouka.append(num)


mini = INF
maxi = 0
q = Queue()
for p in P[:K]:
    mini = min(mini, p)
    maxi = max(maxi, p)
    q.put(p)

ans = 1
m = 0

if zouka[K-1]-zouka[0] == K-1:
    m += 1
    ans = 0

for i in range(1, N-K+1):
    remove = q.get()
    q.put(P[i+K-1])

    if zouka[i+K-1]-zouka[i] == K-1:
        m += 1
    elif P[i+K-1]>maxi and remove==mini:
        None
    else:
        ans += 1
    maxi = segtree_max.query(i, i+K)
    mini = segtree.query(i, i+K)


if m>=1:
    ans += 1

print(max(1,ans))

    

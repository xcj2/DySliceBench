


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
    return max(x,y)

N = int(input())
S = list(input())
Q = int(input())

alphalist = [[0]*N for _ in range(26)]
atmp = ord('a')
for i,s in enumerate(S):
    alphalist[ord(s)-atmp][i] = 1

seglist = [None]*26
for i in range(26):
    seglist[i] = SegTree(N,alphalist[i],segfunc,0)

ans = []
for i in range(Q):
    t,l,r = map(str,input().split())
    if t=='1':
        i = int(l)-1
        c = r
        
        org_idx = ord(S[i])-atmp
        seglist[org_idx].update(i,0)
        S[i] = c
        upt_idx = ord(c) - atmp
        seglist[upt_idx].update(i,1)
                
        
    else:
        l,r = int(l)-1,int(r)
        cnt = 0
        for i in range(26):
            cnt += seglist[i].query(l,r)
        ans.append(cnt)

for a in ans:
    print(a)










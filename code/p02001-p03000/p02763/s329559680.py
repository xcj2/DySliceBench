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

def segfunc2(x,y):
    return min(x,y)

def segfunc3(x,y):
    return x | y

def ctoi(c):
    return ord(c) - ord('a')

def main():
    N = int(input())
    S = list(input())
    Q = int(input())
    Segtree = [SegTree(N,[0] * N,segfunc,0) for _ in range(26)]
    for i, c in enumerate(S):
        Segtree[ctoi(c)].update(i,1)

    for _ in range(Q):
        q, *query = map(str, input().split())
        if q == '1':
            i, c = query
            i = int(i) - 1
            if c == S[i]:
                continue
            Segtree[ctoi(c)].update(i, 1)
            Segtree[ctoi(S[i])].update(i,0)
            S[i] = c
        else:
            l, r = query
            l = int(l) - 1
            r = int(r)
            ans = 0
            for j in range(26):
                if Segtree[j].query(l,r):
                    ans += 1
                    
            print(ans)



    


if __name__ == "__main__":
    main()
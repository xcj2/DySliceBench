class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """
    def __init__(self, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = ide_ele
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = i
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res

def main():
    import random
    from math import log,ceil

    N=int(input())
    n=N

    A=list(map(int,input().split()))
    A=[log(A[i],4) for i in range(N)]
    B=[A[-i-1] for i in range(N)]
    memo=[0]*(N-1)
    ans=10**25
    ope=[0 for i in range(N+1)]
    ope[N]=10**20

    def segfunc(x,y):
        if ope[x]>ope[y]:
            return y
        elif ope[y]>ope[x]:
            return x
        else:
            return min(x,y)
    #####ide_ele#####
    ide_ele = N
    #################


    for i in range(1,N):
        ope[i]=max(0,ceil(A[i-1]-A[i]))
        A[i]+=ope[i]

    rmq=SegTree(segfunc,ide_ele)

    S=sum(ope[i] for i in range(N))
    ans=min(ans,2*S)
    zero=[N]

    #A1 ... AnのBIT(1-indexed)
    BIT = [0]*(n+1)
    #A1 ~ Aiまでの和 O(logN)
    def BIT_query(idx):
        res_sum = 0
        while idx > 0:
            res_sum += BIT[idx]
            idx -= idx&(-idx)
        return res_sum

    #Ai += x O(logN)
    def BIT_update(idx,x):
        while idx <= n:
            BIT[idx] += x
            idx += idx&(-idx)
        return

    for i in range(1,N):
        while i!=zero[-1]:
            k=rmq.query(i,zero[-1])
            val=ope[k]+BIT_query(k+1)
            S-=val*(zero[-1]-i)
            BIT_update(i+1,-val)
            BIT_update(zero[-1]+1,val)
            zero.append(k)
        zero.pop()
        memo[i-1]+=2*S

    ope=[0 for i in range(N+1)]
    ope[N]=10**20
    S=0
    for i in range(1,N):
        ope[i]=max(0,ceil(B[i-1]-B[i]))
        S+=ope[i]
        B[i]+=ope[i]
    #print(time.time()-start)
    rmq=SegTree(segfunc,ide_ele)
    #print(time.time()-start)

    ans=min(ans,2*S+N)
    zero=[N]
    BIT=[0]*(n+1)

    for i in range(1,N):
        while i!=zero[-1]:
            k=rmq.query(i,zero[-1])
            val=ope[k]+BIT_query(k+1)
            S-=val*(zero[-1]-i)
            BIT_update(i+1,-val)
            BIT_update(zero[-1]+1,val)
            zero.append(k)
        zero.pop()
        memo[N-1-i]+=2*S+(N-i)
    #print(time.time()-start)
    test=min(memo)
    print(min(test,ans))

if __name__=="__main__":
    main()
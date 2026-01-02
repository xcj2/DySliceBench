def main():
    import sys
    input = sys.stdin.buffer.readline
    def I(): return int(input())
    
    readline = sys.stdin.readline
    readall = sys.stdin.read
    MI = lambda: map(int, readline().split())
    LI = lambda: list(map(int, readline().split()))
    
    class BIT:
        '''
        0-indexed
        '''
        def __init__(self, N):
            self.size = N
            self.tree = [0] * (N + 1)
            self.depth = N.bit_length()

        def _bitsum(self, i):
            ret = 0
            while i:
                ret += self.tree[i]
                i ^= i & -i
            return ret

        # [l,r)の和
        def bitsum(self, l, r=None):
            if r is None:
                return self._bitsum(l)
            else:
                return self._bitsum(r) - self._bitsum(l)

        # i番目にxを追加
        def add(self, i, x):
            i += 1
            while i <= self.size:
                self.tree[i] += x
                i += i & -i
            return

        def lower_bound(self, x):
            sum_ = 0
            pos = 0
            v = 1 << self.depth
            for i in range(self.depth, -1, -1):
                k = pos + v
                if k <= self.size and sum_ + self.tree[k] < x:
                    sum_ += self.tree[k]
                    pos += v
                v >>= 1
            return pos + 1, sum_

    
    N,Q=MI()
    C=LI()
    
    Query =[]
    
    M=10**6
    M2=10**12
    for i in range(Q):
        l, r = MI()
        l-=1
        r-=1
        Query.append(r*M2 + l*M + i)
    Query.sort()
    
    """
    事前処理 + クエリの高速処理
    or 
    クエリ先読み
    
    とりあえずrの昇順にクエリをソートしておく．
    結局，各色ごとに1つ前のやつがどこにあるかが問題=>各色ごとに最新の物だけを保持すれば良い．
    最終的にクエリに答えたいので，i番目が使えるかどうかBITで管理
    """
    bit=BIT(N+3)
    dd=[N+3]*(N+1)#多くとっておく
    
    ans=[0]*Q
    pre=-1
    for q in Query:
        r = q // 10 ** 12
        l = (q % 10 ** 12) // 10 ** 6
        i = q % 10 ** 6
        for j in range(pre+1,r+1):
            c=C[j]
            old=dd[c]#その色の古いやつ
            bit.add(old,-1)#もしまだ出てきていないなら，範囲外の使わないところを-1する
            #最新を追加
            dd[c]=j
            bit.add(j,1)
        pre=r
        ans[i]=bit.bitsum(l,r+1)
        
    for a in ans:
        print(a)
main()

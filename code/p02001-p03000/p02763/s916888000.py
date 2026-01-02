def main():
    n = int(input())
    s = input()
    m = int(input())
    abc = [input().split() for _ in [0]*m]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    class segtree():
        def __init__(self, base, ini):  # self,モノイド,元の配列
            # ini：上限（下限）,base：元の配列,monoid：モノイド,tree：セグ木,depth：treeの深さ,
            # basesize：baseの要素数,treesize：treeの要素数,num：treesize-basesize
            # 初期値（上限とか下限）を決定
            self.ini = ini
            # セグ木の要素数（num）および深さ（depth）を計算
            self.basesize = len(base)
            self.num, self.depth = 1, 1
            while self.num < self.basesize:
                self.num *= 2
                self.depth += 1
            self.num -= 1
            # 関数（モノイド、今回はmin）を設定
            self.monoid = lambda x, y: x | y
            # セグ木を構築
            self.treesize = self.num*2+1
            self.tree = [None]*self.treesize
            # segtree[m]以降に代入したい配列を入力していく
            for i in range(self.num, self.num+self.basesize):
                self.tree[i] = base[i-self.num]
            for i in range(self.num+self.basesize, self.treesize):
                self.tree[i] = ini
            # segtree[m]以降の情報を使って、0に向かってセグ木を構築していく
            for i in range(self.num-1, -1, -1):
                self.tree[i] = self.monoid(self.tree[2*i+1], self.tree[2*i+2])

        # 条件を満たす(サンプルの条件はs以下になること)最大のインデックスを返す関数
        def max_index(self, index_func):
            # 探していく
            i = 0
            while i < self.num:
                k = 2*i+1
                if index_func(self.tree[k+1]):
                    i = k+1
                    continue
                if index_func(self.tree[k]):
                    i = k
                    continue
                return -1
            return i-self.num

        # 条件を満たす(サンプルの条件はs以下になること)最小のインデックスを返す関数
        def min_index(self, index_func):
            # 探していく
            i = 0
            while i < self.num:
                k = 2*i+1
                if index_func(self.tree[k]):
                    i = k
                    continue
                if index_func(self.tree[k+1]):
                    i = k+1
                    continue
                return -1
            return i-self.num

        # 半開区間[lower,upper)の最小値（とか）を探す関数
        def search(self, lower, upper):
            # 返り値を初期化
            ret = self.ini
            l = lower+self.num
            r = upper+self.num
            while l < r:
                if r % 2 == 0:
                    r -= 1
                    ret = self.monoid(ret, self.tree[r])
                if l % 2 == 0:
                    ret = self.monoid(ret, self.tree[l])
                    l += 1
                l //= 2
                r //= 2
            return ret

        # base[i]をsに更新したときにセグ木全体を更新する関数
        def update(self, index, new_value):
            i = index+self.num
            self.tree[i] = new_value
            while i != 0:
                i = (i-1)//2
                temp = self.monoid(self.tree[2*i+1], self.tree[2*i+2])
                if self.tree[i] != temp:
                    self.tree[i] = temp
                    continue
                break

    d = {alphabet[i]: i for i in range(26)}
    seg = segtree([2**d[s[i]] for i in range(n)], 0)

    for a, b, c in abc:
        if a == "1":
            b = int(b)
            seg.update(b-1, 2**d[c])
        else:
            b, c = int(b), int(c)
            print(bin(seg.search(b-1, c)).count("1"))


main()
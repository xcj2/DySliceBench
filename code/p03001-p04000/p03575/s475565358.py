'''
https://atcoder.jp/contests/abc075/tasks/abc075_c?lang=ja
深さ優先探索でも解ける
'''
def main():
    import sys
    #input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter

    #mod = 1000000007

    class UnionFind():
        #n個の要素を番号0~n-1で管理する
        #parents:要素の親(1つ上), 要素が根の場合サイズを表す
        def __init__(self, n):
            self.n = n
            self.parents = [-1] * n
    
        #要素xの根を返す, その過程で経路圧縮も行う
        def find(self, x):
            if self.parents[x] < 0:
                return x
            else:
                self.parents[x] = self.find(self.parents[x])
                return self.parents[x]
    
        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
            if x == y:
                return
            #それぞれのsizeで比べる
            if self.parents[x] > self.parents[y]:
                x, y = y, x
            self.parents[x] += self.parents[y]
            self.parents[y] = x #根をくっつける(片方を親にする)
    
        #xが属するグループのsize
        def size(self, x):
            return -self.parents[self.find(x)]
    
        #xとyが同じグループかどうか
        def same(self, x, y):
            return self.find(x) == self.find(y)
    
        #xが属するグループの要素全てを返す
        def members(self, x):
            root = self.find(x)
            return [i for i in range(self.n) if self.find(i) == root]
    
        #全ての根の要素を返す
        def roots(self):
            return [i for i, x in enumerate(self.parents) if x < 0]
    
        #各グループの要素を辞書で返す
        def all_group_members(self):
            return {r: self.members(r) for r in self.roots()}
    
        #print(uf)
        def __str__(self):
            return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    n,m = map(int, input().split())
    edge = [list(map(int, input().split())) for _ in range(m)]
    res = 0
    for i in range(m):
        uf = UnionFind(n)
        for j in range(m):
            if i==j:
                continue
            a,b = edge[j]
            uf.union(a-1,b-1)
        if uf.size(0)!=n:
            res += 1
    print(res)

if __name__ == '__main__':
    main()
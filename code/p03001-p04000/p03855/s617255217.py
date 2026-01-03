def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations
    #from itertools import accumulate, product
    from bisect import bisect_left,bisect_right
    from math import floor, ceil
    #from operator import itemgetter

    #mod = 1000000007

    N,K,L = map(int, input().split())
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
        
    douro = UnionFind(N+1)
    tetudou = UnionFind(N+1)
    for _ in range(K):
        p,q = map(int, input().split())
        douro.union(p,q)
    for _ in range(L):
        r,s = map(int, input().split())
        tetudou.union(r,s)
    dic = {}
    parlis = []
    for i in range(1, N+1):
        p1 = douro.find(i)
        p2 = tetudou.find(i)
        parlis.append((p1,p2))
        if (p1,p2) in dic:
            dic[(p1,p2)] += 1
        else: 
            dic[(p1,p2)] = 1
    print(' '.join([str(dic[parlis[i]]) for i in range(N)]))


if __name__ == '__main__':
    main()
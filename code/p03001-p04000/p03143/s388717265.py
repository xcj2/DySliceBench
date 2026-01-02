def main():
    from sys import stdin
    input = stdin.readline
    import heapq
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    aby = [list(map(int, input().split())) for _ in [0]*m]
    aby = [(a-1, b-1, y) for a, b, y in aby]
    tree1 = [sum(x)]
    tree2 = [0]*n

    def Kruskal(n, abc):
        class unionfind():
            # size:要素数,tree：unionfind木
            def __init__(self, size):  # self,要素数
                self.size = size
                self.tree_root = list(range(self.size))
                self.tree_depth = [1]*self.size

            # rootを探す
            def root(self, index):
                temp_list = []
                temp = self.tree_root[index]
                while index != temp:
                    temp_list.append(index)
                    index = temp
                    temp = self.tree_root[index]
                for i in temp_list:
                    self.tree_root[i] = index
                return index

            # 結合
            def unite(self, index1, index2):
                r1 = self.root(index1)
                r2 = self.root(index2)
                if r1 != r2:
                    d1, d2 = self.tree_depth[r1], self.tree_depth[r2]
                    if d1 <= d2:
                        self.tree_root[r1] = r2
                        self.tree_depth[r2] = max(d1+1, d2)
                    else:
                        self.tree_root[r2] = r1
                        self.tree_depth[r1] = max(d2+1, d1)

            # 同じか判定
            def same(self, index1, index2):
                r1 = self.root(index1)
                r2 = self.root(index2)
                return r1 == r2

        uf = unionfind(n)
        ret = []
        abc.sort(key=lambda x: x[2])
        for a, b, c in abc:
            if not uf.same(a, b):
                ret.append((a, b, c))
                uf.unite(a, b)
        return ret

    def dfs(a, b):
        g[a].remove(b)
        g[b].remove(a)
        tree_a, tree_b, q_a, q_b, sum_a, sum_b = {a}, {b}, [a], [b], x[a], x[b]
        while True:
            flag = False
            while q_a:
                i = q_a[-1]
                for j in g[i]:
                    if j not in tree_a:
                        q_a.append(j)
                        tree_a.add(j)
                        sum_a += x[j]
                        flag = True
                        break
                if flag:
                    break
                else:
                    q_a.pop()
            if not q_a:
                l = len(tree1)
                for i in tree_a:
                    tree2[i] = l
                tree1.append(sum_a)
                tree1[tree2[b]] -= sum_a
                return
            flag = False
            while q_b:
                i = q_b[-1]
                for j in g[i]:
                    if j not in tree_b:
                        q_b.append(j)
                        tree_b.add(j)
                        sum_b += x[j]
                        flag = True
                        break
                if flag:
                    break
                else:
                    q_b.pop()
            if not q_b:
                l = len(tree1)
                for i in tree_b:
                    tree2[i] = l
                tree1.append(sum_b)
                tree1[tree2[a]] -= sum_b
                return

    min_tree = Kruskal(n, aby)

    g = [set() for _ in [0]*n]
    [g[a].add(b) for a, b, y in min_tree]
    [g[b].add(a) for a, b, y in min_tree]

    h = [(-y, a, b) for a, b, y in min_tree]
    heapq.heapify(h)

    ans = len(min_tree)

    while h:
        y, a, b = heapq.heappop(h)
        y *= -1
        if y > tree1[tree2[a]]:
            dfs(a, b)
            ans -= 1

    for a, b, y in set(aby)-set(min_tree):
        if tree2[a] == tree2[b]:
            ans += y <= tree1[tree2[a]]

    print(m-ans)


main()

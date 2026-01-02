class UnionFind:
    # 負の値はルートで集合の個数
    # 正の値は次の要素を返す
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    # 集合の代表を求める
    def find(self, x):
        while self.table[x] >= 0:
            # 根に来た時,self.table[根のindex]は負の値なのでx = 根のindexで値が返される。
            x = self.table[x]
        return x

    # 併合
    def union(self, x, y):
        s1 = self.find(x)  # 根のindex,table[s1]がグラフの高さ
        s2 = self.find(y)
        if s1 != s2:  # 根が異なる場合
            if self.table[s1] != self.table[s2]:  # グラフの高さが異なる場合
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                else:
                    self.table[s1] = s2
            else:
                # グラフの長さが同じ場合,どちらを根にしても変わらない
                # その際,グラフが1長くなることを考慮する
                self.table[s1] += -1
                self.table[s2] = s1
        return


def func(n, m, p, x):
    union = UnionFind(n + 1)
    for _x in x:
        union.union(p[_x[0]], p[_x[1]])
    count = 0
    for i in range(n):
        if union.find(i + 1) == union.find(p[i]):
            count += 1
            # print("{}:{}".format(i, union.find(i)))
            # 所属しているunionの根の値を出力する
    # print([union.find(i) for i in range(n+1)])
    return str(count)


n, m = [int(i) for i in input().split()]
p = [int(i) for i in input().split()]
x = [[0, 0] for _ in range(m)]
for i in range(m):
    x[i] = [int(i) - 1 for i in input().split()]
print(func(n, m, p, x))
"""
print(str(2) + " vs " + func(5, 2, [5, 3, 1, 4, 2], [[0, 2], [4, 3]]))
print(str(3) + " vs " + func(3, 2, [3, 2, 1], [[0, 1], [1, 2]]))
print(str(8) + " vs " + func(10, 8, [5, 3, 6, 8, 7, 10, 9, 1, 2, 4],
                             [[2, 0], [3, 0], [4, 8], [1, 4], [5, 4], [2, 4], [7, 8], [6, 8]]))
print(str(5) + " vs " + func(5, 1, [1, 2, 3, 4, 5], [[0, 4]]))
# print("print(func({}, {}, {}, {}))".format(n, m, p, x))
"""

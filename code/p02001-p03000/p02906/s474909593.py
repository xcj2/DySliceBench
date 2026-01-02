#!/usr/bin/env python3
n, m, q = [int(item) for item in input().split()]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    def get_size(self, x):
        return self.size[self.find(x)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    
Forest = UnionFind(n)
circles = []
group_num = n
edge_num = 0
seen = set()
for i in range(q):
    a, b, c = [int(item) for item in input().split()]
    if a > b:
        a, b = b, a
    if (a, b, c) in seen:
        continue
    if c == 0:
        # loop with simple path
        if not Forest.same_check(a, b):
            Forest.union(a, b)
            group_num -= 1
            edge_num += 1
    else:
        circles.append((a, b, c))
    seen.add((a, b, c))

for a, b, c in circles:
    # multipath in tree
    if Forest.same_check(a, b):
        print("No")
        exit()
    # if group_num == 2:
    #     print("No")
    #     exit()

if len(circles) > 0:
    edge_min = edge_num + group_num
    edge_max = edge_num + group_num * (group_num - 1) // 2
else:
    edge_min = edge_num + group_num - 1
    edge_max = edge_num + group_num * (group_num - 1) // 2

if edge_min <= m <= edge_max:
    print("Yes")
else:
    print("No")
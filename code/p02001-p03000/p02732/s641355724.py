# -*- coding: utf-8 -*-
import math

def combination2(n, r):
    if n <= 1:
        return 0
    return math.factorial(n) / (math.factorial(r) * math.factorial(n-r))

def combination(n, r):
    # X = n * n-1 * ... * max(r, n - r)+1
    # Y = min(r, n - r)!
    # nCr = X / Y
    if n <= 1:
        return 0

    X = 1
    for i in range(n, max(r, n - r), -1):
        X *= i
    
    if n - r <= 0:
        return X

    Y = math.factorial(min(r, n - r))

    return X / Y

class UnionFindTree():
    def __init__(self, n):
        self.parent = [] # 親のノード
        self.rank = [] # 木の深さ
        self.number = [] # グループの要素数
        for i in range(n):
            self.parent.append(i)
            self.rank.append(0)
            self.number.append(1)

    # 根ノードを取得
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    # 併合
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.number[y] += self.number[x]
        else:
            self.parent[y] = x
            self.number[x] += self.number[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じノードか判別
    def same(self, x, y):
        return self.find(x) == self.find(y)

    # グループのノード数を取得
    def member_number(self, x):
        x = self.find(x)
        return self.number[x]

N = int(input())
A = [int(i) for i in input().split()]

uft = UnionFindTree(N)

vals = {}
for i in range(N):
    if A[i] in vals:
        uft.unite(vals[A[i]], i)
    else:
        vals[A[i]] = i

comb = {}
group_numbers = {}
total = 0
comb_memo = {}
for k, v in vals.items():
    group_number = uft.member_number(v)
    if group_number not in comb_memo:
        comb_memo[group_number] = combination(group_number, 2)
    comb[k] = comb_memo[group_number]

    group_numbers[k] = group_number
    total += comb[k]

ans = {}
for k, v in vals.items():
    if group_numbers[k] - 1 not in comb_memo:
        comb_memo[group_numbers[k] - 1] = combination(group_numbers[k] - 1, 2)
    ans[k] = int(total - comb[k] + comb_memo[group_numbers[k] - 1])

for a in A:
    print(ans[a])
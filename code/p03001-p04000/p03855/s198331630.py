import sys
fin = sys.stdin.readline
from collections import defaultdict

class UnionFind(object):
    def __init__(self, N):
        self.__root = list(range(N))
    

    def root(self, x):
        if self.__root[x] == x:
            return x
        else:
            # root abbreviation
            self.__root[x] = self.root(self.__root[x])
            return self.__root[x]

    
    def same(self, x, y):
        return self.root(x) == self.root(y)


    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if (x == y):
            return
        self.__root[x] = y
        return


N, K, L = [int(elem) for elem in fin().split(' ')]
road_list = tuple([tuple([int(elem)-1 for elem in fin().split(' ')]) for _ in range(K)])
train_list = tuple([tuple([int(elem)-1 for elem in fin().split(' ')]) for _ in range(L)])

uf_road = UnionFind(N)
uf_train = UnionFind(N)

for p, q in road_list:
    uf_road.unite(p, q)

for r, s in train_list:
    uf_train.unite(r, s)


key_list = []
count = defaultdict(int)
for i in range(N):
    # logN
    key = (uf_road.root(i), uf_train.root(i))
    key_list.append(key)
    count[key] += 1

assert len(key_list) == N
answer_list = [0] * N
for i, key in enumerate(key_list):
    answer_list[i] = str(count[key])
print(' '.join(answer_list))

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

debug = True
#debug = False

def dprint(*objects):
    if debug == True:
        print(*objects)

class UnionFind:

    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def merge(self, i, j):
        rooti = self.findroot(i)
        rootj = self.findroot(j)
        self.parents[rooti] = rootj

    def issame(self, i, j):
        rooti = self.findroot(i)
        rootj = self.findroot(j)
        return rooti == rootj

    def findroot(self, i, followed_indices=None):

        if i == self.parents[i]:
            return i
        else:
            root = self.findroot(self.parents[i])
            self.parents[i] = root # 経路圧縮
            return root
    pass

def solve():
    # np.set_printoptions(suppress=True)
    # n = int(input())
    n, k, l = map(int, input().split())
    uf1 = UnionFind(n)
    uf2 = UnionFind(n)

    for ki in range(k):
        p, q = map(int, input().split())
        uf1.merge(p-1, q-1)

    for li in range(l):
        p, q = map(int, input().split())
        uf2.merge(p-1, q-1)

    ans = {}
    key_list = []
    for i in range(n):
        root1 = uf1.findroot(i)
        root2 = uf2.findroot(i)

        key = str(root1) + "_" + str(root2)
        key_list.append(key)

        if key in ans.keys():
            ans[key] += 1
        else:
            ans[key] = 1

    for i in range(n):
        print(ans[key_list[i]], end=' ')

solve()
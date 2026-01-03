from collections import defaultdict
def main():
    N, M = [int(i) for i in input().split()]
    L = [[] for _ in range(M+1)]
    for i in range(N):
        for j in map(int, input().split()[1:]):
            L[j].append(i)
    uf = UnionFind()
    for i, l in enumerate(L):
        #print("Lang {}".format(i))
        if not l:
            continue
        a = l[0]
        for b in l[1:]:
            #print(a, b)
            uf.union(a, b)
    # print(uf.table)
    print("YES" if uf.size(0) == N else "NO")
    

class UnionFind(object):

    def __init__(self):
        self.table = defaultdict(lambda: -1)

    def find(self, x):
        if self.table[x] < 0:
            return x
        self.table[x] = self.find(self.table[x])
        return self.table[x]

    def size(self, x):
        return -self.table[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 == s2:
            return False
        if self.table[s1] > self.table[s2]:
            s1, s2 = s2, s1
        self.table[s1] += self.table[s2]
        self.table[s2] = s1
        return True

if __name__ == "__main__":
    main()

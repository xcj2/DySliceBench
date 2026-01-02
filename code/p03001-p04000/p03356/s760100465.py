import sys
def input(): return sys.stdin.readline().rstrip()

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * (n + 1)

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

        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)
    
def main():
    N, M = map(int, input().split())
    P = tuple(map(int, input().split()))
    un = UnionFind(N)
    for _ in range(M):
        x, y = map(int, input().split())
        un.union(x, y)
    ans = 0
    for i, p in enumerate(P):
        if un.same(i + 1, p):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()

import sys
def main():
    input = sys.stdin.readline
    N,M=map(int, input().split())
    *P,=map(int, input().split())
    P=[0]+P
    uf=UnionFindTree(N+1)
    for _ in range(M):
        x,y=map(int, input().split())
        uf.union(x,y)
    ans=0
    for i in range(1,N+1):
        if uf.same(i,P[i]): ans+=1
    print(ans)

class UnionFindTree:
    def __init__(self, n):
        self.parent = [-1] * n

    def find(self, x):
        p = self.parent
        while p[x] >= 0: x, p[x] = p[x], p[p[x]]
        return x

    def union(self, x, y):
        x, y, p = self.find(x), self.find(y), self.parent
        if x == y: return False
        if p[x] > p[y]: x, y = y, x
        p[x], p[y] = p[x] + p[y], x
        return True

    def same(self, x, y): return self.find(x) == self.find(y)
    def size(self, x): return -self.parent[self.find(x)]

if __name__ == '__main__':
    main()
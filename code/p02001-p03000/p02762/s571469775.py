import sys
input = sys.stdin.readline

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.group = [set() for _ in range(n)]

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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        if not self.group[root]:
            for i in range(self.n):
                if self.find(i) == root:
                    self.group[root].add(i)
        return self.group[root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

def main():
    N, M, K = map(int, input().split())
    uni = UnionFind(N)
    not_cand = [0] * N
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        not_cand[A] += 1
        not_cand[B] += 1
        uni.union(A,B)
 
    for _ in range(K):
        C, D = map(int, input().split())
        C -= 1
        D -= 1
        if uni.same(C,D):
            not_cand[C] += 1
            not_cand[D] += 1
            
    
    ans = [0] * N
    for i in range(N):
        ans[i] = uni.size(i) - not_cand[i] - 1
    
    print(*ans)
 
 
if __name__ == "__main__":
    main()

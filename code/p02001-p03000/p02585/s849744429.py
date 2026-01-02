import sys
sys.setrecursionlimit(10 ** 7)

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
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
        return [i for i in range(self.n) if self.find(i) == root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    uf = UnionFind(n)
    for i in range(n):
        uf.union(i, p[i]-1)
    G = [[] for _ in range(uf.group_count())]
    idx = 0
    st = set()
    for i in range(n):
        if not i in st:
            x = i
            while not x in st:
                G[idx].append(c[x])
                st.add(x)
                x = p[x] - 1
            idx += 1
    ans = max(c) #1回動かした時の最大
    for i in range(len(G)):
        sum_g = sum(G[i])
        tmp_k = k
        if sum_g > 0:
            tmp = sum_g * (tmp_k // len(G[i]))
            tmp_k %= len(G[i])
            csum = [0]
            for v in G[i]:
                csum.append(v)
            for v in G[i]:
                csum.append(v)
            for j in range(len(csum)-1):
                csum[j+1] += csum[j]
            tmp_tmp = 0
            for j in range(len(G[i])+1):
                for l in range(1, tmp_k+1):
                    if tmp_tmp < csum[j+l] - csum[j]:
                        tmp_tmp = csum[j+l] - csum[j]
            if 0 < tmp_tmp:
                tmp += tmp_tmp
            if ans < tmp:
                ans = tmp
            if k > len(G[i]):
                tmp_k = k
                tmp = sum_g * ((tmp_k // len(G[i]))-1)
                tmp_k = len(G[i])
                csum = [0]
                for v in G[i]:
                    csum.append(v)
                for v in G[i]:
                    csum.append(v)
                for j in range(len(csum)-1):
                    csum[j+1] += csum[j]
                tmp_tmp = 0
                for j in range(len(G[i])+1):
                    for l in range(1, tmp_k+1):
                        if tmp_tmp < csum[j+l] - csum[j]:
                            tmp_tmp = csum[j+l] - csum[j]
                if 0 < tmp_tmp:
                    tmp += tmp_tmp
                if ans < tmp:
                    ans = tmp
        else:
            if tmp_k > len(G[i]):
                tmp_k = len(G[i])
            csum = [0]
            for v in G[i]:
                csum.append(v)
            for v in G[i]:
                csum.append(v)
            for j in range(len(csum)-1):
                csum[j+1] += csum[j]
            for j in range(len(G[i])):
                for l in range(1, tmp_k+1):
                    if ans < csum[j+l] - csum[j]:
                        ans = csum[j+l] - csum[j]
    print(ans)

if __name__ == "__main__":
    main()
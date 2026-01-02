class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x

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

    def size(self, x):
        return -self.parents[self.find(x)]

def solve(uf, except_list):
    ret = [0]
    for i in range(1, N + 1):
        ret.append(uf.size(i) - 1 - len(except_list[i]))
    return ret

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    except_list = [[] for _ in range(N + 1)]
    uf = UnionFind(N + 1)

    for _ in range(M):
        a, b = map(int, input().split())
        except_list[a].append(b)
        except_list[b].append(a)
        uf.union(a, b)

    for _ in range(K):
        c, d = map(int, input().split())
        if not uf.same(c, d):
            continue
        except_list[c].append(d)
        except_list[d].append(c)

    for ans in solve(uf, except_list)[1:]:
        print(ans, end=' ')
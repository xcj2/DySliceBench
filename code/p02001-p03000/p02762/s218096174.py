import collections

def Z(): return int(input())
def ZZ(): return [int(_) for _ in input().split()]

def main():
    N, M, K = ZZ()
    F = [0] * (N+1)
    output = []

    par = [i for i in range(N+1)]
    rank = [0] * (N+1)

    # 要素xの親ノードを返す
    def find(x):
        if par[x] == x:
            return x
        par[x] = find(par[x])
        return par[x]

    # 要素x, yの属する集合を併合
    def unite(x, y):
        x, y = find(x), find(y)
        if x == y:
            return
        if rank[x] < rank[y]:
            par[x] = y
        else:
            par[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
        return

    # xとyが同じ集合に属するか？
    def same(x, y):
        return find(x) == find(y)

    for _ in range(M):
        a, b = ZZ()
        F[a] += 1
        F[b] += 1
        unite(a, b)

    for i in range(1, N+1): find(i)
    cnt = collections.Counter(par)

    for _ in range(K):
        c, d = ZZ()
        if same(c, d):
            F[c] += 1
            F[d] += 1
    for i in range(1, N+1):
        cc = cnt[par[i]] - F[i] - 1
        output.append(cc)

    print(*output)

    return

if __name__ == '__main__':
    main()

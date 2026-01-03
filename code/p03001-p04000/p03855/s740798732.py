from collections import defaultdict

def find(x, parent):
    if parent[x] == x:
        return x
    else:
        # keyとvalueが同じ位置に当たるまで親をたどる
        parent[x] = find(parent[x], parent)
        return parent[x]

# 併合
def unite(x, y, parent):
    x = find(x, parent)
    y = find(y, parent)
    if x == y: return

    parent[y] = x

def solve():
    N, K, L = map(int, input().split())
    
    street = [i for i in range(N)]
    train = [i for i in range(N)]

    for _ in range(K):
        a, b = map(int, input().split())
        unite(a-1, b-1, street)

    for _ in range(L):
        a, b = map(int, input().split())
        unite(a-1, b-1, train)

    d = defaultdict(int)
    for i in range(N):
        a = find(street[i], street)
        b = find(train[i], train)
        d[(a, b)] += 1

    ans = []
    for i in range(N):
        a = find(street[i], street)
        b = find(train[i], train)
        ans.append(str(d[(a, b)]))

    print(' '.join(ans))

solve()
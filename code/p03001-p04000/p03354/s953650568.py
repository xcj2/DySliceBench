def main():
    p = [0] + list(map(int, input().split()))
    cnt = 0
    for _ in range(m):
        x, y = map(int, input().split())
        unite(x, y)
    for i in range(1, n+1):
        if same(i, p[i]):
            cnt += 1
    print(cnt)

def root(x):
    if par[x] == x:
        return x
    par[x] = root(par[x])
    return par[x]

def unite(x, y):
    root_x = root(x)
    if root_x != root(y):
        par[root_x] = y

def same(x, y):
    return root(x) == root(y)

if __name__ == "__main__":
    n, m = map(int, input().split())
    par = list(range(n+1))
    main()
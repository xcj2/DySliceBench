def main():
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

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    if x != root(y):
        par[x] = y

if __name__ == "__main__":
    n, m = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    par = list(range(n+1))
    main()

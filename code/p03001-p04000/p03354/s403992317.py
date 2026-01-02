def main():
    n, m = map(int, input().split())
    p = [0] + list(map(int, input().split()))
    cnt = 0
    global parent
    parent = list(range(n+1))
    for _ in range(m):
        x, y = map(int, input().split())
        unite(x, y)
    for i in range(1, n+1):
        cnt += (root(i) == root(p[i]))
    print(cnt)

def root(x):
    if parent[x] == x:
        return x
    parent[x] = root(parent[x])
    return parent[x]

def unite(x, y):
    root_x = root(x)
    if root_x != root(y):
        parent[root_x] = y

if __name__ == "__main__":
    main()
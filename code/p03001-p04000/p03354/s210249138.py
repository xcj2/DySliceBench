def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    global parent, rank
    parent = list(range(n+1))
    rank = [0]*(n+1)
    cnt = 0
    for _ in range(m):
        x, y = map(int, input().split())
        unite(x, y)
    for i, pi in enumerate(p, 1):
        if same(i, pi):
            cnt += 1
    print(cnt)
        
def root(x):
    if parent[x] == x:
        return x
    parent[x] = root(parent[x])
    return parent[x]

def same(x, y):
    return root(x) == root(y)

def unite(x, y):
    x = root(x)
    y = root(y)
    if x != y:
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

if __name__ == "__main__":
    main()

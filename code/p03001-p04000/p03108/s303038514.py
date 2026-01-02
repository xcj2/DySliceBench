import sys
input = sys.stdin.readline

def readlines(n):
    for _ in range(n):
        a, b = map(int, input().split())
        yield a, b

n, m = map(int, input().split())
bridges = list(readlines(m))
tree = list(range(n+1))
rank = [1] * (n+1)

def root(v):
    while tree[v] != v:
        tree[v] = tree[tree[v]]
        v = tree[v]
    return v

def merge(x, y):
    if rank[x] < rank[y]:
        tree[x] = y
        rank[y] += rank[x]
    else:
        tree[y] = x
        rank[x] += rank[y]

def main():
    fuben = n*(n-1)//2

    for a, b in bridges[::-1]:
        x = root(a)
        y = root(b)

        if x == y:
            yield str(fuben)
            continue
        
        yield str(fuben)
        fuben -= rank[x]*rank[y]
        merge(x, y)


print("\n".join(reversed(list(main()))))
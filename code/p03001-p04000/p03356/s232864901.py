import sys
sys.setrecursionlimit(100010)

def main():
    def input():
        return sys.stdin.readline()[:-1]

    N, M = map(int,input().split())

    p = list(map(lambda x: int(x)-1, input().split()))
    parent = [k for k in range(N)]

    def find(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = find(parent[x])
            return find(parent[x])

    def unite(x,y):
        parent[find(x)] = find(y)

    for k in range(M):
        x, y = map(int,input().split())
        unite(x-1,y-1)

    ans = 0
    for k in range(N):
        if find(k) == find(p[k]):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()

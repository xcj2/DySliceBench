def main():
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    for i in range(N):
        p[i] -= 1
    x = [0 for _ in range(M)]
    y = [0 for _ in range(M)]
    for i in range(M):
        x[i], y[i] = map(int, input().split())
        x[i] -= 1
        y[i] -= 1

    def root(x):
        if Parent[x]==x:
            return x
        else:
            Parent[x] = root(Parent[x])
            return Parent[x]

    def unite(x,y):
        x = root(x)
        y = root(y)
        if x!=y:
            Parent[x] = y

    Parent = [i for i in range(N)]
    for i in range(M):
        unite(x[i], y[i])

    count = 0
    for i in range(N):
        if root(i)==root(p[i]):
            count += 1

    return count

if __name__ == '__main__':
    print(main())

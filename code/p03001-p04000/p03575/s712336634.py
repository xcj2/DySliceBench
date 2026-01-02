N, M = map(int, input().split())
E = []
for _ in range(M):
    a, b = map(int, input().split())
    E.append((a, b))

E = sorted(E)

P = -1

def unionFind(E):
    parent = [i for i in range(N+1)]
    def root(a):
        p = a
        while parent[p] != p:
            p = parent[p]
        parent[a] = p
        return p
        
    for a, b in E:
        pa = root(a)
        pb = root(b)
        if pa < pb:
            parent[pb] = pa
        elif pa > pb:
            parent[pa] = pb

    for i in range(1, N+1):
        root(i)
    return max(parent)

def main():
    bridge = 0
    if M == 1:
        print(1)
    else:
        for i in range(0, M):
            if unionFind(E[:i]+E[i+1:]) != 1:
                bridge += 1
        print(bridge)
main()

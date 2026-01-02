import sys

sys.setrecursionlimit(10**5)

def main():
    N, M, K = map(int, input().split())
    parent = [n for n in range(0, N+1)]
    depth  = [1 for _ in range(0, N+1)] 
    blocks = [[] for _ in range(0, N+1)]
    friends = [[] for _ in range(0, N+1)]

    def root(x):
        p = parent[x]
        if p == x:
            return x
        p = root(p)
        parent[x] = p
        return p

    def union(a, b):
        pa = root(a)
        pb = root(b)
        if pa == pb:
            return
        if depth[pa] > depth[pb]:
            parent[pb] = pa
            depth[pa] += depth[pb]
        elif depth[pa] < depth[pb]:
            parent[pa] = pb
            depth[pb] += depth[pa]
        else:
            parent[pa] = pb
            depth[pb] *= 2
        #print((a, b), pa, pb, root(a), depth[2])

    for i in range(M):
        A, B = map(int, input().split())
        friends[A].append(B)
        friends[B].append(A)
        union(A, B)

    for i in range(K):
        C, D = map(int, input().split())
        blocks[C].append(D)
        blocks[D].append(C)
    if 0==1:
        print("index :", *range(1,N+1))
        print("parent:", *parent[1:])
        print("depth :", *[depth[root(x)] for x in range(1,N+1)])
        for n in range(1, N+1):
            p = root(n)
            c = depth[p]-1
            print(c, end=" ")
        print()

    for n in range(1, N+1):
        p = root(n)
        c = depth[p]-1
        for f in friends[n]:
            if root(f) == p:
                c-=1
        for b in blocks[n]:
            if root(b) == p:
                c-=1
        print(c, end=" ")
    print()

main() 

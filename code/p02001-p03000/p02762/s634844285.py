def root(parents, i):
    depth = 0
    while parents[i] != i:
        i = parents[i]
        depth += 1

    return i, depth

def isSame(parents, a, b):
    return root(parents,a)[0] == root(parents, b)[0]

def union(parents, size, a, b):
    pa, deptha = root(parents, a)
    pb, depthb = root(parents, b)
    if pa == pb: # already same group
        return
    if deptha < depthb:
        parents[pa] = pb
        size[pb] += size[pa]
    else:
        parents[pb] = pa
        size[pa] += size[pb]

def resolve():
    N, M, K = list(map(int, input().split()))
    parents = [i for i in range(N)]
    size = [1] * N
    ans = [0] * N

    for i in range(M):
        A, B = list(map(int, input().split()))
        ans[A-1] += 1
        ans[B-1] += 1
        union(parents, size, A-1, B-1)

    for i in range(N):
        pi = root(parents, i)[0]
        ans[i] = size[pi] - ans[i] -1 # eliminate friend count from candidate

    for i in range(K):
        A, B = list(map(int, input().split()))
        if isSame(parents, A-1, B-1):
            ans[A-1] -= 1
            ans[B-1] -= 1

    print(" ".join(map(str, ans)))

resolve()
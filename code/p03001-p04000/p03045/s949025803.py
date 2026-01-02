def main():

    N, M = map(int, input().split())
    parent = [i for i in range(N)]
    level = [1 for _ in range(N)]

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        pi, pj = find(i), find(j)
        if pi != pj:
            if level[pi] < level[pj]:
                parent[pi] = pj
                level[pj] = max(1+level[pi], level[pj])
            else:
                parent[pj] = pi
                level[pi] = max(1+level[pj], level[pi])

    for _ in range(M):
        i, j, z = map(int, input().split())
        union(i-1, j-1)

    # print(parent)
    for i in range(N): find(i)
    # print(parent)

    ans = len(set(parent))
    return ans

if __name__ == '__main__':
    print(main())
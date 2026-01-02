def ABC075C_dfs(targ, root, graph, now):

    for dst in graph[now]:
        if targ == sorted([dst, now]):
            continue
        if dst not in root:
            root.append(dst)
            ABC075C_dfs(targ, root, graph, dst)


def ABC075C_Bridge():
    N, M = map(int, input().strip().split())
    graph = [[] for i in range(N)]

    if N > M:
        print(M)
        return 0
    
    edge = [[] for i in range(M)]
    for i in range(M):
        a1, b1 = map(int, input().strip().split())
        a1 -= 1
        b1 -= 1
        graph[a1].append(b1)
        graph[b1].append(a1)
        edge[i] = sorted([a1, b1])

    ans = 0
    for ed in edge:
        root = [0]
        ABC075C_dfs(ed, root, graph, 0)
        if len(root) != N:
            ans += 1

    print(ans)

def main():
    ABC075C_Bridge()

if __name__ == "__main__":
    main()

from collections import defaultdict


def read_int():
    return int(input().strip())


def read_ints():
    return list(map(int, input().strip().split(' ')))


def solve():
    N, M = read_ints()
    G = defaultdict(list)
    for _ in range(M):
        a, b = read_ints()
        G[a].append(b)
        G[b].append(a)

    def dfs(node, visited):
        if len(visited) == N:
            return 1
        answer = 0
        for child in G[node]:
            if child not in visited:
                visited.add(child)
                answer += dfs(child, visited)
                visited.discard(child)
        return answer
    
    return dfs(1, set([1]))


if __name__ == '__main__':
    print(solve())

from collections import deque


def make_list(length, repeat):
    result = [[] for _ in range(length)]
    for _ in range(repeat):
        a, b = map(lambda x: int(x) - 1, input().split())
        result[a].append(b)
        result[b].append(a)
    return result


def main():
    n, m, k = map(int, input().split())
    friend = make_list(n, m)
    block = make_list(n, k)
    group_id = 1
    group = [0 for _ in range(n)]

    def dfs(start, group_id):
        q = deque([start])
        connection = 0
        if group[start] == 0:
            connection += 1
            while q:
                now = q.pop()
                group[now] = group_id
                for nn in friend[now]:
                    if group[nn] == 0:
                        group[nn] = group_id
                        q.append(nn)
                        connection += 1
        return connection

    count = {}
    for i in range(n):
        if group[i] == 0:
            count[group_id] = dfs(i, group_id)
            group_id += 1

    answer = [0 for _ in range(n)]
    for i in range(n):
        answer[i] = count[group[i]] - len(friend[i]) - 1
        for b in block[i]:
            if group[i] == group[b]:
                answer[i] -= 1
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    main()


def make_list(length, loop):
    result = [[] for _ in range(length)]
    for _ in range(loop):
        a, b = map(lambda x: int(x) - 1, input().split())
        result[a].append(b)
        result[b].append(a)
    return result


def main():
    # 敢えてDFSで解いてみる．
    n, m, k = map(int, input().split())
    friend = make_list(n, m)
    brock = make_list(n, k)
    answer = [0] * n
    group_index = [0] * n
    group_id = 1

    def dfs(index):
        q = [index]
        group_index[index] = group_id
        connection = 1
        while not q == []:
            now = q.pop()
            for f in friend[now]:
                if group_index[f] == 0:
                    connection += 1
                    group_index[f] = group_id
                    q.append(f)
        return connection

    id_and_elements = {}
    for i in range(n):
        if group_index[i] == 0:
            id_and_elements[group_id] = dfs(i)
            group_id += 1

    for i in range(n):
        answer[i] += id_and_elements[group_index[i]] - 1
        answer[i] -= len(friend[i])
        for b in brock[i]:
            if group_index[b] == group_index[i]:
                answer[i] -= 1
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    main()


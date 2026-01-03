from collections import defaultdict


def dd(N, abc, ne_table, start_i):
    used_edge = set()
    pivot = start_i

    kouho = {start_i: (0, 0, True)}  # value: (d, path,kakutei)

    for _ in range(N - 1):

        current_dist, path, kaku = kouho[pivot]
        assert kaku
        edges_i = ne_table[pivot]  # エッジリスト取得
        for i in edges_i:
            a, b, weight = abc[i]
            target = a if a != pivot else b

            if target in kouho:
                tmp_d, tmp_path, kakutei = kouho[target]
                if kakutei:
                    continue
                if current_dist + weight < tmp_d:  # 更新
                    kouho[target] = (current_dist + weight, i, False)
                continue
            kouho[target] = (current_dist + weight, i, False)

        min_kouho = min([(k, d, p) for k, (d, p, kakutei) in kouho.items() if not kakutei], key=lambda q: q[1])
        min_kouho_i = min_kouho[0]
        used_edge.add(min_kouho[2])
        kouho[min_kouho_i] = (kouho[min_kouho_i][0], kouho[min_kouho_i][1], True)
        pivot = min_kouho_i
    return used_edge


def main():
    N, M = [int(a) for a in input().split()]

    def pre(a, b, c):
        return a - 1, b - 1, c

    abc = [
        pre(*[int(a) for a in input().split()])
        for _ in range(M)
    ]

    ne_table = defaultdict(lambda: [])
    for i, (a, b, c) in enumerate(abc):
        ne_table[a].append(i)
        ne_table[b].append(i)

    total_used = set()

    for i in range(N):
        used = dd(N, abc, ne_table, i)
        total_used.update(used)

    print(M - len(total_used))


if __name__ == '__main__':
    main()

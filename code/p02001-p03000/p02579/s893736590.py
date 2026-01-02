from collections import deque


def main():
    height, width = [int(x) for x in input().split()]
    init_h, init_w = [int(x) - 1 for x in input().split()]
    dest_h, dest_w = [int(x) - 1 for x in input().split()]
    grid = [input() for _ in range(height)]

    adjacents = (
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
    )

    def gen_warp_can_reach():
        for h in range(-2, 3):
            for w in range(-2, 3):
                if h == 0 == w:
                    continue
                if (h, w) in adjacents:
                    continue
                yield (h, w)

    warp_can_reach = tuple(gen_warp_can_reach())

    qu = deque()
    qu.append((init_h, init_w))
    arrived_total = set()
    arrived_total.add((init_h, init_w))
    distances = [[-1] * width for _ in range(height)]
    warp_count = 0

    def append_qu(now_h, now_w, next_go_to):
        """行き先へ進めそうならキューに追加し， arrived_total に記録する。"""
        for h_delta, w_delta in next_go_to:
            new_h, new_w = h + h_delta, w + w_delta
            if new_h < 0 or new_h >= height or new_w < 0 or new_w >= width:
                continue
            if (new_h, new_w) in arrived_total:
                continue
            if grid[new_h][new_w] == '#':
                arrived_total.add((new_h, new_w))
                continue
            qu.append((new_h, new_w))
            arrived_total.add((new_h, new_w))

    while qu:
        arrived_set_by_cost = set()
        # ワープなしのBFS
        while qu:
            h, w = qu.popleft()
            distances[h][w] = warp_count
            arrived_set_by_cost.add((h, w))
            append_qu(h, w, adjacents)

        warp_count += 1
        # 1回ワープして行ける場所を列挙し，次期スタート地点とする。
        for h, w in arrived_set_by_cost:
            append_qu(h, w, warp_can_reach)

    return distances[dest_h][dest_w]


if __name__ == '__main__':
    print(main())

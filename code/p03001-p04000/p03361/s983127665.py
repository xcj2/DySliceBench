import sys

sys.setrecursionlimit(10 ** 5 + 10)


def input(): return sys.stdin.readline().strip()


def resolve():
    def main():

        H, W = map(int, input().split())
        grid = [[_ for _ in input()] for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if grid[h][w]=='#':
                    for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                        nh, nw = h + j, w + k
                        # nh と nw が街の範囲を超えてたら後の処理をスキップして別方向を模索
                        if nh < 0 or nh >= H or \
                                nw < 0 or nw >= W:
                            continue
                        else:
                            if grid[nh][nw] == '#':
                                break
                            else:
                                if [j, k] == [0, -1]:
                                    return 'No'
        return 'Yes'

    print(main())


resolve()
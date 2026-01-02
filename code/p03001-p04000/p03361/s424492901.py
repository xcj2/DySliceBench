from itertools import repeat, product

def get_targets(a_grid):
    h = len(a_grid)
    w = len(a_grid[0])

    targets = [t for t in product(range(h), range(w)) if a_grid[t[0]][t[1]] == '#']

    return targets

def get_arounds(t, h, w):
    arounds = map(lambda a: (t[0] + a[0], t[1] + a[1]), ((0, 1), (1, 0), (0, -1), (-1, 0)))

    return list(filter(lambda x: -1 < x[0] < h and -1 < x[1] < w, arounds))

def main():
    h, w = tuple(map(int, input().split()))
    a_grid = [list(input()) for _ in range(h)]

    black_sq = get_targets(a_grid)

    if all([any([(sq in black_sq) for sq in get_arounds(bsq, h, w)]) for bsq in black_sq]):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

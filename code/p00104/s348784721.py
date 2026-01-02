def run_magic_tiles(magic_tiles, past_matrix):
    def move_up(x, y):
        return x - 1, y

    def move_down(x, y):
        return x + 1, y

    def move_left(x, y):
        return x, y - 1

    def move_right(x, y):
        return x, y + 1

    def goal():
        return -1, -1

    i, j = 0, 0
    while True:
        res = {
            '^': move_up(i, j),
            'v': move_down(i, j),
            '<': move_left(i, j),
            '>': move_right(i, j),
            '.': goal()
        }.get(magic_tiles[i][j])
        if res[0] == -1 and res[1] == -1:
            return j, i
        else:
            i, j = res
            if past_matrix[i][j]:
                return 'LOOP'
            past_matrix[i][j] = 1


def main():
    while True:
        c, r = map(int, input().split(' '))
        if c == 0 and r == 0:
            break

        past_matrix = [[0 for _ in range(r)] for _ in range(c)]
        tiles = []
        for _ in range(c):
            tiles.append(list(input()))

        res = run_magic_tiles(tiles, past_matrix)
        print('LOOP' if res == 'LOOP' else '%d %d' % (res[0], res[1]))


if __name__ == '__main__':
    main()
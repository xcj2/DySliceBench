import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(
            think(
                [
                    [84, 97, 66],
                    [79, 89, 11],
                    [61, 59, 7]
                ],
                [89, 7, 87, 79, 24, 84, 30]
            ),
            'Yes'
        )

    def test_2(self):
        self.assertEqual(
            think(
                [
                    [41, 7, 46],
                    [26, 89, 2],
                    [78, 92, 8]
                ],
                [6, 45, 16, 57, 17]
            ),
            'No'
        )

    def test_3(self):
        self.assertEqual(
            think(
                [
                    [60, 88, 34],
                    [92, 41, 43],
                    [65, 73, 48]
                ],
                [60, 43, 88, 11, 48, 73, 65, 41, 92, 34]
            ),
            'Yes'
        )


def solve():
    a, b = read()
    result = think(a, b)
    write(result)


def read():
    a = []
    for _ in range(3):
        a.append(read_int(3))
    b = []
    n = read_int(1)[0]
    for _ in range(n):
        b.append(read_int(1)[0])
    return a, b


def read_int(n):
    return read_type(int, n, sep=' ')


def read_float(n):
    return read_type(float, n, sep=' ')


def read_type(t, n, sep):
    return list(map(lambda x: t(x), read_line().split(sep)))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a, b):
    check_mark = 0
    for q in b:
        for row in a:
            for i, cell in enumerate(row):
                if cell == q:
                    row[i] = check_mark
    return 'Yes' if is_bingo(a, check_mark) else 'No'


def write(result):
    print(result)


def is_bingo(a, check_mark):
    rows = len(a)
    cols = len(a[0])

    for y in range(rows):
        if is_bingo_found_in_row(a, y, check_mark):
            return True

    for x in range(cols):
        if is_bingo_found_in_col(a, x, check_mark):
            return True

    if is_bingo_found_in_diagonal(a, check_mark):
        return True
    return False


def is_bingo_found_in_row(a, y, check_mark):
    row = a[y]
    return all(map(lambda x: x == check_mark, row))


def is_bingo_found_in_col(a, x, check_mark):
    col = []
    for row in a:
        col.append(row[x])
    return all(map(lambda x: x == check_mark, col))


def is_bingo_found_in_diagonal(a, check_mark):
    rows = len(a)
    cols = len(a[0])
    if rows != cols:
        return False

    diagonal = []
    for i in range(rows):
        diagonal.append(a[i][i])
    if all(map(lambda x: x == check_mark, diagonal)):
        return True

    diagonal = []
    for i in range(rows):
        diagonal.append(a[i][rows - i - 1])
    if all(map(lambda x: x == check_mark, diagonal)):
        return True

    return False


if __name__ == '__main__':
    # unittest.main()
    solve()
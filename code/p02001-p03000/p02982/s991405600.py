import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([[1, 2], [5, 5], [-2, 8]]), 1)

    def test_2(self):
        self.assertEqual(think([[-3, 7, 8, 2], [-12, 1, 10, 2], [-2, 8, 9, 3]]), 2)

    def test_3(self):
        self.assertEqual(think([[1], [2], [3], [4], [5]]), 10)


def solve():
    x = read()
    result = think(x)
    write(result)


def read():
    n, d = read_int(2)
    x = []
    for _ in range(n):
        if d == 1:
            x.append([read_int(1)[0]])
        else:
            x.append(read_int(d))
    return x


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(x):
    n = len(x)
    max_d = 10
    max_x, min_x = 20, -20
    set_of_square_of_dist = create_set_of_square_of_dist(max_d, max_x, min_x)

    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            square_of_dist = calc_square_of_dist(x[i], x[j])
            if square_of_dist in set_of_square_of_dist:
                count += 1
    return count


def write(result):
    print(result)


def create_set_of_square_of_dist(max_d, max_x, min_x):
    max_diff = max_x - min_x
    max_square_of_sum = (max_diff ** 2) * max_d

    set_of_square_of_dist = set()
    i = 0
    while True:
        if i ** 2 > max_square_of_sum:
            break
        set_of_square_of_dist.add(i ** 2)
        i += 1
    return set_of_square_of_dist


def calc_square_of_dist(x_1, x_2):
    diff_x = [0 for x in range(len(x_1))]
    for i in range(len(x_1)):
        diff_x[i] = x_1[i] - x_2[i]

    return sum([x ** 2 for x in diff_x])


if __name__ == '__main__':
    # unittest.main()
    solve()
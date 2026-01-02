import unittest


class TestB(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([
                ['khabarovsk' ,20],
                ['moscow', 10],
                ['kazan', 50],
                ['kazan', 35],
                ['moscow', 60],
                ['khabarovsk', 40]
            ]),
                [3, 4, 6, 1, 5, 2]
        )

    def test_2(self):
        self.assertEqual(think([
                ['yakutsk', 10],
                ['yakutsk', 20],
                ['yakutsk', 30],
                ['yakutsk', 40],
                ['yakutsk', 50],
                ['yakutsk', 60],
                ['yakutsk', 70],
                ['yakutsk', 80],
                ['yakutsk', 90],
                ['yakutsk', 100]
            ]),
                [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        )


def solve():
    list_of_s_and_p = read()
    result = think(list_of_s_and_p)
    write(result)


def read():
    n = read_int(1)[0]
    list_of_s_and_p = []
    for _ in range(n):
        buf = read_line().split()
        list_of_s_and_p.append([buf[0], int(buf[1])])
    return list_of_s_and_p


def read_int(n):
    return read_type(int, n)


def read_float(n):
    return read_type(float, n)


def read_type(t, n):
    return list(map(lambda x: t(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(list_of_s_and_p):
    data_with_index = []
    for i, e in enumerate(list_of_s_and_p):
        data_with_index.append((i + 1, e[0], e[1]))
    data_with_index.sort(key=lambda x: (x[1], -x[2]))
    return [x[0] for x in data_with_index]


def write(result):
    for r in result:
        print(r)


if __name__ == '__main__':
    # unittest.main()
    solve()
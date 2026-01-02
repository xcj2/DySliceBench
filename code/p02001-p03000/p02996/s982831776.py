import unittest


class TestD(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([[2, 4], [1, 9], [1, 8], [4, 9], [3, 12]]), 'Yes')

    def test_2(self):
        self.assertEqual(think([[334, 1000], [334, 1000], [334, 1000]]), 'No')

    def test_3(self):
        self.assertEqual(think([[384, 8895], [1725, 9791], [170, 1024], [4, 11105], [2, 6], [578, 1815], [702, 3352], [143, 5141], [1420, 6980], [24, 1602], [849, 999], [76, 7586], [85, 5570], [444, 4991], [719, 11090], [470, 10708], [1137, 4547], [455, 9003], [110, 9901], [15, 8578], [368, 3692], [104, 1286], [3, 4], [366, 12143], [7, 6649], [610, 2374], [152, 7324], [4, 7042], [292, 11386], [334, 5720]]), 'Yes')


def solve():
    list_of_a_and_b = read()
    result = think(list_of_a_and_b)
    write(result)


def read():
    n = read_int(1)[0]
    list_of_a_and_b = []
    for i in range(n):
        list_of_a_and_b.append(read_int(2))
    return list_of_a_and_b


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(data):
    data.sort(key=lambda x: (x[1], x[0]))
    current_time = 0
    for d in data:
        if current_time + d[0] > d[1]:
            return 'No'
        current_time += d[0]
    return 'Yes'


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
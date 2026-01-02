import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([[[2, 1]], [[1, 1]], [[2, 0]]]), 2)

    def test_2(self):
        self.assertEqual(think([[[2, 1], [3, 0]], [[3, 1], [1, 0]], [[1, 1], [2, 0]]]), 0)

    def test_3(self):
        self.assertEqual(think([[[2, 0]], [[1, 0]]]), 1)

    def test_4(self):
        self.assertEqual(count_bits_one(1), 1)

    def test_5(self):
        self.assertEqual(count_bits_one(2), 1)

    def test_6(self):
        self.assertEqual(count_bits_one(3), 2)

    def test_7(self):
        self.assertEqual(count_bits_one(31), 5)


def solve():
    list_of_testimony = read()
    result = think(list_of_testimony)
    write(result)


def read():
    n = read_int(1)[0]
    list_of_testimony = []
    for _ in range(n):
        list_of_x_y = []
        a = read_int(1)[0]
        for __ in range(a):
            list_of_x_y.append(read_int(2))
        list_of_testimony.append(list_of_x_y)
    return list_of_testimony


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


def think(data):
    max_bits = 2 ** len(data)
    result = 0
    for bits in range(max_bits):
        # print(is_legal(bits, data), bits)
        if is_legal(bits, data):
            result = max(result, count_bits_one(bits))
    return result


def is_legal(bits, data):
    n = len(data)
    for i in range(n):
        if not is_honest(i, bits):
            continue
        for x, y in data[i]:
            if y == 1:
                if not is_honest(x - 1, bits):
                    return False
            else:
                if is_honest(x - 1, bits):
                    return False
    return True


def is_honest(i, bits):
    # print('is_honest', i, bits, (bits >> i) % 2 == 1)
    return (bits >> i) % 2 == 1


def count_bits_one(bits):
    count = 0
    while bits > 0:
        if bits % 2 == 1:
            count += 1
        bits //= 2
    return count


def write(result):
    print(result)


if __name__ == '__main__':
    # unittest.main()
    solve()
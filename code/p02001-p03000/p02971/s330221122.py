import unittest


class TestC(unittest.TestCase):
    def test_1(self):
        self.assertEqual(think([1, 4, 3]), [4, 3, 4])

    def test_2(self):
        self.assertEqual(think([5, 5]), [5, 5])


def solve():
    a = read()
    result = think(a)
    write(result)


def read():
    n = read_int(1)[0]
    a = []
    for _ in range(n):
        a.append(read_int(1)[0])
    return a


def read_int(n):
    return list(map(lambda x: int(x), read_line().split(' ')))[:n]


def read_float(n):
    return list(map(lambda x: float(x), read_line().split(' ')))[:n]


def read_line(n=0):
    if n == 0:
        return input().rstrip()
    else:
        return input().rstrip()[:n]


def think(a):
    hist = make_histogram(a)

    list_form_of_hist = []
    for k, v in hist.items():
        list_form_of_hist.append([k, v])
    list_form_of_hist.sort(key=lambda x: -x[0])

    result = []
    for e in a:
        if e == list_form_of_hist[0][0]:
            if list_form_of_hist[0][1] == 1:
                result.append(list_form_of_hist[1][0])
            else:
                result.append(list_form_of_hist[0][0])
        else:
            result.append(list_form_of_hist[0][0])
    return result


def write(result):
    for e in result:
        print(e)


def make_histogram(a):
    hist = {}
    for e in a:
        if e in hist:
            hist[e] += 1
        else:
            hist[e] = 1
    return hist


if __name__ == '__main__':
    # unittest.main()
    solve()
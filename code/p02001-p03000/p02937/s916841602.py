import unittest
import collections
import bisect


def solve(s, t):
    d = collections.defaultdict(list)
    for i, c in enumerate(s):
        d[c].append(i)
    i = 0
    n = 0
    for c in t:
        if len(d[c]) == 0:
            return - 1
        k = bisect.bisect_left(d[c], i)
        if k == len(d[c]):
            n += 1
            k = bisect.bisect_left(d[c], 0)
        i = d[c][k]+1
    return len(s)*n+i


def main():
    s = input()
    t = input()
    print(solve(s, t))


class TestAbc138_e(unittest.TestCase):
    def test_abc138_e(self):
        self.assertEqual(solve('contest', 'son'), 10)
        self.assertEqual(solve('contest', 'programming'), -1)
        self.assertEqual(solve('contest', 'sentence'), 33)
        self.assertEqual(solve('abc', 'abccccac'), 15)


if __name__ == "__main__":
    # unittest.main()
    main()

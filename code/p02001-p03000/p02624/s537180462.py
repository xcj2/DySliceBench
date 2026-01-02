import unittest


def solve(n):
    total = 0
    for i in range(1, n+1):
        k = n // i
        total += i * k * (k + 1) // 2

    return total


def main():
    n = int(input())
    print(solve(n))


if __name__ == "__main__":
    main()


class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(solve(1), 1)
        self.assertEqual(solve(2), 5)
        self.assertEqual(solve(3), 11)
        self.assertEqual(solve(4), 23)

    def test2(self):
        self.assertEqual(solve(100), 26879)

    def test3(self):
        self.assertEqual(solve(10000000), 838627288460105)

import unittest


def solve(n):
    used = set()
    total = 0
    for i in range(1, int(n ** 0.5)+1):
        if n % i > 0:
            continue
        d = n // i
        cand = [i-1, d-1]
        for c in cand:
            if c not in used and c > 0 and n % c == n // c:
                total += c
                used.add(c)

    return total


def main():
    n = int(input())
    result = solve(n)
    print(result)


if __name__ == "__main__":
    main()


class Test(unittest.TestCase):
    def test_solve_1(self):
        n = 8
        actual = solve(n)
        expected = 10
        self.assertEqual(actual, expected)

    def test_solve_2(self):
        n = 1000000000000
        actual = solve(n)
        expected = 2499686339916
        self.assertEqual(actual, expected)

import sys
from io import StringIO
import unittest


def resolve():
    n, m = map(int, input().split())
    item = []*n
    item = input().split()

    all = 0
    for i in range(len(item)):
        all += int(item[i])

    # リストの作成
    dicta = {}
    for i, a in enumerate(item):
        dicta[i] = int(a)
    dicta_sorted = sorted(dicta.items(), key=lambda x: x[1], reverse=True)

    # えらべるか判定
    choice_count = 0
    i = 0
    for i in range(m):
        aaa = 4 * m
        if dicta_sorted[i][1] < all/aaa:
            continue
        choice_count += 1

    if choice_count >= m:
        print("Yes")
    else:
        print("No")


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """4 1
5 4 2 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 2
380 19 1"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """12 3
4 56 78 901 2 345 67 890 123 45 6 789"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()
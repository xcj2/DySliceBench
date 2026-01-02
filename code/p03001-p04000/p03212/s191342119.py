import sys
from io import StringIO
import unittest


def recursive(base, pattern, n):

    for i in ["7", "5", "3"]:

        new_target = "".join(base + str(i))

        # 条件を満たさない場合は、再帰を呼ばない。
        if int(new_target) > n:
            continue

        # 条件を満たす場合、リストに加える
        if new_target.count("7") >= 1 and new_target.count("5") >= 1 and new_target.count("3") >= 1:
            pattern.append(new_target)

        recursive(new_target, pattern, n)


def resolve():

    n = int(input())

    pattern = []

    # 再帰的処理
    for i in ["7", "5", "3"]:
        recursive(i, pattern, n)

    print(len(pattern))


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
        input = """575"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3600"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999999"""
        output = """26484"""
        self.assertIO(input, output)


if __name__ == "__main__":
    #unittest.main()
    resolve()

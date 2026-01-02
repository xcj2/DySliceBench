#
# abc105 b
#
import unittest
from io import StringIO
import sys


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    N = int(input())
    C = 4
    D = 7

    for i in range(N//C+1):
        for j in range(N//D+1):
            if i*C + j*D == N:
                print("Yes")
                exit()
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
        input = """11"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """40"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    #unittest.main()
    resolve()

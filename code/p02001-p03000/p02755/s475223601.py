import sys
from io import StringIO
import unittest


def resolve():
    A, B = [int(i) for i in input().split()]
    mina = int(-(-min(A / 0.08, B / 0.1) // 1))
    while int(mina * 0.08) == A or int(mina * 0.1) == B:
        if int(mina * 0.08) == A and int(mina * 0.1) == B:
            print(mina)
            return
        mina += 1
    else:
        print(-1)


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
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """25 32"""
        output = """320"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()

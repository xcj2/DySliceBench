import sys
from io import StringIO
import unittest


def resolve():
    s = input()

    odd = set(['R', 'U', 'D'])
    even = set(['L', 'U', 'D'])

    ans = True

    for i, ss in enumerate(s):
        if (i + 1) % 2 == 0 and ss in even:
            continue
        elif (i + 1) % 2 == 1 and ss in odd:
            continue
        else:
            ans = False
            break

    if ans:
        print('Yes')
    else:
        print('No')


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
        input = """RUDLUDR"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """DULL"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """UUUUUUUUUUUUUUU"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_4(self):
        input = """ULURU"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_5(self):
        input = """RDULULDURURLRDULRLR"""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    # unittest.main()
    resolve()
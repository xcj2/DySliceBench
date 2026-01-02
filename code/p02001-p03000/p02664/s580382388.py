import sys
from io import StringIO
import unittest


def resolve():
    t = list(input())

    if t[0] == '?':
        t[0] = 'D'

    for i in range(1, len(t) - 1):
        if t[i] == '?':
            if t[i - 1] == 'P':
                t[i] = 'D'
            else:
                if t[i + 1] == '?':
                    t[i] = 'P'
                    t[i + 1] = 'D'
                elif t[i + 1] == 'D':
                    t[i] = 'P'
                else:
                    t[i] = 'D'

    if t[-1] == '?':
        t[-1] = 'D'

    print(''.join(t))



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
        input = """PD?D??P"""
        output = """PDPDPDP"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """P?P?"""
        output = """PDPD"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()

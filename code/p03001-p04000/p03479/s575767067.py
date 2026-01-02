import sys
from io import StringIO
import unittest

def resolve():
    x, y = map(int, input().split())

    ans = [x]

    while 1:
        tmp = ans[-1] * 2
        if tmp > y:
            break
        else:
            ans.append(tmp)
            
    print(len(ans))

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
        input = """3 20"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """25 100"""
        output = """3"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """314159265 358979323846264338"""
        output = """31"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
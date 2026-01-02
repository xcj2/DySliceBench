import sys
from io import StringIO
import unittest

def resolve():
    h, w = map(int, input().split())
    s = [list(input()) for _ in range(h)]

    ans = [[0]*w for i in range(h)]

    def put(s, i, j):
        if 0 <= i-1:
            s[i-1][j] += 1
        if 0 <= i-1 and 0 <= j-1:
            s[i-1][j-1] += 1
        if 0 <= j-1:
            s[i][j-1] += 1
        if i+1 < h:
            s[i+1][j] += 1
        if i+1 < h and j+1 < w:
            s[i+1][j+1] += 1
        if j+1 < w:
            s[i][j+1] += 1
        if 0 <= i-1 and j+1 < w:
            s[i-1][j+1] += 1
        if 0 <= j-1 and i+1 < h:
            s[i+1][j-1] += 1
        return s
    
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans = put(ans, i, j)
    for i in range(h):
        for j in range(w):
            if s[i][j] == '#':
                ans[i][j] = '#'
    
    ans_str = ''
    for i in range(h):
        for j in range(w):
            ans_str += str(ans[i][j])
        ans_str += '\n'
    ans_str = ans_str[:-1]
    print(ans_str)
    



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
        input = """3 5
.....
.#.#.
....."""
        output = """11211
1#2#1
11211"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
#####
#####
#####"""
        output = """#####
#####
#####"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6
#####.
#.#.##
####.#
.#..#.
#.##..
#.#..."""
        output = """#####3
#8#7##
####5#
4#65#2
#5##21
#4#310"""
        self.assertIO(input, output)


if __name__ == "__main__":
    # unittest.main()
    resolve()


import sys
def resolve():
    input = sys.stdin.readline
    H,W=map(int,input().rstrip().split())
    S=[input().rstrip() for _ in range(H)]

    dx=[0,0,-1,1]#上下左右
    dy=[1,-1,0,0]

    for i in range(H):
        for j in range(W):
            if(S[i][j]=="#"):
                for dir in range(4):
                    nx=j+dx[dir]
                    ny=i+dy[dir]

                    if(nx<0 or nx>=W):
                        continue
                    if(ny<0 or ny>=H):
                        continue

                    if(S[i][j]==S[ny][nx]):
                        break
                else:
                    print("No")
                    return
    print("Yes")




from io import StringIO
import unittest

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
        input = """3 3
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
import sys
def resolve():
        input = sys.stdin.readline
        N=int(input().rstrip())
        a=[input().rstrip() for _ in range(N)]

        index=0
        ans=0
        for i in range(N):
            index=int(a[index])-1
            ans+=1
            if(index==1):
                print(ans)
                return
        print(-1)



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
        input = """3
3
1
2"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4
3
4
1
2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5
3
3
4
2
4"""
        output = """3"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
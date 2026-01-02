import sys
input = sys.stdin.readline
N=int(input().rstrip())
count=0

def resolve():
    global count
    dfs("")
    print(count)

def dfs(s):
    global count
    

    s3=str(s)+str(3) if s!="" else str(3)
    s5=str(s)+str(5) if s!="" else str(5)
    s7=str(s)+str(7) if s!="" else str(7)

    if s3.find("3")!=-1 and s3.find("5")!=-1 and s3.find("7")!=-1 and int(s3)<=N:
        count+=1
    if int(s3)>N:
        return
    dfs(s3)

    if s5.find("3")!=-1 and s5.find("5")!=-1 and s5.find("7")!=-1 and int(s5)<=N:
        count+=1
    if int(s5)>N:
        return
    dfs(s5)

    if s7.find("3")!=-1 and s7.find("5")!=-1 and s7.find("7")!=-1 and int(s7)<=N:
        count+=1
    if int(s7)>N:
        return
    dfs(s7)


import sys
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
#    unittest.main()
    resolve()
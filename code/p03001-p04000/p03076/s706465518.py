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
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)

def resolve():
    a=[]
    count=0
    for i in range(5):
        x=int(input())
        if x%10==0:
            count+=x
        else:
            a.append(x)
    if len(a)==0:
        print(count)
    else:
        a.sort(key= lambda xx: xx%10 , reverse= True)

        for i in a[:-1]:
            count+=i-i%10+10
        else:
            count+=a[-1]
        print(count)
if __name__ == "__main__":
    resolve()
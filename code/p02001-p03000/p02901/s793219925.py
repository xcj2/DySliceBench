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
        input = """2 3
10 1
1
15 1
2
30 2
1 2"""
        output = """25"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """12 1
100000 1
2"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 6
67786 3
1 3 4
3497 1
2
44908 3
2 3 4
2156 3
2 3 4
26230 1
2
86918 1
3"""
        output = """69942"""
        self.assertIO(input, output)
def resolve():
    (N,M)=(int(i) for i in input().split())
    housekis=[]
    for i in range(M):
        (a,b)=(int(i) for i in input().split())
        ability=sum([2**(int(i)-1) for i in input().split()])
        housekis.append([a,ability])
    dpt=[[1<<29 for i in range(2**N)] for j in range(M+1)]
    dpt[0][0]=0
    for i in range(M):
        for j in range(2**N):

            dpt[i+1][j]=min(dpt[i][j],dpt[i+1][j])
            dpt[i+1][j | housekis[i][1]]=min(dpt[i+1][j | housekis[i][1]],housekis[i][0]+dpt[i][j])

    if dpt[-1][-1]==1<<29:
        print(-1)
    else:
        print(dpt[-1][-1])


if __name__ == "__main__":
    resolve()
import sys

input = sys.stdin.readline
N,M=map(int,input().rstrip().split())
G=[[0 for _ in range(N)] for __ in range(N)]
used=[0 for _ in range(N)]
used[0]=True

for i in range(M):
    a,b=map(int,input().rstrip().split())
    G[a-1][b-1]=True
    G[b-1][a-1]=True

def resolve():
    print(dfs(0,used))


def dfs(v,used):
    if not False in used:
        return 1
    ans=0
    for i in range(N):
        if G[v][i]==False:
            continue
        if used[i]==True:
            continue

        used[i]=True
        ans+=dfs(i,used)
        used[i]=False
    return ans

    



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
1 2
1 3
2 3"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 7
1 3
2 7
3 4
4 5
4 6
5 6
6 7"""
        output = """1"""
        self.assertIO(input, output)

if __name__ == "__main__":
    #unittest.main()
    resolve()
import sys
from io import StringIO
import unittest
import heapq
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
        input = """4 5
1 2
2 3
2 4
4 1
4 3"""
        output = """3
1
2
4"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 5
1 2
2 3
2 4
1 4
4 3"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 9
1 2
2 3
3 4
4 5
5 6
5 1
5 2
6 1
6 2"""
        output = """4
2
3
4
5"""
        self.assertIO(input, output)



def resolve():
    (N,M)=(int(i) for i in input().split())
    graph=[[[],[]] for i in range(N)]
    for i in range(M):
        (a,b)=(int(i)-1 for i in input().split())
        graph[a][0].append(b)
        graph[b][1].append(a)
    flg=True
    element=[True for i in range(N)]
    while flg:
        flg=False
        for i in range(N):
            if element[i]==False:
                continue
            if graph[i][0]==[]:
                for j in graph[i][1]:
                    graph[j][0].remove(i)
                flg=True
                graph[i][1]=[]
                element[i]=False
            if graph[i][1]==[]:
                for j in graph[i][0]:
                    graph[j][1].remove(i)
                flg=True
                graph[i][0]=[]
                element[i]=False




    def dicstra(i):

        cost=[100000 for _ in graph]
        cost[i]=0

        oya=[[] for _ in graph]
        muki = [j[0] for j in graph]

        visited=[False for j in muki]
        q=[]
        heapq.heappush(q,[0,i])
        while q:
            c,ind=heapq.heappop(q)
            visited[ind]=True
            oya[ind].append(ind)
            for j in muki[ind]:
                if (not visited[j]) and  cost[j]>cost[ind]+1:
                    cost[j]=cost[ind]+1
                    oya[j]=oya[ind][:]
                    heapq.heappush(q,[cost[j],j])
        xx=[oya[j] for j in graph[i][1]]
        xx.sort(key=lambda it: len(it))


        for j in xx[0]:
            for k in range(len(graph[j][0])):
                if k>=len(graph[j][0]):
                    break                
                x=graph[j][0][k]
                if not (x in xx[0]):
                    graph[j][0].remove(x)
                    if k>=len(graph[j][0]):
                        break
            for k in range(len(graph[j][1])):
                if k>=len(graph[j][1]):
                        break
                x=graph[j][1][k]
                if not (x in xx[0]):

                    graph[j][1].remove(x)

            if len(graph[j][1])>1:

                return j
                
        else:
            print(len(xx[0]))
            for i in xx[0]:
                print(i+1)
            return -1
    for i in range(N):
        if element[i]:
            while i>=0:
                
                i = dicstra(i)
            
            
            break
    else:
        print(-1)



if __name__ == "__main__":
    resolve()
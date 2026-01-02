import sys
input = sys.stdin.readline

n = int(input())
A = [list(map(int,input().split())) for _ in range(n)]

class WarshallFloyd:
    def __init__(self,n):
        self.v = n
        self.d = [[1e100]*n for _ in range(n)]
        for i in range(n):
            self.d[i][i] = 0

    def path(self,x,y,c):
        if x == y:
            return False
        self.d[x][y] = c
        self.d[y][x] = c
        return True

    def build(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])

wf = WarshallFloyd(n)

for i in range(1,n):
    for j in range(i):
        wf.path(i,j,A[i][j])

wf.build()
ans = 0
for i in range(n-1):
    for j in range(i+1,n):
        if A[i][j] > wf.d[i][j]:
            print(-1)
            exit(0)
        flag = 1
        for k in range(n):
            if i != k != j:
                if wf.d[i][j] == wf.d[i][k] + wf.d[k][j]:
                    flag = 0
                    break
        if flag:
            ans += A[i][j]
print(ans)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

INF = 100100100

class Queue:
    __slots__ = ['Q', 'begin', 'end']
    def __init__(self):
        self.Q = [None] * 100
        self.begin = 0
        self.end = 0
    def full(self) -> bool:
        if self.begin == 0 and self.end == 99:
            return True
        elif self.begin == self.end + 1:
            return True
        else:
            return False
    def empty(self) -> bool:
        if self.begin == self.end:
            return True
        else:
            return False
    def insert(self, num: int):
        if self.full():
            print('Error: Queue is full.')
        else:
            if self.end == 99:
                self.end = 0
            else:
                self.end += 1
            self.Q[self.end-1] = num
    def pop(self) -> int:
        if self.empty():
            print('Error: Queue is empty.')
            return
        else:
            if self.begin == 99:
                self.begin = 0
                return self.Q[99]
            else:
                self.begin += 1
                return self.Q[self.begin-1]

def bfs(M: list, visited: list, d: list, v: int = 0):
    n = len(visited)
    Q = Queue()
    visited[v] = True
    d[v] = 0
    Q.insert(v)
    while not Q.empty():
        u = Q.pop()
        for i in range(n):
            if M[u][i] == 1 and not visited[i]:
                visited[i] = True
                d[i] = d[u] + 1
                Q.insert(i)


def main():
    n = int(input())
    M = [[0]*n for _ in range(n)]
    for _ in range(n):
        a = list(map(int, input().split()))
        i = a[0]-1
        for j in range(a[1]):
            k = a[j+2]-1
            M[i][k] = 1
    visited = [False] * n
    d = [INF] * n
    bfs(M, visited, d)
    for i, l in enumerate(d):
        if l == INF:
            print(i+1, -1)
        else:
            print(i+1, l)

if __name__ == '__main__': main()

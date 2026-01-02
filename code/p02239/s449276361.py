# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C&lang=jp
# Breadth First Search: python3
#  2018.12.06 yonezawa

import sys
input = sys.stdin.readline
from collections import deque

class node:
    def __init__(self):
        n = self.n = int(input())
        self.cnt = 0
        self.discover = [-1] * n
        self.pos = [1] * n
        self.nmap = [[0 for i in range(n)] for i in range(n)]
    
        for _ in range(n):
            l = list(map(int,input().split()))
            a = l[0] - 1
            for i in l[2:]:
                self.nmap[a][i-1] = 1
    def printMap(self):
        for i in self.nmap:
            print (*i)

    def printResult(self):
        for i in range(self.n):
            print(i+1,self.discover[i])

    def bfs(self,u):
        self.pos[u] = 0
        self.discover[u] = self.cnt
        t = deque()
        t.append(u)
        while t:
            n = t.popleft()
            for i in range(self.n):
                if (self.nmap[n][i] == 1 and self.pos[i] == 1 ):
                    t.append(i)
                    self.pos[i] = 0
                    self.discover[i] = self.discover[n] + 1
                
def main():
    a = node()
    a.bfs(0)
    a.printResult()
    #a.printMap()
if __name__ == '__main__':
    main()


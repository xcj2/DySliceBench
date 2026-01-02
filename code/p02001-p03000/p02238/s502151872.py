# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_A&lang=jp
# Graph: python3
#  2018.12.05 yonezawa

import sys
input = sys.stdin.readline

class node:
    def __init__(self):
        n = self.n = int(input())
        self.cnt = 0
        self.start = [-1] * n
        self.end = [-1] * n
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
            print(i+1,self.start[i],self.end[i])

    def dfs(self,u):
        self.cnt += 1
        self.start[u] = self.cnt
        self.pos[u] = 0
        for i in range(self.n):
            if self.nmap[u][i] == 1 and self.pos[i] == 1:    
                self.dfs(i)
        self.cnt += 1
        self.end[u] = self.cnt
                
def main():
    a = node()
    for i in range(a.n):
        if a.pos[i] == 1:
            a.dfs(i)
    a.printResult()

if __name__ == '__main__':
    main()


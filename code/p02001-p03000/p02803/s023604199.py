import sys
sys.setrecursionlimit(700000)

def s_in():
    return input()

def n_in():
    return int(input())

def l_in():
    return list(map(int, input().split()))

def print_l(l):
    print(' '.join(map(str, l)))

class Interval():
    def __init__(self, li):
        self.li = li
        self.n = len(li)
        self.sum_li = [li[0]]
        for i in range(1, self.n):
            self.sum_li.append(self.sum_li[i-1] + li[i])

    def sum(self, a, b=None):
        if b is None:
            return self.sum(0, a)

        res = self.sum_li[min(self.n-1, b-1)]
        if a > 0:
            res -= self.sum_li[a-1]
        return res

h,w = l_in()
S = [s_in() for _ in range(h)]
    
from collections import deque

res = 0
for i in range(h):
    for j in range(w):
        q = deque()
        s = set()
        check = lambda x,y: (not (x,y) in s) and x >= 0 and x < h and y >=0 and y < w and S[x][y] == '.'
        
        if S[i][j] == '.':
            q.append((i,j,0))

        while len(q) > 0:
            i,j,d = q.popleft()
            s.add((i,j))
            res = max(d,res)
            
            if check(i+1,j):
                s.add((i+1,j))
                q.append((i+1,j,d+1))
            if check(i-1,j):
                s.add((i-1,j))                
                q.append((i-1,j,d+1))
            if check(i,j+1):
                s.add((i,j+1))            
                q.append((i,j+1,d+1))
            if check(i,j-1):
                s.add((i,j-1))            
                q.append((i,j-1,d+1))

print(res)


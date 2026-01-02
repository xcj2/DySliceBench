import sys
readline = sys.stdin.buffer.readline

from collections import deque
import copy

def myinput():
    return map(int,readline().split())

def mycol(data,col):
    return [ row[col] for row in data ]

ls_ans = []

w,h = myinput()
c = [ list(myinput()) for _ in range(h) ]

while w!=0 or h!=0:
    def dfs(sx,sy):
        stack = deque()
        stack.append([sx,sy])
        while stack:
            x,y = stack.pop()
            if c[x][y]==1:
                c[x][y] = 0
                for i in range(-1,2):
                    for j in range(-1,2):
                        if i==0 and j==0:
                            continue
                        else:
                            nx = x + i
                            ny = y + j
                            if nx==-1 or ny==-1 or nx==h or ny==w:
                                pass
                            else:
                                if c[nx][ny]==1:
                                    stack.append([nx,ny])
                                else:
                                    pass
            else:
                pass

    ans = 0
    for i in range(h):
        for j in range(w):
            if c[i][j]==1:
                dfs(i,j)
                ans += 1
            else:
                pass
    # print(ans)
    ls_ans.append(ans)

    w,h = myinput()
    c = [ list(myinput()) for _ in range(h) ]

for i in range(len(ls_ans)):
    print(ls_ans[i])

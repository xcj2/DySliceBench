from collections import deque

y = [-1,0,1,0]
x = [0,-1,0,1]

def main():

    h,w = 0,0
    c = []

    def check(i,j):
        return 0<=i and i<h and 0<=j and j<w

    def bfs(a,b):
        res = 0
        d = deque()
        d.append([a,b])
        f = [[False]*w for _ in range(h)]
        while len(d):
            i,j = d.popleft()
            if not check(i,j):continue
            if c[i][j]=='#':continue
            if f[i][j]==True:continue
            res += 1
            f[i][j]=True
            for k in range(4):
                d.append([i+y[k],j+x[k]])
        return res

    while True:
        w,h = map(int,input().split())
        if h==0 and w==0:break
        c = []
        for i in range(h):
            c.append(input())
        res = 0
        for i in range(h):
            for j in range(w):
                if c[i][j]=='@':
                    res = bfs(i,j)
        print(res)

if __name__ == '__main__':
    main()



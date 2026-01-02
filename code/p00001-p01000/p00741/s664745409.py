from collections import deque

y = [1,1,1,0,0,-1,-1,-1]
x = [-1,0,1,-1,1,-1,0,1]

def main():
    w,h = 0,0
    c = []

    def check(i,j):
        return 0<=i and i<h and 0<=j and j<w

    def bfs(a,b):
        d = deque()
        d.append([a,b])
        while len(d):
            i,j = d.popleft()
            if not check(i,j):continue
            if c[i][j]==0:continue
            c[i][j]=0
            for k in range(8):
                d.append([i+y[k],j+x[k]])

    while True:
        w,h = map(int,input().split())
        if w==0 and h==0: break
        c = []
        res = 0
        for _ in range(h):
            c.append(list(map(int,input().split())))
        for i in range(h):
            for j in range(w):
                if c[i][j]==1:
                    bfs(i,j)
                    res+=1
        print(res)

if __name__ == '__main__':
    main()



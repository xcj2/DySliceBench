import sys
from collections import deque

W,H,C = None,None,None
mmax = None

def main():
    global W,H,C,mmax

    while True:
        W,H = map(int,input().split())
        if not W and not H:
            return
        C = []
        mmax = [[-1]*(W+1) for _ in range(H+1)]
        for _ in range(H):
            C.append(list(input()))
        # visualize(C)

        num = 0

        # for i in range(H):
        #     for j in range(W):
        #         if mmax[i][j] != -1:
        #             continue
        #         print("------", i, j, "--------")
        #         num = max(num, bfs(i,j))

        for i in reversed(range(H)):
            for j in reversed(range(W)):
                if mmax[i][j] != -1:
                    continue
                num = max(num, bfs(i,j))
        
        print(num)


def bfs(y,x):
    global W,H,C,mmax

    if not C[y][x].isdigit():
        return 0

    l = []
    queue = deque(l)
    dd = [(0,-1), (-1,0)]
    num = 0

    queue.appendleft((C[y][x],(y,x)))
    mmax[y][x] = int(C[y][x])

    while len(queue) != 0:
        s, (uy,ux) = queue.pop()
        for dy,dx in dd:
            vy,vx = uy+dy, ux+dx
            if not (0 <= vy < H and 0 <= vx < W):
                num = max(num, mmax[uy][ux])
                continue
            if C[vy][vx].isdigit():
                n = int(C[vy][vx]+s)
                if mmax[vy][vx] < n:
                    queue.appendleft((C[vy][vx]+s, (vy,vx)))
                    mmax[vy][vx] = n
            else:
                num = max(num, mmax[uy][ux])

    return num


# def bfs(y,x): # h w
#     global W,H,C,mmax

#     if not C[y][x].isdigit():
#         return 0

#     l = []
#     queue = deque(l)
#     dd = [(0,1), (1,0)]
#     num = 0

#     queue.appendleft((C[y][x],(y,x)))
#     mmax[y][x] = int(C[y][x])

#     while len(queue) != 0:
#         print(len(queue))
#         s, (uy,ux) = queue.pop()
#         for dy,dx in dd:
#             vy,vx = uy+dy, ux+dx
#             if not (0 <= vy < H and 0 <= vx < W):
#                 num = max(num, mmax[uy][ux])
#                 continue
#             if C[vy][vx].isdigit():
#                 n = int(s+C[vy][vx])
#                 if mmax[vy][vx] < n:
#                     queue.appendleft((s+C[vy][vx], (vy,vx)))
#                     mmax[vy][vx] = n
#             else:
#                 num = max(num, mmax[uy][ux])

#     return num


def visualize(mmap):
    for row in mmap:
        print(" ".join(row))

            

if __name__ == '__main__':
    main()

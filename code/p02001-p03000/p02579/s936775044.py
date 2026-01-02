from collections import deque

H,W = map(int,input().split())
Ch,Cw = map(int,input().split())
Dh,Dw = map(int,input().split())
Ch,Cw,Dh,Dw = Ch-1,Cw-1,Dh-1,Dw-1
S = []
for i in range(H):
    S.append(list(input()))


def check(h,w):
    if 0<=h<=H-1 and 0<=w<=W-1:
        if S[h][w] == ".":
            return True
    return False

def move_A():
    v = [[-1,0],[1,0],[0,1],[0,-1]]
    while qA != deque():
        h,w,c = map(int,qA.pop())
        searched[h][w] = True
        qB.append([h,w,c])
        for vv in v:
            next_h = h+vv[0]
            next_w = w+vv[1]
            if check(next_h,next_w) and searched[next_h][next_w] == False:
                qA.append([next_h,next_w,c])
                cost[next_h][next_w] = c

def move_B():
    while qB != deque():
        h,w,c = map(int,qB.pop())
        for i in range(-2,3):
            for j in range(-2,3):
                next_h = h + i
                next_w = w + j
                if check(next_h,next_w) and searched[next_h][next_w] == False:
                    qA.append([next_h,next_w,c+1])
                    searched[next_h][next_w] = True
                    cost[next_h][next_w] = c+1
        
searched = [[False]*W for _ in range(H)]
cost = [[10**9]*W for _ in range(H)]

qA = deque()
qB = deque()
qA.append([Ch,Cw,0])
cost[Ch][Cw] = 0

while qA != deque():
    move_A()
    move_B()

if searched[Dh][Dw] == False:
    print(-1)
else:
    print(cost[Dh][Dw])

h,w = map(int, input().split())
ch, cw = map(int, input().split())
ch -= 1
cw -= 1
dh,dw = map(int, input().split())
dh -= 1
dw -= 1

def trans(s):
    res = []
    for i in s:
        if i == '.':
            res.append(-1)
        else:
            res.append(-2)
    return res

def move(x,y,dq,dq_next):
    for ix,iy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if ix > h-1 or ix < 0 or iy > w-1 or iy < 0:
            continue
        if (m[ix][iy] == -1) or (m[ix][iy] > m[x][y]):
            m[ix][iy] = m[x][y]
            dq.append((ix, iy))
    for ix, iy in [(x-2, y-2), (x-2, y-1), (x-2, y), (x-2, y+1), (x-2, y+2),
                        (x-1, y-2), (x-1, y-1), (x-1, y+1), (x-1, y+2),
                        (x, y-2), (x, y+2),
                        (x+1, y-2), (x+1, y-1), (x+1, y+1), (x+1, y+2),
                        (x+2, y-2), (x+2, y-1), (x+2, y), (x+2, y+1), (x+2, y+2)]:
        if ix > h-1 or ix < 0 or iy > w-1 or iy < 0:
            continue
        if m[ix][iy] == -1:
            m[ix][iy] = m[x][y] + 1
            dq_next.append((ix, iy))
            
m = [trans(input()) for _ in range(h)]

from collections import deque

m[ch][cw] = 0

def main():
    dq = deque()
    dq_next = deque()
    dq.append((ch,cw))
    while True:
        while len(dq)>0:
            xx, yy = dq.popleft()
            if xx == dh and yy == dw:
                return m[xx][yy]
            move(xx, yy, dq, dq_next)
        if len(dq_next) > 0:
            dq = dq_next.copy()
            dq_next = deque()
        else:
            return -1
          
print(main())
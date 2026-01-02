from sys import stdin
import sys
import collections


##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return map(int, input().split()) 
    else: return map(int, input().split(sep))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
def main():
    H, W = rip()
    S = [rs() for i in range(H)]
    #min = np.full((H,W),-1, dtype = 'int')
    min = [[-1] * W for i in range(H)]
    q = collections.deque()
    def enc(h, w): return h * W + w
    def inRange(t, l, r): return l <= t and t < r
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]

    for i in range(H):
        for j in range(W):
            if S[i][j] == '#':
                q.append(enc(i,j))
                min[i][j] = 0
    while(len(q) > 0):
        rc = q.popleft()
        y = rc // W
        x = rc % W
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if (not inRange(nx,0,W)) or (not inRange(ny,0,H)): continue
            if min[ny][nx] == -1:
                min[ny][nx] = min[y][x] + 1
                q.append(enc(ny,nx))
    
    ma = 0
    for i in range(H):
        for j in range(W):
            ma = max(ma, min[i][j])
    print(ma)





if __name__ == "__main__":
    main()

from collections import deque
import sys

def input():
    return sys.stdin.readline().strip()

def main():
    H,W = map(int,input().split())
    Ch,Cw = map(int,input().split())
    Dh,Dw = map(int,input().split())
    S = [list(input()) for _ in range(H)]
    S[Ch-1][Cw-1] = 0

    def bfs(x,y):
        que = deque()
        que.append((x,y))

        while que:
            x,y = que.popleft()
            for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)):
                sx = x + dx
                sy = y + dy
                if sx < 0 or sx >= W or sy < 0 or sy >= H:
                    continue
                if S[sy][sx] == '#':
                    continue
                if S[sy][sx] == '.':
                    S[sy][sx] = S[y][x]
                    que.appendleft((sx,sy))        
                else:
                    if S[sy][sx] > S[y][x]:
                        S[sy][sx] = S[y][x]
                        que.appendleft((sx,sy)) 
            for dx in range(-2,3):
                for dy in range(-2,3):
                    if (dx,dy) in ((-1,0),(1,0),(0,-1),(0,1),(0,0)):
                        continue
                    sx = x + dx
                    sy = y + dy
                    if sx < 0 or sx >= W or sy < 0 or sy >= H:
                        continue
                    if S[sy][sx] == '#':
                        continue
                    if S[sy][sx] == '.':
                        S[sy][sx] = S[y][x] + 1
                        que.append((sx,sy))
                    else:
                        if S[sy][sx] > S[y][x] + 1:
                            S[sy][sx] = S[y][x] + 1
                            que.append((sx,sy))     
    bfs(Cw-1,Ch-1)
    print(S[Dh-1][Dw-1] if S[Dh-1][Dw-1] != '.' else '-1')

if __name__ == "__main__":
    main()

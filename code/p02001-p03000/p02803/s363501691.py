import sys
import queue
def I(): return int(sys.stdin.readline())
def LI(): return [int(x) for x in sys.stdin.readline().split()]

d = [[-1,0],[1,0],[0,-1],[0,1]]

H,W = LI()
S = [list(input()) for _ in range(H)]

def bfs(s):
    dist = [[-1]*W for _ in range(H)]
    h,w = s
    dist[h][w] = 0
    que = queue.Queue()
    que.put(s)
    while(not(que.empty())):
        h,w = que.get_nowait()
        for dh,dw in d:
            nh,nw = h+dh,w+dw
            if 0<=nh<H and 0<=nw<W and dist[nh][nw]==-1 and S[nh][nw]=='.':
                dist[nh][nw] = dist[h][w] + 1
                que.put([nh,nw])
    return dist[h][w]

def main():
    ans = 0
    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                ans = max(ans,bfs([h,w]))
#                if (((h==0 or S[h-1][w]=='#') or (h==H-1 or S[h+1][w]=='#')) and 
#                        ((w==0 or S[h][w-1]=='#') or (w==W-1 or S[h][w+1]=='#'))):
#                    ans = max(ans,bfs([h,w]))
    print(ans)

if __name__ == "__main__":
    main()


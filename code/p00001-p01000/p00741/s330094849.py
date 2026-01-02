from collections import deque
def dfs(G,v,h,w):
    stack = deque([v])
    connected = set([v])
    while stack:
        u = stack.popleft()
        x,y = u
        dx = [-1,0,1]
        dy = [-1,0,1]
        for i in range(3):
            for j in range(3):
                s = x + dx[i]
                t = y + dy[j]
                if 0 <= s < h and 0 <= t < w:
                    if G[s][t] == 1:
                        if (s,t) not in connected:
                            stack.appendleft((s,t))
                            connected.add((s,t))
    return connected

def solve(C,h,w):
    node = set()
    ans = 0
    for i in range(h):
      for j in range(w):
        if C[i][j] == 1 and (i,j) not in node:
          node = node|dfs(C,(i,j),h,w)
          ans += 1
    print(ans)

def main():
    h = 0
    w = 0
    while h >= 0 and w >= 0:
        w,h = map(int,input().split(" "))
        if h == w == 0:
            return
        C = [list(map(int,input().split(" "))) for _ in range(h)]
        solve(C,h,w)
  

if __name__ == "__main__":
    main()

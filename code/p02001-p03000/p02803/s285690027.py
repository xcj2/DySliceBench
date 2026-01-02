import collections
INF = 10**9
    
def next(H,W,S,current):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        neighbor = (current[0]+dx[i],current[1]+dy[i])
        if 0 <= neighbor[0] < H and 0 <= neighbor[1] < W and S[neighbor[0]][neighbor[1]] == '.':
            yield neighbor

def bfs(start,H,W,S):
    q = collections.deque([start])
    v = 0
    visited = []
    layer = [[INF for i in range(W)] for j in range(H)]
    layer[start[0]][start[1]] = 0
    while q:
        c = q.popleft()
        if c in visited:
            continue
        visited.append(c)
        for neighbor in next(H,W,S,c):
            if neighbor not in visited:
                q.append(neighbor)
                layer[neighbor[0]][neighbor[1]] = layer[c[0]][c[1]]+1
                v = max(v,layer[neighbor[0]][neighbor[1]])
    #print(layer,start)
    return v

def main():
    H,W  = map(int, input().split())
    S = [[] for i in range(H)]
    route = 0
    for i in range(H):
        S[i]  = list(input())
    for i in range(H):
        for j in range(W):
            if S[i][j] == '.':
                start = (i,j)
                route = max(route,bfs(start,H,W,S))
    print(route)

if __name__ == '__main__':
    main()                

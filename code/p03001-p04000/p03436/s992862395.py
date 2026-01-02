import collections,itertools,sys
def S(): return sys.stdin.readline().rstrip()
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
H,W = LI()
s = [S() for _ in range(H)]
black_count = 0
for i,j in itertools.product(range(H),range(W)):
    if s[i][j]=='#':
        black_count += 1
dhdw = [[-1,0],[1,0],[0,-1],[0,1]]
min_dist = [[-1]*W for _ in range(H)]
seen = [[0]*W for _ in range(H)]
queue = collections.deque() #位置[行,列]を入れておく
def bfs():
    seen[0][0] = 1
    queue.append([0,0])
    min_dist[0][0] = 1
    while queue:
        qh,qw = queue.popleft()
        for dh,dw in dhdw:
            nh,nw = qh+dh,qw+dw
            if not(0<=nh<=H-1) or not(0<=nw<=W-1) or seen[nh][nw] or s[nh][nw]=='#':
                continue
            seen[nh][nw] = 1
            queue.append([nh,nw])
            min_dist[nh][nw] = min_dist[qh][qw]+1
bfs()
if min_dist[H-1][W-1]!=-1:
    print(H*W-black_count-min_dist[H-1][W-1])
else:
    print(-1)

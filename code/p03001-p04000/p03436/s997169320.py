import collections,itertools,sys
def S(): return sys.stdin.readline().rstrip()
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
h,w=LI()
s=[S() for _ in range(h)]
blackcount=0
for i,j in itertools.product(range(h),range(w)):
    if s[i][j]=="#":
        blackcount+=1
dhdw=[[-1,0],[1,0],[0,-1],[0,1]]
mindist=[[-1]*w for _ in range(h)]
seen=[[0]*w for _ in range(h)]
queue=collections.deque()
def bfs():
    seen[0][0]=1
    queue.append([0,0])
    mindist[0][0]=1
    while queue:
        qh,qw=queue.popleft()
        for dh,dw in dhdw:
            nh,nw=qh+dh,qw+dw
            if not(0<=nh<=h-1) or not(0<=nw<=w-1) or seen[nh][nw] or s[nh][nw]=="#":
                continue
            if [nh,nw]==[h-1,w-1]:
                return mindist[qh][qw]+1
            seen[nh][nw]=1
            queue.append([nh,nw])
            mindist[nh][nw]=mindist[qh][qw]+1
    else:
        return -1
mindist=bfs()
print(h*w-blackcount-mindist if mindist!=-1 else -1)
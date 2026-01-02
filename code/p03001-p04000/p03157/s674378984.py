# Mar 11, 12:14-
def inpl(): return list(map(int,input().split()))

H,W = inpl()
S = ''
for i in range(H):
    S += input()

N = H*W
parent = [-1]*N
white = [0]*N
black = [0]*N

def group(n):
    if parent[n] < 0:
        return n
    else:
        g = group(parent[n])
        parent[n] = g
        return g

def merge(m,n):
    gm = group(m)
    gn = group(n)
    if gm != gn:
        parent[gn] = gm
        white[gm] += white[gn]
        black[gm] += black[gn]
    return gm

def groupsize(n):
    g = group(n)
    return white[g]*black[g]

def place(n):
    return divmod(n,W)

def index(h,w):
    return h*W + w

for n in range(N):
    if S[n] == '.':
        white[n] = 1
    else:
        black[n] = 1

    h, w = place(n)
    if h > 0 and S[n] != S[n-W]:
        merge(n-W,n)
    if w > 0 and S[n] != S[n-1]:
        merge(n-1,n)    

groupset = set()
for n in range(N):
    groupset.add(group(n))

sizes = [ groupsize(p) for p in groupset ]
ans = sum(sizes)

print(ans)
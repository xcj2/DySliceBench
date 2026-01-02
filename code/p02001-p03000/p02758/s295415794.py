import sys

input=sys.stdin.readline

N=int(input())
robot=[]
for i in range(N):
    x,d=map(int,input().split())
    robot.append((x,d))
mod=998244353

robot.sort()
move=[i for i in range(0,N)]
for i in range(0,N):
    x,d=robot[i]
    start=i
    end=N-1
    while end-start>1:
        test=(end+start)//2
        if x+d>robot[test][0]:
            start=test
        else:
            end=test

    if x+d>robot[end][0]:
        move[i]=end
    else:
        move[i]=start


n=N
#####segfunc######
def segfunc(x,y):
    return max(x,y)

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2])

def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])

def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele =0

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

chain=[i for i in range(N)]
for _ in range(0,N):
    i=N-1-_
    if move[i]==i:
        chain[i]=i
        update(i,chain[i])
    else:
        chain[i]=query(i+1,move[i]+1)
        update(i,chain[i])

dp=[0 for i in range(0,N+1)]
dp[N]=1
for j in range(0,N):
    i=N-1-j
    if chain[i]==i:
        dp[i]=(2*dp[i+1])%mod
    else:
        dp[i]=(dp[i+1]+dp[chain[i]+1])%mod

print(dp[0])
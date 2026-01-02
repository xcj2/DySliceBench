import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from heapq import heappush, heappop

Q = int(readline())
query = (tuple(map(int,line.split())) for line in readlines())

# 適当に番兵を入れておく
INF = 10**12
L = [INF] # -1倍していれる
R = [INF]
SL = 0; SR = 0

def pushL(x):
    global SL
    heappush(L,-x)
    SL += x
def popL():
    global SL
    x = -heappop(L)
    SL -= x
    return x
def pushR(x):
    global SR
    heappush(R,x)
    SR += x
def popR():
    global SR
    x = heappop(R)
    SR -= x
    return x

add = 0 # 全体に共通に加わってるもの

answer = []
for q in query:
    if len(q) == 1:
        # 値を求める
        x = -L[0]
        f = SR - SL + x * (len(L)-len(R))
        answer.append('{} {}'.format(x,f+add))
        continue
    # 更新
    a,b = q[1:]
    add += b
    b = popL(); c = popR()
    a,b,c = sorted([a,b,c])
    pushL(a); pushR(c)
    if len(L) > len(R):
        pushR(b)
    else:
        pushL(b)

print('\n'.join(answer))
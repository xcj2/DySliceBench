import math
import sys
import os

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")


N,X,M = LI()

# ans = X
# for i in range(N-1):
#     X = X**2 % M
#     ans += X

# 訪れる順序、indexは移動回数
route = [X]
# 訪れた番号、高速検索用にhash tableを使う
visited = set([X])
next = X**2 % M

while True:
    if next in visited:
        loopStart = route.index(next)
        break
    else:
        route.append(next)
        visited.add(next)
        next = next**2 % M    

beforeLoop = route[:loopStart]
# print(beforeLoop)
loop = route[loopStart:]
# print(loop)

# loop前
if N < loopStart:
    ans = sum(beforeLoop[:N])
# loop後
else:
    numOfLoops,mod = divmod((N-(loopStart)),len(loop))
    # print(numOfLoops,mod)
    ans = sum(beforeLoop) + numOfLoops * sum(loop) + sum(loop[:mod])

print(ans)
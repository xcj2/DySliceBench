import math
import sys
import os
from operator import mul

sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(_S())
def LS(): return list(_S().split())
def LI(): return list(map(int,LS()))

if os.getenv("LOCAL"):
    inputFile = basename_without_ext = os.path.splitext(os.path.basename(__file__))[0]+'.txt'
    sys.stdin = open(inputFile, "r")
INF = float("inf")


_,k = LI()
a = LI()

a = list(map(lambda x:x-1,a))

# 訪れる順序、indexは移動回数
route = [0]
# 訪れた番号、高速検索用にhash tableを使う
visited = set([0])
next = a[0]

while True:
    if next in visited:
        loopStart = route.index(next)
        break
    else:
        route.append(next)
        visited.add(next)
        next = a[next]

# print(route)
# print(loopStart)

beforeLoop = route[:loopStart]
# print(beforeLoop)
loop = route[loopStart:]
# print(loop)

# loop前
if k < loopStart:
    ans = beforeLoop[k]
# loop後
else:
    numOfLoops,mod = divmod((k-(loopStart)),len(loop))
    # print(numOfLoops,mod)
    ans = loop[mod]

ans += 1
print(ans)
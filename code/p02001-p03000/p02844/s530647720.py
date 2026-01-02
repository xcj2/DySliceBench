import sys
import bisect
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
s = list(map(int, [i for i in S()]))

ID = [[] for _ in range(10)]
for i in range(N):
  ID[s[i]].append(i)

cnt = 0
for a in range(10):
  n1 = bisect.bisect_left(ID[a], 0)
  if n1 == len(ID[a]):
    continue
  for b in range(10):
    n2 = bisect.bisect_left(ID[b], ID[a][n1]+1)
    if n2 == len(ID[b]):
      continue
    for c in range(10):
      n3 = bisect.bisect_left(ID[c], ID[b][n2]+1)
      if n3 == len(ID[c]):
        continue
      cnt += 1
      #print(a,b,c)
print(cnt)
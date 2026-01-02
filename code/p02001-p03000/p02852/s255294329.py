import sys
import math
MAX_INT = int(10e15)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N, M = IL()
s = S()[::-1]

ans = []

now = 0
while True:
  if 0 <= now + M <= N:
    for num in range(1,M+1)[::-1]:
      if s[now + num] == "1":
        continue
      else:
        ans.append(num)
        now += num
        break
    else:
      print(-1)
      exit()
    continue
  else:
    if N - now == 0:
      pass
    else:
      ans.append(N - now)
    break

print(*ans[::-1])
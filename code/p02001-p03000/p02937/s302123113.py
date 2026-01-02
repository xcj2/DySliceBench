import sys
import bisect
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

s = S()
t = S()
N = len(s)

dic = {}

for i in range(N):
  if s[i] in dic:
    dic[s[i]].append(i+1)
  else:
    dic[s[i]] = [i+1]

tmp = 0
cnt = 0
for i in t:
  if i not in dic:
    print(-1)
    exit()
  else:
    l = dic[i]
    n = bisect.bisect_left(l,tmp)
    if n > len(l)-1:
      tmp = l[0]
      cnt += 1
    else:
      if tmp == l[n]:
        n += 1
        if n > len(l)-1:
          tmp = l[0]
          cnt += 1
        else:
          tmp = l[n]
      else:
        tmp = l[n]

print(cnt*N+tmp)

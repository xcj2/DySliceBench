import sys
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()

s = []
for i in range(N):
  tmp = [i for i in S()]
  tmp.sort()
  s.append(tmp)

t = s[0]
for i in range(1,N):
  tt = s[i]
  n = 0
  d = []
  for j in range(len(t)):
    for k in range(n, len(tt)):
      if t[j] == tt[k]:
        d.append(t[j])
        n = k + 1
        break
  else:
    t = d
t.sort()
print("".join(t))
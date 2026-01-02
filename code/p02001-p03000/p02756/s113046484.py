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

s = S()
q = I()
que = [S() for i in range(q)]
#print(que)

st = []
en = []
f = 0
for i in range(q):
  n = que[i]
  if n == "1":
    f += 1
  else:
    t,ff,c = list(n.split())
    if (f+int(ff))%2 == 0:
      st.append(c)
    else:
      en.append(c)

#print(st)
#print(en)

if f%2 == 0:
  print("".join(en[::-1]) + s + "".join(st))
else:
  print("".join(st[::-1]) + s[::-1] + "".join(en))

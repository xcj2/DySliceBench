import bisect
import sys
MAX_INT = int(10e12)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(index):
  if index == N:
    ans.append(-1)
    return
  num = a[index]
  if len(data[num]) == 1:
    ans.append(index)
    tami(index+1)
  elif index == data[num][-1]:
    ans.append(index)
    tami(data[num][0]+1)
  else:
    tmp = bisect.bisect_left(data[num],index)
    #print(num,data[num],tmp)
    tami(data[num][tmp+1]+1)

N,K = IL()
a = IL()

data = [[] for i in range(200010)]
ans = []

for i in range(N):
  data[a[i]].append(i)

#print(data)

tami(0)

#print(ans)
#print(len(ans),K)
#print(K%len(ans))

if K%len(ans) == 0:
  print()
else:
  x = ans[K%len(ans)-1]
  d = []
  d.append(a[x])
  while x != N-1:
    x += 1
    if len(data[a[x]]) == 1:
      d.append(a[x])
    elif x == data[a[x]][-1]:
      d.append(a[x])
    else:
      tmp = bisect.bisect_left(data[a[x]],x)
      x = data[a[x]][tmp+1]

  print(" ".join(map(str,d)))

"""
for i in range(K):
  for j in range(N):
    if a[j] in data:
      num = data.index(a[j])
      data = data[:num]
    else:
      data.append(a[j])
  print(data)

11 10
1 2 3 0 4 5 6 0 4 5 6

11 10
3 1 4 1 5 9 2 6 5 3 5

10 10
1 4 8 3 5 4 2 3 4 6
"""
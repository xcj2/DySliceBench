import sys
MAX_INT = int(10e9)
MIN_NUM = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
a = [IL()[::-1] for i in range(N)]

used = [-1]*N
updatelist = [i for i in range(N)]
total = N*(N-1)//2
cnt = 0
days = 0
ul = []
while updatelist:
  ul = []
  for i in updatelist:
    #print(a)
    #print(i+1)
    if len(a[i]) > 0 and used[i] != days:
      numIND = a[i][-1] -1
      #print(numIND+1)
      if a[numIND][-1] == i+1 and used[numIND] != days:
        a[i].pop(-1)
        a[numIND].pop(-1)
        used[i] = days
        used[numIND] = days
        ul.append(i)
        ul.append(numIND)
        cnt += 1
  else:
    updatelist = ul[:]
    if len(ul) != 0:
      days += 1
#print(a)
#print(cnt)
if cnt == total:
  print(days)
else:
  print(-1)
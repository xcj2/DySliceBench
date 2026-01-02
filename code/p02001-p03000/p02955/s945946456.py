import sys
import math
MAX_INT = int(10e9)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def judge(x):
  l = []
  for i in range(N):
    l.append(a[i]%x)
  l.sort()

  aa = 0
  bb = 0
  for i in l:
    tmp = i
    if aa + tmp > K:
      bb += x-tmp
      if bb > K:
        return False
    else:
      aa += tmp
  else:
    return True

N,K = IL()
a = IL()
num = sum(a)
ans = []

for i in range(1,int(math.sqrt(num)+1)):
  if num%i == 0:
    if judge(i):
      ans.append(i)
    if judge(num//i):
      ans.append(num//i)

print(max(ans))
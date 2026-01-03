import bisect,collections,copy,heapq,itertools,math,numpy,string
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def SS(): return map(str,sys.stdin.readline().rstrip().split())
def II(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

def div2count(n):
  cnt = 0
  while n % 2 == 0:
    cnt += 1
    n = n / 2
  return cnt

N = I()

ans = 1
ans_cnt = 0

for n in range(1,N+1):
  cnt = div2count(n)
  if ans_cnt < cnt:
    ans_cnt = cnt
    ans = n
print(ans)

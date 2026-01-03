import sys
import heapq
MAX_INT = int(10e10)
MIN_INT = -MAX_INT
mod = 1000000007
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

N = I()
s = S()
kakko = ["(", ")"]

cnt = 0
for i in range(N):
  if s[i] == kakko[0]:
    cnt += 1
  else:
    cnt = max(cnt-1, 0)
right = cnt

cnt = 0
for i in range(N-1,-1,-1):
  if s[i] == kakko[1]:
    cnt += 1
  else:
    cnt = max(cnt-1, 0)
left = cnt

print(kakko[0]*left + s + kakko[1]*right)
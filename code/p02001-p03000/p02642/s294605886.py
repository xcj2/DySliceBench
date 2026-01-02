import sys
input = sys.stdin.readline
import math
 
def INT(): return int(input())
def MAPINT(): return map(int, input().split())
def LMAPINT(): return list(map(int, input().split()))
def STR(): return input()
def MAPSTR(): return map(str, input().split())
def LMAPSTR(): return list(map(str, input().split()))
 
f_inf = float('inf')
 
n = INT()
a = sorted(LMAPINT())

length = (max(a) + 1)

ans = [0] * length
for x in a:
  # 重複
  if ans[x] != 0:
    ans[x] = 2
    continue
  for j in range(x, length, x):
    ans[j] += 1
 
count = 0
for x in a:
  if ans[x] == 1:
    count += 1
print(count)
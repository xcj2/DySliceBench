from collections import Counter
import sys
sys.setrecursionlimit(1000000)

global color 
global adlist

def make_adlist(N, AB):
  global adlist
  for a, b in AB:
    adlist[a] += [b]
    adlist[b] += [a]

def dfs(v, c):
  color[v] = c
  for u in adlist[v]:
    if color[u] == c:
      return False
    if color[u] == 0 and dfs(u, -c)==False:
      return False
  return True

def main():
  global color 
  global adlist
  N, M = map(int, input().split())
  AB = [list(map(lambda x:int(x)-1, input().split())) for _ in range(M)]
  color = [0 for _ in range(N)]
  adlist = [[] for _ in range(N)]
  make_adlist(N, AB)
  if dfs(0, 1):
    B = color.count(-1)
    W = color.count(1)
    print(B*W-M)
  else:
    print(N*(N-1)//2-M)

if __name__ == "__main__":
  main()


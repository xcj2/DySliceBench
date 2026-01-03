import sys
sys.setrecursionlimit(1000000)
def main():
  n, m = map(int, input().split())
  ab = [list(map(lambda x:int(x)-1, input().split())) for _ in range(m)]
  ad_list = make_ad_list(n, ab)
  global searched
  global ans
  searched = [0 for _ in range(n)]
  searched[0] = 1
  ans = 0
  dfs(0, n, ad_list)
  print(ans)

def make_ad_list(n, l):
  ad_list = [[] for _ in range(n)]
  for a, b in l:
    ad_list[a] += [b]
    ad_list[b] += [a]

  return ad_list

def dfs(v, n, ad_list):
  global searched
  global ans
  if sum(searched) == n:
    ans += 1
    return
  for u in ad_list[v]:
    if searched[u] == 0:
      searched[u] = 1
      dfs(u, n, ad_list)
      searched[u] = 0
  return 

if __name__ == "__main__":
  main()

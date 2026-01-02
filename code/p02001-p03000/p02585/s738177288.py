#!/usr/bin/python3
# -*- coding:utf-8 -*-


def main():
  n, k = map(int, input().strip().split())
  lp = list(map(lambda p:int(p)-1, input().strip().split()))
  lc = list(map(int, input().strip().split()))

  used = [0] * n
  loops = []
  for i in range(n):
    if used[i] == 1:
      continue
      
    ic = i
    loop = []
    while used[ic] == 0:
      loop.append(lc[ic])
      used[ic] = 1      
      ic = lp[ic]
      
    if len(loop) > 0:
      loops.append(loop)
    
  def loop_score(loop, k):
    return (k // len(loop)) * sum(loop)
  
  def path_score(loop, k):
    score = 0
    for i in range(len(loop)):
      cumsum = 0
      for j in range(k):
        cumsum += loop[(i+j) % len(loop)]
        score = max(score, cumsum)
    return score
  
  def calc_score(loop, k):
    if max(loop) < 0:
      return max(loop)
    
    if k < len(loop):
      return path_score(loop, k)
    if k >= len(loop):
      k -= len(loop)
      score = 0
      if sum(loop) > 0:
        score += loop_score(loop, k)
      k %= len(loop)
      k += len(loop)
      score += path_score(loop, k)

    return score
  
  print(max([calc_score(loop, k) for loop in loops]))

if __name__=='__main__':
  main()


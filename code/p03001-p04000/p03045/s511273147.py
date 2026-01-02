#!/usr/bin/python3
# -*- coding:utf-8 -*-

import sys
sys.setrecursionlimit(10**5)

def main():
  n, m = map(int, input().split())
  luf = [-1] * (n+1)
  
  def find(x):
    if luf[x] < 0:
      return x
    else:
      luf[x] = find(luf[x])
      return luf[x]
  
  def union(x, y):
    px, py = find(x), find(y)
    if px == py:
      return
    if px < py:
      px, py = py, px
    luf[px] += luf[py]
    luf[py] = px
  
  for _ in range(m):
    x, y, z = map(int, input().split())
    union(x, y)
#   print(luf)
  print(sum([x<0 for x in luf[1:]]))

if __name__=='__main__':
  main()


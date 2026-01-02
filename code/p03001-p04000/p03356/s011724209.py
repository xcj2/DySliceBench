#!/usr/bin/python3
# -*- coding:utf-8 -*-

def main():
  n, m = map(int, input().split())
  lp = list(map(int, input().split()))
  
  luf = [-1] * (n)
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
    x, y = map(int, input().split())
    union(x-1, y-1)
  
  dic = dict()
  for i, p in enumerate(lp):
    p -= 1
    pp = find(p)
    if pp in dic:
      dic[pp]['inds'] |= set([i])
      dic[pp]['vals'] |= set([p])
    else:
      dic[pp] = dict()
      dic[pp]['inds'] = set([i])
      dic[pp]['vals'] = set([p])
  print(sum([len(v['inds'] & v['vals']) for _, v in dic.items()]))
    

if __name__=='__main__':
  main()


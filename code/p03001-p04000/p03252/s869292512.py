import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  s=S()
  t=S()

  # a〜z
  l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

  l1=['']*26
  l2=['']*26

  for i in range(len(s)):
    if l1[l.index(s[i])]!='':
      if l1[l.index(s[i])]!=t[i]:
        return 'No'
    else:
      l1[l.index(s[i])]=t[i]

  for i in range(len(s)):
    if l2[l.index(t[i])]!='':
      if l2[l.index(t[i])]!=s[i]:
        return 'No'
    else:
      l2[l.index(t[i])]=s[i]

  return 'Yes'

print(main())

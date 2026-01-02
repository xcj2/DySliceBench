import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():

  # a〜z
  l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

  l2=[list() for i in range(26)]
  l3=[list() for i in range(26)]

  s=S()
  t=S()

  for i in range(len(s)):
    if len(l2[l.index(s[i])])>0:
      if l2[l.index(s[i])][0]!=t[i]:
        return 'No'
    else:
      l2[l.index(s[i])].append(t[i])
    if len(l3[l.index(t[i])])>0:
      if l3[l.index(t[i])][0]!=s[i]:
        return 'No'
    else:
      l3[l.index(t[i])].append(s[i])

  return 'Yes'

print(main())

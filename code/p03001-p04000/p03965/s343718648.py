import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# 方針
# なるべくパーを出した方がいい
# len(s)の半分をパーにすれば条件は満たされる
# あとはポイントを計算する
# （自分のパーの数） - （相手のパーの数）

def main():
  s=S()

  g=s.count('g')
  p=len(s)-g

  myp=len(s)//2
  myg=len(s)-myp

  return myp-p

print(main())

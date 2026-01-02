import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

# 方針
# 前から順に-1していく
# その際、常に前の数を見ておき、0になった場合一区切り
# カウンターを+1する
# また、最後の項に達したときも+1
# インデックスは先頭に戻して
# 全ての項が0になるまで繰り返す
# （全部0になったことを確認するため、初めにsumを取って
# 引き算するたびにsumも-1していき、0になったらループ脱出）

def main():
  n=I()
  l=LI()

  sm=sum(l)

  i=0
  c=0
  while True:

    # print(l)
    # print(c)

    if l[i]!=0:
      l[i]-=1
      sm-=1

      if i==n-1 or l[i+1]==0:
        c+=1

    i+=1
    if i>=n:
      i=0

      if sm==0:
        break

  return c

print(main())

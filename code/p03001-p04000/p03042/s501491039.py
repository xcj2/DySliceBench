import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def II(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  s=S()
  a=s[:2]
  b=s[2:]
  if a=='00' and int(b)>12:
    print('NA')
  elif int(a)>12 and b=='00':
    print('NA')
  elif a=='00' and b=='00':
    print('NA')
  elif a=='00' and int(b)<=12:
    print('YYMM')
  elif int(a)<=12 and b=='00':
    print('MMYY')
  elif int(a)>12 and int(b)>12:
    print('NA')
  elif int(a)<=12 and int(b)>12:
    print('MMYY')
  elif int(a)>12 and int(b)<=12:
    print('YYMM')
  else:
    print('AMBIGUOUS')

main()
# print(main())

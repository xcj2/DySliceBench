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

  if len(s)<5:
    print('NO')
  else:
    if s[-4:]=='BARA':
      if s.count('A')>4:
        print('NO')
      elif s.count('A')==4:
        if s=='AKIHABARA':
          print('YES')
        else:
          print('NO')
      else:
        if s.count('KIH')==1:
          print('YES')
        else:
          print('NO')

    elif s[-3:]=='BRA' or s[-3:]=='BAR':
      if s.count('A')>3:
        print('NO')
      elif s.count('A')==3:
        if s=='AKIHABRA' or s=='AKIHABAR':
          print('YES')
        else:
          print('NO')
      else:
        if s.count('KIH')==1:
          print('YES')
        else:
          print('NO')

    elif s[-2:]=='BR':
      if s.count('A')>2:
        print('NO')
      elif s.count('A')==2:
        if s=='AKIHABR':
          print('YES')
        else:
          print('NO')
      else:
        if s.count('KIH')==1:
          print('YES')
        else:
          print('NO')
    else:
      print('NO')

main()

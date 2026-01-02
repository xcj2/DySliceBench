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
  t=S()

  for i in range(len(s)-len(t)+1)[::-1]:
    x=s[i:i+len(t)]
    f=True
    for j in range(len(t)):
      if x[j]==t[j] or x[j]=='?':
        pass
      else:
        f=False

    if f:
      # 後ろから合致する場所は置き換え
      # 残りの '?' 部は 'a' に置き換え
      print(str(s[:i]+t+s[i+len(t):]).replace('?','a'))
      exit()

  print('UNRESTORABLE')

main()
# print(main())

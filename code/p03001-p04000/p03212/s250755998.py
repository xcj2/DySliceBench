import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7

def LI(): return list(map(int,input().split()))
def I(): return int(input())
def LS(): return input().split()
def S(): return input()

def main():
  n=I()

  cnt=0
  for j in range(-1,3):
    for b in range(-1,3):
      for c in range(-1,3):
        for d in range(-1,3):
          for e in range(-1,3):
            for f in range(-1,3):
              for g in range(-1,3):
                for h in range(-1,3):
                  for i in range(-1,3):
                    a=0

                    if i==0:
                      a+=3
                    elif i==1:
                      a+=5
                    elif i==2:
                      a+=7

                    if h==0:
                      a+=30
                    elif h==1:
                      a+=50
                    elif h==2:
                      a+=70

                    if g==0:
                      a+=300
                    elif g==1:
                      a+=500
                    elif g==2:
                      a+=700

                    if f==0:
                      a+=3000
                    elif f==1:
                      a+=5000
                    elif f==2:
                      a+=7000

                    if e==0:
                      a+=30000
                    elif e==1:
                      a+=50000
                    elif e==2:
                      a+=70000

                    if d==0:
                      a+=300000
                    elif d==1:
                      a+=500000
                    elif d==2:
                      a+=700000

                    if c==0:
                      a+=3000000
                    elif c==1:
                      a+=5000000
                    elif c==2:
                      a+=7000000

                    if b==0:
                      a+=30000000
                    elif b==1:
                      a+=50000000
                    elif b==2:
                      a+=70000000

                    if j==0:
                      a+=300000000
                    elif j==1:
                      a+=500000000
                    elif j==2:
                      a+=700000000

                    if a>n:
                      return cnt
                    else:
                      x=list(set(str(a)))
                      if x.count('0')>0:
                        continue
                      if len(x)==3:
                        cnt+=1
  
  return cnt

print(main())

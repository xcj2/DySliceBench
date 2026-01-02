import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
# def LF(): return [float(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  n=I()
  ho={}
  if n%2==0:
    for i in range(1,n//2+1):
      ho[str(i)+'-'+str(n-i+1)]=0
  else:
    for i in range(1,n//2+1):
      ho[str(i)+'-'+str(n-i)]=0

  # print(ho)

  ans=[]
  for i in range(1,n+1):
    for j in range(1,n+1):
      if i<=j:
        break

      pair=str(j)+'-'+str(i)
      if pair in ho:
        continue

      ans.append((j,i))

  print(len(ans))
  for x,y in ans:
    print(x,y)

main()
# print(main())

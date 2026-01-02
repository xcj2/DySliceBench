import math,itertools,fractions,heapq,collections,bisect,sys,queue,copy

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

def main():
  l=[LI() for _ in range(3)]
  n=I()
  ans=[[0]*3 for _ in range(3)]

  for i in range(n):
    a=I()
    for j in range(3):
      for k in range(3):
        if l[j][k]==a:
          ans[j][k]=1

  for i in range(3):
    if ans[i][0]==1 and ans[i][1]==1 and ans[i][2]==1:
      return 'Yes'

  for i in range(3):
    if ans[0][i]==1 and ans[1][i]==1 and ans[2][i]==1:
      return 'Yes'

  if ans[0][0]==1 and ans[1][1]==1 and ans[2][2]==1:
    return 'Yes'

  if ans[0][2]==1 and ans[1][1]==1 and ans[0][2]==1:
    return 'Yes'

  return 'No'

# main()
print(main())

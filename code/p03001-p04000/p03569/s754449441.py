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
  s=S()
  i_f=0
  i_b=len(s)-1

  ans=0
  while True:
    if i_f>=i_b:
      return ans

    # print(i_f,i_b)
    if s[i_f]==s[i_b]:
      i_f+=1
      i_b-=1
    else:
      if s[i_f]=='x':
        i_f+=1
        ans+=1
      elif s[i_b]=='x':
        i_b-=1
        ans+=1
      else:
        return -1

# main()
print(main())

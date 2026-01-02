import sys,collections

sys.setrecursionlimit(10**7)
inf=10**20
mod=10**9+7
dd=[(-1,0),(0,1),(1,0),(0,-1)]
ddn=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS(): return sys.stdin.readline().split()
def S(): return input()

# Summarize count of factor within list -- START --
def summarize_list(l):
  sl=sorted(l)

  a=sl[0]
  c=1
  res=[]

  for x in sl[1:]:
    if x==a:
      c+=1
    else:
      res.append([a,c])
      a=x
      c=1
  res.append([a,c])

  return res
# Summarize count of factor within list --- END ---

def main():
  n=I()
  l=[S() for _ in range(n)]

  l=summarize_list(l)

  l=sorted(l,key=lambda x:x[0])
  l=sorted(l,key=lambda x:x[1],reverse=True)

  a=l[0][1]
  print(l[0][0])

  for x,y in l[1:]:
    if y!=a:
      break
    else:
      print(x)

main()
# print(main())

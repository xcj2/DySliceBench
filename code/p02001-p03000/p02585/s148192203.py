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
  N,K=LI()
  P=LI()
  P=[0]+P
  C=LI()
  C=[0]+C

  l=[[0] for _ in range(N)]
  check=[[False]*(N+1) for _ in range(N)]
  roop=[]
  for i in range(N):
    zahyo=i+1
    check[i][zahyo]=True
    f=False
    for j in range(N+1):
      zahyo=P[zahyo]
      if check[i][zahyo] and not f:
        roop.append(j+1)
        f=True
      score=C[zahyo]
      l[i].append(l[i][-1]+score)
  # for i in range(N):
  #   print(l[i])
  # print(roop)

  ans=-inf
  for i in range(N):
    roop_count=roop[i]
    if K<=roop_count:
      ans=max(ans,max(l[i][1:K+1])) # 1巡以内
    else:
      ans=max(ans,max(l[i][1:K+1])) # 1巡以内

      # 2巡目以降（1巡で負になるなら回らない方がいい）
      if l[i][roop_count]>0:
        c=K//roop_count
        _ans1=c*l[i][roop_count]
        k=K%roop_count
        _ans1+=max(l[i][1:k+1]+[0])
        ans=max(ans,_ans1)

        # 可能な巡数まで行かない方がいい場合も
        _ans2=(c-1)*l[i][roop_count]
        _ans2+=max(l[i][:roop_count]+[0])
        ans=max(ans,_ans1,_ans2)

  return ans

# main()
print(main())

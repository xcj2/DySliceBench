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

def main():
  # a1>a2<a3>a4...
  # a1-a2+a3-a2+a3-a4...
  # a1+2a3-2a2-2a4+...+an? -an?

  # 偶数なら例えば4: a1-2a2+2a3-a4
  # 奇数なら例えば3: a1-2a2+a3

  # 割り当て：2の係数がついて正の数は大きいやつを優先して
  # 2の係数がついて負の数は小さいやつを優先

  # 逆の場合は
  # a4-2a3+2a2-a1
  # -a3+2a2-a1

  n=I()
  l=[I() for _ in range(n)]

  l.sort()

  i1=0
  i2=n-1

  ans=0
  if n%2==0:
    for i in range((n-2)//2):
      ans+=l[i2]*2
      i2-=1
      ans-=l[i1]*2
      i1+=1

    ans+=l[i2]
    ans-=l[i1]

  else:
    for i in range((n-2)//2):
      ans+=l[i2]*2
      i2-=1
      ans-=l[i1]*2
      i1+=1

    ans-=l[i1]*2
    i1+=1

    ans+=l[i2]
    ans+=l[i1]

  ans1=ans
  ans=0
  i1=0
  i2=n-1
  if n%2==0:
    for i in range((n-2)//2):
      ans+=l[i2]*2
      i2-=1
      ans-=l[i1]*2
      i1+=1

    ans+=l[i2]
    ans-=l[i1]

  else:
    # print(i1,i2,l)
    for i in range((n-2)//2):
      ans+=l[i2]*2
      i2-=1
      ans-=l[i1]*2
      i1+=1

    ans+=l[i2]*2
    i2-=1

    ans-=l[i2]
    ans-=l[i1]

  ans2=ans
  return max(ans1,ans2)

# main()
print(main())

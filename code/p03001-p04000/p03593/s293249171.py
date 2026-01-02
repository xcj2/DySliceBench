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

# a〜z -- START --
alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# a〜z --- END ---

def main():
  h,w=LI()
  l=[0]*len(alf)

  for _ in range(h):
    a=S()
    for x in a:
      l[alf.index(x)]+=1

  count4=count2=count1=0
  for i in range(len(alf)):
    count4+=l[i]//4
    l[i]%=4
    count2+=l[i]//2
    l[i]%=2
    count1+=l[i]

  # print(count1,count2,count4)

  if h%2==1 and w%2==1:
    if count1!=1:
      return 'No'

    x=count4-(h-1)*(w-1)//4
    if x<0:
      return 'No'
    count2+=x*2

    if count2!=w//2+h//2:
      return 'No'

    return 'Yes'
  elif h%2==1 and w%2==0:
    if count1!=0:
      return 'No'

    x=count4-(h-1)*w//4
    if x<0:
      return 'No'
    count2+=x*2

    if count2!=w//2:
      return 'No'

    return 'Yes'
  elif h%2==0 and w%2==1:
    if count1!=0:
      return 'No'

    x=count4-h*(w-1)//4
    if x<0:
      return 'No'
    count2+=x*2

    if count2!=h//2:
      return 'No'

    return 'Yes'
  elif h%2==0 and w%2==0:
    if count1!=0:
      return 'No'

    x=count4-h*w//4
    if x<0:
      return 'No'
    count2+=x*2

    if count2!=0:
      return 'No'

    return 'Yes'

# main()
print(main())

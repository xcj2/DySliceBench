import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

N, X = LI()

def solve():
  
  lenl = [0 for i in range(N+1)]
  for i in range(N+1):
    if i == 0:
      lenl[i] = 1
    else:
      lenl[i] = 2 * lenl[i-1] + 3
  
  npl = [0 for i in range(N+1)]
  for i in range(N+1):
    if i == 0:
      npl[i] = 1
    else:
      npl[i] = 2 * npl[i-1] + 1

  def np(l, x):
    if x <= 0:
      return 0
    if l == 0:
      return 1
    
    if x < lenl[l] // 2:
      return np(l-1, x-1)
    elif x == lenl[l] // 2:
      return npl[l-1]
    elif x == (lenl[l] // 2) + 1:
      return npl[l-1] + 1
    else:
      return npl[l-1] + 1 + np(l-1, x-(lenl[l]//2)-1)
  
  print(np(N, X))
solve()
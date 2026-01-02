import sys
sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline    ####
int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

INF = float('inf')

from collections import Counter

def solve():
    n = II()
    V = LI()
    
    even = V[::2]
    odd = V[1::2]
    harf = n // 2
    
    ec = Counter(even).most_common()
    oc = Counter(odd).most_common()
    #print(n)
    #print(ec[:3])
    #print(oc[:3])
    e1 = ec[0][1]
    o1 = oc[0][1]
    
    if ec[0][0] == oc[0][0]:
      # 小さい方を変える
      e2 = ec[1][1] if len(ec) > 1 else 0
      o2 = oc[1][1] if len(oc) > 1 else 0
      
      ans = min(n - e1 - o2, n - o1 - e2)
    else:
      ans = n - e1 - o1
    
    print(ans)


if __name__ == '__main__':
    solve()

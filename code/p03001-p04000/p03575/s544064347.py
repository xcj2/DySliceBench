import math
import bisect
import collections
import itertools
import sys
sys.setrecursionlimit(100000000)
def gcd(a,b):return math.gcd #最大公約数
def lcm(a,b):return (a*b) // math.gcd(a,b) #最小公倍数
def iin(): return int(input()) #整数読み込み
def imn(): return map(int, input().split()) #整数map取得
def iln(): return list(map(int, input().split())) #整数リスト取得
def iln_s(): return sorted(iln()) # 昇順の整数リスト取得
def iln_r(): return sorted(iln(), reverse=True) # 降順の整数リスト取得
def join(l, s=''): return s.join(l) #リストを文字列に変換
def perm(l, n): return itertools.permutations(l, n) # 順列取得
def comb(l, n): return itertools.combinations(l, n) # 組み合わせ取得
def divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i: divisors.append(n//i)
    return divisors
def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False 
    return True

N,M=imn()
a = []
b = []
visited = [False for _ in range(N)]
graph = [[False for _ in range(50)] for _ in range(50)]
    
for i in range(M):
    v1,v2 = map(lambda x:int(x)-1, input().split())
    a.append(v1)
    b.append(v2)
    graph[v1][v2] = graph[v2][v1] = True

def dfs(v):
    visited[v] = True
    #print(graph[v])
    for v2 in range(N):
        if graph[v][v2] == False: continue
        if visited[v2]: continue
        dfs(v2)

ans = 0

for i in range(M):
    v1 = a[i]
    v2 = b[i]
    graph[v1][v2] = graph[v2][v1] = False
    
    for i in range(N): visited[i] = False

    dfs(0)
    
    for j in range(N):
        if visited[j] == False:
            ans += 1
            break

    graph[v1][v2] = graph[v2][v1] = True

print(ans)
import sys
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def ti(): return tuple(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

from functools import reduce

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r == 0:
        return b
    return gcd(b, r)

def lcm(a):
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x

def table(n:int, p=10**9+7):
    global fact, factinv, inv
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n+1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)

def main():
    N = ii()
    A = ti()
    P = 10**9 + 7
    lcm_a = lcm(A) % P

    N = 10**6+1
    inv_t = [0]+[1]
    for i in range(2,N):
        inv_t += [inv_t[P % i] * (P - int(P / i)) % P]

    #print(inv_t[:10])
    ans = 0
    for num in A:
        ans = (ans + inv_t[num] * lcm_a) % P
        #ans +=  (ans + lcm_a // num) % P
        #ans %= inf
    print(ans)

if __name__ == "__main__":
    main()
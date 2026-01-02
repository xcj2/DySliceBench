import sys
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*2, n+1, i):
                is_prime[j] = False
    return [i for i in range(n+1) if is_prime[i]]

def resolve():
    Q = I()
    lr = [LI() for _ in range(Q)]

    r_max = max([i[1] for i in lr])
    primes = set(sieve(r_max))

    acc = [0]*(r_max+2)
    for i in range(r_max+1):
        if i in primes and (i+1)//2 in primes:
            acc[i+1] = acc[i] + 1
        else:
            acc[i+1] = acc[i]

    for i in lr:
        print(acc[i[1]+1]-acc[i[0]])

if __name__ == '__main__':
    resolve()
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

class Sieve:
    def __init__(self, n):
        self.plist = [2]  # n以下の素数のリスト
        min_prime_factor = [2, 0] * (n // 2 + 5)
        for x in range(3, n + 1, 2):
            if min_prime_factor[x] == 0:
                min_prime_factor[x] = x
                self.plist.append(x)
                if x ** 2 > n: continue
                for y in range(x ** 2, n + 5, 2 * x):
                    if min_prime_factor[y] == 0:
                        min_prime_factor[y] = x
        self.min_prime_factor = min_prime_factor

    def isprime(self, x):
        return self.min_prime_factor[x] == x

    # これが素因数分解(prime factorization)
    def pfct(self, x):
        pp, ee = [], []
        while x > 1:
            mpf = self.min_prime_factor[x]
            if pp and mpf == pp[-1]:
                ee[-1] += 1
            else:
                pp.append(mpf)
                ee.append(1)
            x //= mpf
        return [(p, e) for p, e in zip(pp, ee)]

def main():
    md=10**9+7
    sv=Sieve(1005)
    cnt_e=[0]*1005
    for a in range(2,II()+1):
        pe=sv.pfct(a)
        for p,e in pe:cnt_e[p]+=e
    ans=1
    for e in cnt_e:ans=ans*(e+1)%md
    print(ans)

main()
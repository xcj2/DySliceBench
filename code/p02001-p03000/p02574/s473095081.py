from sys import stdin, setrecursionlimit
input = stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))

max_A = max(A)
if max_A == 1:
    print("pairwise coprime")
    exit()

class Prime:
    def __init__(self, n):
        self.prime_factor = [i for i in range(n + 1)]
        self.prime = []
        for i in range(2, n + 1):
            if self.prime_factor[i] == i:
                for j in range(2, n // i + 1):
                    self.prime_factor[i * j] = i
                self.prime.append(i)
        #print(self.prime_factor)
        #print(self.prime)
    def factorize(self, m):
        ret = []
        while m != 1:
            if not ret:
                ret = [[self.prime_factor[m], 1]]
            elif self.prime_factor[m] == ret[-1][0]:
                ret[-1][1] += 1
            else:
                ret.append([self.prime_factor[m], 1])
            m //= self.prime_factor[m]
        return ret
    def divisors(self, m):
        ret = []
        for i in range(1, int(m ** 0.5) + 1):
            if m % i == 0:
                ret.append(i)
                if i != m // i:
                    ret.append(m // i)
        #self.divisors.sort()
        return ret
pm = Prime(max_A)

def is_pairwise_coprime(arr):
    cnt = [0] * (max_A + 1)
    for a in arr:
        for b, c in pm.factorize(a):
            cnt[b] += 1
    if max(cnt[2:]) <= 1:
        return 1
    else:
        return 0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_setwise_coprime(A):
    gcd_a = 0
    for a in A:
        gcd_a = gcd(gcd_a, a)
    if gcd_a == 1:
        return 1
    else:
        return 0

if is_pairwise_coprime(A):
    print("pairwise coprime")
elif is_setwise_coprime(A):
    print("setwise coprime")
else:
    print("not coprime")
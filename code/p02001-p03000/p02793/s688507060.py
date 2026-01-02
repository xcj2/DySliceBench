import sys
from collections import Counter
import time

class Osa_k:
    def __init__(self, n):
        self.n = n
        self.min_factor = [int(x) for x in range(n+1)]
        
        self.is_prime = [True] * (self.n + 1)
        self.is_prime[0] = False
        self.is_prime[1] = False
        for j in range(4, self.n+1, 2):
            self.is_prime[j] = False
            self.min_factor[j] = 2
        for i in range(3, int(self.n**0.5) + 1, 2):
            if not self.is_prime[i]:
                continue
            for j in range(i * 2, self.n + 1, i):
                self.is_prime[j] = False
                if self.min_factor[j] >= i:
                	self.min_factor[j] = i
        


    def calculate(self, x):
        ans = []
        while x > 1:
            key = self.min_factor[x]
            while x%key == 0:
                ans.append(key)
                x //= key
        counter = Counter(ans)
        return counter

def main():
    input = sys.stdin.readline
    mod = pow(10,9)+7
    n = int(input())
    a = [int(x) for x in input().split()]
    prime_list = dict()
    osa_k = Osa_k(max(a))
    for i in range(n):
        primes = osa_k.calculate(a[i])
        for key, value in primes.items():
            if key in prime_list:
                if prime_list[key] < value:
                    prime_list[key] = value
            else:
                prime_list[key] = value
              
    L = 1
    for key, value in prime_list.items():
        L *= pow(key, value, mod)
        L %= mod
        
    ans = 0
    for i in range(n):
        ans += (L*pow(a[i], mod-2, mod))%mod
        ans %= mod
    print(ans)

    

if __name__ == "__main__":
    main()
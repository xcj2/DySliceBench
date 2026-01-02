import sys
import math
input = sys.stdin.readline

from collections import Counter

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
    
    def calulate(self, x):
        ans = []
        while x > 1:
            key = self.min_factor[x]
            while x%key == 0:
                ans.append(key)
                x //= key
        counter = set(ans)
        return counter
        

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    key = a[0]
    sc = False
    for i in range(1, n):
        key = math.gcd(key, a[i])
    
    if key == 1:
        sc = True
    
    
    pc = True
    osak = Osa_k(10**6+1)
    
    sub = set()
    
    judge = dict()
    for i in range(n):
        key = osak.calulate(a[i])
        for v in key:
            if v in judge:
                pc = False
            judge[v] = 1
            
    
    if pc:
        print("pairwise coprime")
    elif sc:
        print("setwise coprime")
    else:
        print("not coprime")

    
    
    
    
    
if __name__ == "__main__":
    main()


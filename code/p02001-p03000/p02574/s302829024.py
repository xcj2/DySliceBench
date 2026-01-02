class Prime():
    def __init__(self, n):
        self.p = []
        self.d = [0] * n

        for i in range(2, n):
            if self.d[i] == 0:
                self.p.append(i)
                for j in range(i, n, i):
                    if self.d[j] == 0:
                        self.d[j] = i

        self.ind = [-1] * n
        for i in range(len(self.p)):
            self.ind[self.p[i]] = i

    def prime_factorization_index(self, x):
        l = []
        while x != 1:
            if l == [] or l[-1] != self.ind[self.d[x]]:
                l.append(self.ind[self.d[x]])
            x //= self.d[x]
        return l

    def num_prime(self):
        return len(self.p)

from math import gcd
 
n = int(input())
a = list(map(int, input().split()))
 
g = a[0]
for i in range(1, n):
    g = gcd(g, a[i])
    if g == 1:
        break
else:
    print('not coprime')
    exit()

p = Prime(10**6 + 1)

tf = [False] * p.num_prime()

for i in range(1, n):
    l = p.prime_factorization_index(a[i])
    for i in l:
        if tf[i]:
            print('setwise coprime')
            exit()
        else:
            tf[i] = True

print('pairwise coprime')
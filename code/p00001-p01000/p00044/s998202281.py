def create_prime(n):
    prime = [1] * (n + 1)
    prime[:2] = [0, 0]
    for i in range(len(prime)):
        if prime[i]:
            for j in range(2 * i, len(prime), i):
                prime[j] = 0
    return prime

def under(prime, n):
    for i in range(n - 1, -1, -1):
        if prime[i]:
            return i
def over(prime, n):
    for i in range(n + 1, len(prime)):
        if prime[i]:
            return i
import sys
n = [int(line) for line in sys.stdin]

prime = create_prime(max(n) + 100)

for ni in n:
    print(under(prime, ni), over(prime, ni))
import sys
import math
def input(): return sys.stdin.readline().rstrip()

def isPrime(n):
    m = (n + 1) // 2
    n_sqrt = int(math.sqrt(n))
    for i in range(2, n_sqrt + 1):
        if n % i == 0 or m % i == 0:
            return 0
    else:
        return 1

def main():
    Q = int(input())

    MAX = 10 ** 5
    prime = [0] * MAX
    for i in range(3, MAX):
        prime[i] = prime[i-1] + isPrime(i)

    for _ in range(Q):
        l, r = map(int, input().split())
        print(prime[r] - prime[l-1])
if __name__ == '__main__':
    main()
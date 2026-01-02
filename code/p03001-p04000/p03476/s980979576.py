import sys
import math
def input(): return sys.stdin.readline().rstrip()

def isPrime(n):
    if n <= 2:
        return 0

    m = (n + 1) // 2
    n_sqrt = int(math.sqrt(n))
    for i in range(2, n_sqrt + 1):
        if n % i == 0 or m % i == 0:
            return 0
    else:
        return 1

def main():
    Q = int(input())
    lr = [tuple(map(int, input().split())) for _ in range(Q)]

    MAX = 10 ** 5
    prime = [0] * MAX
    for i in range(1, MAX):
        prime[i] = prime[i-1] + isPrime(i)
    for i in lr:
        l, r = i
        if prime[l] != prime[l-1]:
            print(prime[r] - prime[l]+1)
        else:
            print(prime[r] - prime[l])
if __name__ == '__main__':
    main()
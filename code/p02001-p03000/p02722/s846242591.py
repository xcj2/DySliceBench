from math import sqrt
import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def is_ok(n, k):
    while n % k == 0:
        n //= k
    if n < k:
        return n == 1
    else:
        return n % k == 1


def prime_enumeration(n):
    div = []
    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            if i != 1:
                div.append(i)
            if n // i != i:
                div.append(n // i)

    #div.sort()
    return div


def main():
    N = int(readline())

    div_n = prime_enumeration(N)
    div_n1 = prime_enumeration(N-1)
    #print(div_n)
    #print(div_n1)

    ans = 0
    for d in div_n:
        if is_ok(N, d):
            ans += 1
    
    for d in div_n1:
        if is_ok(N, d):
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()

# import sys
# input = sys.stdin.readline
# import re
import itertools

def main():
    n = int(input())
    a = n % 1000
    if a > 0:
        print(1000 - a)
        exit()
    print(a)

def count_tento(l, cur):
    count = 0
    for v in l:
        if v > cur:
            count += 1
    return count

def input_list():
    return list(map(int, input().split()))

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

if __name__ == '__main__':
    main()


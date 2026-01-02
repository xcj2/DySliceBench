# import sys
# input = sys.stdin.readline
# import re
# import itertools
import collections

def main():
    n = int(input())
    s = input_list()
    sc = collections.Counter(s)
    q = int(input())
    data = []
    for i in range(q):
        b, c = input_list()
        sc[c] += sc[b]
        if i > 0:
            data.append(c*sc[b] - b * sc[b])
        if b in sc:
            sc.pop(b)
    ans = 0
    for k, v in sc.items():
        ans += k*v
    aa = [ans]
    for i, v in enumerate(data[::-1]):
        aa.append(aa[i] - v)
    for a in aa[::-1]:
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

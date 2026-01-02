import sys
from math import gcd


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return map(int, stdin.readline().split())
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n = ni()
    A = nl()
    c = A[0]
    b = []

    cnt = [0] * (10 ** 6 + 1)

    for a in A:
        c = gcd(c, a)
        cnt[a] += 1

    max_num = 0
    for i in range(2, 10 ** 6 + 1):
        max_num = max(max_num, sum(cnt[i::i]))

    if c == 1 and max_num <= 1:
        print('pairwise coprime')
    elif c == 1:
        print('setwise coprime')
    else:
        print('not coprime')


if __name__ == '__main__':
    main()

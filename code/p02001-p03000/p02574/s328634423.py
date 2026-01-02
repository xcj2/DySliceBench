import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def enum_primes(n):
    flag_num = (n + 1) // 2
    prime_flag = [True] * flag_num

    for num in range(3, int(n ** 0.5) + 1, 2):
        idx = (num - 1) // 2 - 1
        if prime_flag[idx]:
            for j in range(idx + num, flag_num, num):
                prime_flag[j] = False

    primes = [2]
    temp = [(i + 1) * 2 + 1 for i in range(flag_num) if prime_flag[i]]
    primes.extend(temp)

    return primes


def main():
    N = int(readline())
    A = list(map(int, readline().split()))
    primes = enum_primes(10 ** 6 + 1)

    def judge():
        seq = [False] * (10 ** 6 + 1)
        A.sort()

        for x in A:
            if x == 1:
                continue
            if seq[x]:
                return False
            seq[x] = True

        for prime in primes:
            cnt = 0
            for i in range(prime, 10 ** 6 + 1, prime):
                if seq[i]:
                    cnt += 1
            if cnt > 1:
                return False
        return True

    if judge():
        print("pairwise coprime")
    else:
        from math import gcd
        cur = A[0]
        for x in A[1:]:
            cur = gcd(cur, x)

        if cur == 1:
            print("setwise coprime")
        else:
            print("not coprime")


if __name__ == '__main__':
    main()

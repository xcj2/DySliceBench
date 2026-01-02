# -*- coding: utf-8 -*-


def main():
    N = int(input())

    def f(n):
        if n < 2:
            return 1
        else:
            return n * f(n - 2)

    def count_tail_zero(s):
        cnt = 0
        for i in range(len(s) - 1, 0, -1):
            if s[i] == '0':
                cnt += 1
            else:
                break
        return cnt

    print(count_tail_zero(str(f(N))))


def correct():
    N = int(input())

    if N % 2 == 1:
        print(0)
        return

    denominator = 10
    ans = 0
    while denominator <= N:
        ans += N // denominator
        denominator *= 5

    print(ans)


if __name__ == "__main__":
    correct()

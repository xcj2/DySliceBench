import sys
input = sys.stdin.readline
import math

def main():
    n, m = input_list()
    if abs(n-m) > 1:
        print(0)
        exit()
    mod = 10**9 + 7
    diff = abs(n-m)
    if diff == 1:
        ans = math.factorial(n) * math.factorial(m)
        print(ans % mod)
    else:
        ans = 2 * (math.factorial(n) * math.factorial(m))
        print(ans % mod)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)


def input_list():
    return list(map(int, input().split()))


def input_list_str():
    return list(map(str, input().split()))


if __name__ == "__main__":
    main()

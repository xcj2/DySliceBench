# import sys
# sys.setrecursionlimit(10 ** 6)
from itertools import combinations_with_replacement

int1 = lambda x: int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors


def solve():
    n = II()
    divisors = make_divisors(n)

    ans = 1001001001001001
    for a, b in combinations_with_replacement(divisors, 2):
        if a * b != n:
            continue
        step = (a-1) + (b-1)
        ans = min(step, ans)
    print(ans)



if __name__ == '__main__':
    solve()

import math
import string


def readints():
    return list(map(int, input().split()))


def nCr(n, r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))


def has_duplicates2(seq):  # リストに重複した要素があるか判定（要素にリストがある場合）
    seen = []
    for item in seq:
        if not(item in seen):
            seen.append(item)
    return len(seq) != len(seen)


def divisor(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    return divisor


s = input()
t = input()
# print(s)
# print(t)


def rotate(s):
    a = []
    a.append(s[-1])
    a.append(s[:-1])
    return ''.join(a)


def solve(r):
    if r == s:
        return False
    if r == t:
        return True
    return solve(rotate(r))


if s == t:
    print("Yes")
    exit()
if solve(rotate(s)):
    print("Yes")
else:
    print("No")

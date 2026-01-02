import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()

digit = 1

alphabets = "abcdefghijklmnopqrstuvwxyz"
ans = ""

while(1):
    if N > pow(26, digit):
        N -= pow(26, digit)
        digit += 1
        continue
    N -= 1
    for j in range(digit):
        ans += alphabets[N // pow(26, digit - j - 1)]
        N = N % pow(26, digit - j - 1)
    break
print(ans)

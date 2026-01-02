import sys
# from collections import defaultdict

N = int(sys.stdin.readline().rstrip())
S = sys.stdin.readline().rstrip()
Q = int(sys.stdin.readline().rstrip())

BIT = [[0 for _ in range(N + 1)] for _ in range(26)]  # 初期化（アルファベット分）
alpha = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
         "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
         "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
         "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
         "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}


# 初期化
def initialize():
    global BIT, S, N
    for j in range(N):
        c = alpha[S[j]]  # 文字切り出し／index に変換
        i = j + 1
        while i <= N:
            BIT[c][i] += 1
            i += (i & -i)


def identify(i):
    # i文字目を、変化点があった文字として探索する
    for c in range(26):
        if sum(i, c) != sum(i - 1, c):
            return c


# 文字の交換
def change(i, before, after):

    global BIT, N
    while i <= N:
        BIT[before][i] -= 1
        BIT[after][i] += 1
        i += (i & -i)


# 文字数の取り出し
def sum(i, c):

    global BIT

    _sum = 0
    while i > 0:
        _sum += BIT[c][i]
        i -= (i & -i)

    return _sum


initialize()

for _ in range(Q):
    q, x, y = sys.stdin.readline().rstrip().split()
    if q == "1":
        i = int(x)
        ac = alpha[y]
        bc = identify(i)
        change(i, bc, ac)

    else:
        x = int(x)
        y = int(y)
        count = 0
        for c in range(26):
            if sum(y, c) != sum(x - 1, c):
                count += 1
        print(count)
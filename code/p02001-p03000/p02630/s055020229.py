import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N = ni()
A_array = na()
a_dic = {}

ans = 0
for a in A_array:
    ans += a
    if a in a_dic:
        a_dic[a] += 1
    else:
        a_dic[a] = 1

ans_array = []

Q = ni()
for _ in range(Q):
    b, c = na()
    if b in a_dic:
        if c in a_dic:
            a_dic[c] += a_dic[b]
        else:
            a_dic[c] = a_dic[b]
        ans = ans + (c - b) * a_dic[b]
        a_dic[b] = 0
    ans_array.append(ans)

print("\n".join(map(str, ans_array)))

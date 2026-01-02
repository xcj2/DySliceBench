import sys

stdin = sys.stdin


def ni(): return int(ns())


def na(): return list(map(int, stdin.readline().split()))


def naa(N): return [na() for _ in range(N)]


def ns(): return stdin.readline().rstrip()  # ignore trailing spaces


N, K = na()
a_array = na()

win = [0] * (K+1)

for i in range(a_array[0]):
    win[i] = 1

for i in range(a_array[0], K+1):
    for a in a_array:
        if i-a >= 0 and win[i-a] == 1:
            win[i] = -1
            break
    else:
        win[i] = 1

# print(win)

print("First" if win[-1] == -1 else "Second")

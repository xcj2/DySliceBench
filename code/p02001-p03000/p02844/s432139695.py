from sys import stdin


def input():
    return stdin.readline()[:-1]


def intput():
    return int(input())


def sinput():
    return input().split()


def intsput():
    return map(int, sinput())


# Code

n = intput()
s = input()

cnt = 0
for a in range(10):
    for b in range(10):
        for c in range(10):
            targets = list(map(str, [a, b, c]))
            i = 0
            target = targets[i]
            for digit in s:
                if digit == target:
                    i += 1
                    if i == 3:
                        break
                    target = targets[i]
            if i == 3:
                cnt += 1

print(cnt)

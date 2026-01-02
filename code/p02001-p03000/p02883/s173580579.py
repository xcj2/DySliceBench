from sys import stdin


def input():
    return stdin.readline()[:-1]


def intput():
    return int(input())


def sinput():
    return input().split()


def intsput():
    return map(int, sinput())


n, k = intsput()

a = list(intsput())
f = list(intsput())

a.sort()
f.sort(reverse=True)
p = [a[i] * f[i] for i in range(n)]
scrap = [0] * n

start = 0
end = max(p)
target = (start + end) // 2
while start != end:
    cnt = 0
    for i in range(n):
        fix = 0
        if p[i] > target:
            fix = (p[i] - target + f[i] - 1) // f[i]
            cnt += fix
        #scrap[i] = a[i] - fix
        if cnt > k:
            start = target + 1
            target = (start + end) // 2
            break
    else:
        end = target
        target = (start + end) // 2

print(start)

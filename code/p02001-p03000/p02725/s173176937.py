import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


############ ---- Input Functions ---- ############
def in_int():
    return (int(input()))


def in_list():
    return (list(map(int, input().split())))


def in_str():
    s = input()
    return (list(s[:len(s) - 1]))


def in_ints():
    return (map(int, input().split()))


k, n  = in_ints()
a = in_list()

mx = 0
ans = 0
for i in range(n):
    next = 0
    if i == n-1:
        next = k + a[0]
    else:
        next = a[i+1]

    mx = max(mx, abs(a[i]- next))
    ans  += abs(a[i]- next)


print(ans - mx)
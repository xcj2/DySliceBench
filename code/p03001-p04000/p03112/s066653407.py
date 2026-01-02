import bisect

A, B, Q = list(map(int, input().split()))
s = [0] * A
for i in range(A):
    s[i] = int(input())

t = [0] * B
for i in range(B):
    t[i] = int(input())


def find_index(arr, xi):
    t = bisect.bisect_left(arr, xi)
    if t == 0:
        return [-float('inf'), arr[0]]
    elif t == len(arr):
        return [arr[-1], float('inf')]
    else:
        return [arr[t-1], arr[t]]


def func1(a, b, x):
    return min(x-a, b-x)


def calc(xi):
    global s, t
    if xi < s[0] and xi < t[0]:
        return max(s[0] - xi, t[0] - xi)

    if xi > s[-1] and xi > t[-1]:
        return max(xi - s[-1], xi - t[-1])

    s1, s2 = find_index(s, xi)
    t1, t2 = find_index(t, xi)

    if t1 < s1 and s2 < t2:
        return func1(t1, t2, xi)

    elif s1 < t1 and t2 < s2:
        return func1(s1, s2, xi)

    elif s1 < t1 and s2 < t2:
        a1 = s2 - xi + s2 - t1
        a2 = xi - t1 + s2 - t1
        return min(a1, a2, func1(s1, t2, xi))

    else:
        a1 = t2 - xi + t2 - s1
        a2 = xi - s1 + t2 - s1
        return min(a1, a2, func1(t1, s2, xi))


for i in range(Q):
    xi = int(input())
    print(calc(xi))

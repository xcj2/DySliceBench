def is_ok_under(array, mid, target):
    return array[mid] < target


def is_ok_over(array, mid, target):
    return array[mid] > target


# ok is -1. ng is len(array)
def bSearchUnder(array, ok, ng, target):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok_under(array, mid, target):
            ok = mid
        else:
            ng = mid
    return ok


# ng is -1. ok is len(array)
def bSearchOver(array, ok, ng, target):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok_over(array, mid, target):
            ok = mid
        else:
            ng = mid
    return ok


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()

ans = 0

for i in range(len(b)):
    add = 1
    add *= bSearchUnder(a, -1, len(a), b[i]) + 1
    add *= len(c) - bSearchOver(c, len(c), -1, b[i])
    ans += add

print(ans)

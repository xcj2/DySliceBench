
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

def is_ok(arg, target, abc):
    if abc[arg] >= target:
        return True
    else:
        return False

def is_ok2(arg, target, abc):
    if abc[arg] > target:
        return True
    else:
        return False


def bict(left, right, target, abc, jug):

    while(right - left > 1):
        mid = (right + left)//2

        if jug(mid, target, abc):
            right = mid
        else:
            left = mid

    return right

cnt = 0
for b in B:
    a_min_index = bict(-1, N, b, A, is_ok)
    c_min_index = bict(-1, N, b, C, is_ok2)
    temp = (a_min_index - 1 + 1) * (N - c_min_index)
    cnt += temp

print(cnt)

N, Q = map(int, input().split())
s = str(input())
coms = [list(map(str, input().split())) for _ in range(Q)]


def isOK(A, index, coms, c):
    # シミュレーションを行う
    for com in coms:
        if com[0] == A[index]:
            if com[1] == 'R':
                index += 1
                if index == len(A):
                    return c == 'R'
            elif com[1] == 'L':
                index -= 1
                if index == -1:
                    return c == 'L'
    return False


def lower_bound(A, coms):
    ng = -1
    ok = len(A)

    while(abs(ok-ng) > 1):
        mid = (ok + ng) // 2

        if isOK(A, mid, coms, 'R'):
            ok = mid
        else:
            ng = mid
    return ok


def upper_bound(A, coms):
    ng = len(A)
    ok = -1

    while(abs(ok-ng) > 1):
        mid = (ok + ng) // 2

        if isOK(A, mid, coms, 'L'):
            ok = mid
        else:
            ng = mid
    return ok


lower = lower_bound(s, coms)
upper = upper_bound(s, coms)
print(lower-upper-1)
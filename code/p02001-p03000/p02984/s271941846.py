import sys

sys.setrecursionlimit(10 ** 7)

debug = True
debug = False


def dprint(*objects):
    if debug == True:
        print(*objects)


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    def check(A, x):
        ans = [x]
        for i in range(1, N):
            tmp = A[i - 1] - ans[i - 1]
            if tmp < 0:
                if i % 2 == 1:
                    return 1, ans
                else:
                    return -1, ans
            else:
                ans.append(tmp)

        tmp = A[N - 1] - (ans[N - 1])
        if x > tmp:
            return 1, ans
        elif x < tmp:
            return -1, ans
        else:
            return 0, ans

    x = min(A[0], A[N - 1])
    jump = min(A[0], A[N - 1]) // 2

    # i = 0
    while True:
        # i += 1
        # if i > 10:
        #     break
        ret, ans = check(A, x)
        if ret == 1:
            x = x - jump
        elif ret == -1:
            x = x + jump
        else:
            dprint(x, ret, ans, jump)
            break
        jump = max(jump // 2, 1)
        dprint(x, ret, ans, jump)

    print(" ".join([str(i * 2) for i in ans]))


solve()
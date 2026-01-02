N, A, B, C = map(int, input().split())
L = [int(input()) for _ in range(N)]


def solve(X):
    if not ("1" in X and "2" in X and "3" in X):
        return 1e10

    MS = [[L[i] for i in range(N) if X[i] == j] for j in "123"]
    ret = 1e10
    A_ans = []
    B_ans = []
    C_ans = []
    for i in range(3):
        A_ans.append(solve2(MS[i], A))
        B_ans.append(solve2(MS[i], B))
        C_ans.append(solve2(MS[i], C))
    ret = min(ret, A_ans[0] + B_ans[1] + C_ans[2])
    ret = min(ret, A_ans[0] + B_ans[2] + C_ans[1])
    ret = min(ret, A_ans[1] + B_ans[0] + C_ans[2])
    ret = min(ret, A_ans[1] + B_ans[2] + C_ans[0])
    ret = min(ret, A_ans[2] + B_ans[0] + C_ans[1])
    ret = min(ret, A_ans[2] + B_ans[1] + C_ans[0])
    return ret


def solve2(M, target):
    def rec(Y, target):
        # Y: [1, 0, 0]
        if len(Y) == len(M):
            if len(set(Y)) == 1 and Y[0] == 0:
                return 1e10
            sum_M = sum([M[i] for i in range(len(M)) if Y[i] == 1])
            return abs(target - sum_M) + 10 * (Y.count(1) - 1)
        return min(rec(Y + [0], target), rec(Y + [1], target))
    ret = rec([], target)
    return ret


ans = 1e10


def rec(X):
    global ans
    if len(X) == N:
        ans = min(ans, solve(X))
        return
    rec(X + "1")
    rec(X + "2")
    rec(X + "3")


rec("")

print(ans)

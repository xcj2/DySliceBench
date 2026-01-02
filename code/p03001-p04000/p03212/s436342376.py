def STR(): return input()

def func(a, b):
    if a > b:
        return 0
    else:
        return 1

def solve_dp(arr, ii):
    dp = [[0, 0] for _ in range(ii)]
    lenarr = len(arr)
    n0 = int(n[0])
    a = lenarr
    for j in range(lenarr):
        a -= func(n0, arr[j])
    dp[0][0] = a
    dp[0][1] = 1 if n0 in arr else 0
    for i in range(1, ii):
        ni = int(n[i])
        a = lenarr
        for j in range(lenarr):
            a -= func(ni, arr[j])
        dp[i][0] = dp[i-1][0] * lenarr + dp[i-1][1] * a
        dp[i][1] = dp[i-1][1] if ni in arr else 0
    return sum(dp[ii-1])

n = STR()
l = len(n)
ans = 0

arr = [[3], [5], [7], [3, 5], [5, 7], [7, 3], [3, 5, 7]]
ans = solve_dp(arr[6], l)
for i in range(3):
    ans += solve_dp(arr[i], l)
for i in range(3, 6):
    ans -= solve_dp(arr[i], l)
for i in range(1, l):
    ans += pow(3, i) + 3 - 3 * pow(2, i)
print(ans)
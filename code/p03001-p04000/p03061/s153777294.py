def solve(n, a_list):
    # 1-origin
    left_dp = [0, a_list[0]]
    right_dp = [0, a_list[-1]]

    # time O(N log(A))
    for key in range(1, n):
        left_value = a_list[key]
        left_dp.append(gcd(left_dp[-1], left_value))

        right_value = a_list[-key-1]
        right_dp.append(gcd(right_dp[-1], right_value))

    ans = 0
    for key in range(1, n + 1):
        ans = max(ans, gcd(left_dp[key-1], right_dp[-key-1]))
    return ans


# time O(log(A))
def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a

    while a % b:
        a, b = b, a % b
    return b


def main():
    n = int(input())
    a_list = list(map(int, input().split()))

    ans = solve(n, a_list)
    print(ans)


main()

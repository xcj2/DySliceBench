# https://onlinejudge.u-aizu.ac.jp/problems/1167


def porok(n):
    return n * (n+1) * (n+2) // 6


def dp_1(n):
    for j in poroks_odd:
        for i in range(j, n+1):
            tmp = dp[i-j] + 1
            if dp[i-j] + 1 < dp[i]:
                dp[i] = dp[i-j] + 1


def dp_2(n):
    for j in poroks_even:
        for i in range(j, n+1):
            tmp = dp[i-j] + 1
            if dp[i-j] + 1 < dp[i]:
                dp[i] = dp[i-j] + 1


if __name__ == "__main__":
    query_list = []
    ans_even = []
    while(True):
        n = int(input())
        if n == 0:
            break
        query_list.append(n)

    poroks = [i * (i + 1) * (i + 2) // 6 for i in range(1, 181)]
    poroks_odd = [
        porok_number for porok_number in poroks if porok_number % 2 == 1]
    poroks_even = [
        porok_number for porok_number in poroks if porok_number % 2 == 0]
    dp = [100] * (max(query_list)+1)
    dp[0] = 0

    dp_1(max(query_list))

    for q in query_list:
        ans_even.append(dp[q])

    dp_2(max(query_list))

    for i, q in enumerate(query_list):
        print('{} {}'.format(dp[q], ans_even[i]))


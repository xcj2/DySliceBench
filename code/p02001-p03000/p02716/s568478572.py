import bisect
import collections
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
ACMOD = 1000000007
INF = 1 << 62


def lmi():
    return list(map(int, input().split()))


def llmi(n):
    return [lmi() for _ in range(n)]


N = int(input())
A = lmi()


# dp = [[-INF]*3 for _ in range(N)]
def solve2():
    """

6
1 2 3 4 5 6
>> 12
6
2 1 3 4 5 6
>> 12
    :return:
    """
    assert N % 2 == 0
    even = [0]
    odd = [0]
    for v in range(N):
        if v % 2 == 0:
            even.append(even[-1] + A[v])
        else:
            odd.append(odd[-1] + A[v])

    # print(even)
    # print(odd)
    ans = 0
    for i in range(len(even)):
        ans = max(ans, even[i] + odd[-1] - odd[i])
    print(ans)


def solve():
    # dp[N][ignored]
    dp = [[-INF] * 3 for _ in range(N // 2 + 1)]
    dp[0][0] = 0
    dp[0][1] = 0
    dp[0][2] = 0

    for v in range(N):
        for ignore_count in range(3):
            if ignore_count == 0:
                flag = (v < N - 1 and v % 2 == 0)
                dp_slice = v // 2
            elif ignore_count == 1:
                flag = (v % 2 == 1)
                dp_slice = v // 2
            else:  # ignore_count == 2:
                flag = (v > 1 and v % 2 == 0)
                dp_slice = v // 2 - 1
            if flag:
                dp[dp_slice + 1][ignore_count] = max(dp[dp_slice][ignore_count] + A[v], dp[dp_slice + 1][ignore_count])
                if ignore_count != 2:
                    dp[dp_slice + 1][ignore_count + 1] = max(dp[dp_slice + 1][ignore_count],
                                                             dp[dp_slice + 1][ignore_count + 1])
                # if ignore_count==0:
                #     dp[dp_slice + 1][2] = max(dp[dp_slice + 1][ignore_count],
                #                                              dp[dp_slice + 1][2])

                # if ignore_count:
                #     dp[dp_slice + 1][ignore_count] = dp[dp_slice][ignore_count - 1]
    if N % 2 == 1:
        print(max(dp[-1]))
    else:
        print(max(dp[-1][:2]))


if N % 2 == 1:
    solve()
else:
    solve()


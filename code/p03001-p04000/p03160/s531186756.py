import sys

sys.setrecursionlimit(1000000)

def input_from_console():
    n = int(input().strip())
    h_list = list(map(int, input().split()))
    return n, h_list


def solve(n, h_list):
    dp = [-1] * (n+2)
    dp[0] = 0
    dp[1] = abs(h_list[1]- h_list[0])
    def dp_solve(i):
        if dp[i] != -1:
            return dp[i]
        dp[i] = min(
            dp_solve(i-1) + abs(h_list[i] - h_list[i-1]),
            dp_solve(i-2) + abs(h_list[i] - h_list[i-2]),
        )
        return dp[i]
    return dp_solve(n-1)


def main():
    n, h_list = input_from_console()
    print(solve(n, h_list))


if __name__ == "__main__":
    import sys

    if sys.gettrace():  # Check if the python interpreter is in debug mode or not.
        check_cases()
    else:
        main()

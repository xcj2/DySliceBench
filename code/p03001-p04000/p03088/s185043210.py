def dfs(index, last, string, memo):
    mod = 10 ** 9 + 7
    if string in memo[index]:
        return memo[index][string]
    if index == last:
        return 1

    ret = 0
    for s in "ACGT":
        if check(string + s):
            ret = (ret + dfs(index + 1, last, string[1:] + s, memo)) % mod
    memo[index][string] = ret
    return ret


def check(string):
    for i in range(4):
        s_list = list(string)
        if i >= 1:
            s_list[i-1], s_list[i] = s_list[i], s_list[i-1]
        if "".join(s_list).count("AGC") >= 1:
            return False
    return True


def main():
    n = int(input())
    memo = [{} for _ in range(n+1)]

    ans = dfs(0, n, "TTT", memo)
    print(ans)


if __name__ == "__main__":
    main()
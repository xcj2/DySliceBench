n = int(input())
mod = 10 ** 9 + 7
memo = [{} for _ in range(n+1)]


def AGCin(s):
    for i in range(len(s) - 2):
        if s[i] == 'A' and s[i+1] == 'G' and s[i+2] == 'C':
            return True
    return False


def isok(last4):
    if AGCin(last4):
        return False
    for i in range(3):
        last4_ = [c for c in last4]
        tmp = last4_[i]
        last4_[i] = last4_[i+1]
        last4_[i+1] = tmp
        if AGCin(''.join(last4_)):
            return False
    return True


def dfs(i, last3):
    if i == n:
        return 1
    if last3 in memo[i]:
        return memo[i][last3]
    ret = 0
    for c in 'AGCT':
        last4 = last3 + c
        if isok(last4):
            new_last3 = last4[1:]
            delta = dfs(i+1, new_last3)
            memo[i+1][new_last3] = delta
            ret = (ret + delta) % mod
    return ret


print(dfs(0, 'TTT'))
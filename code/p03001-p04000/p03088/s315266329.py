import sys

def check(last4):
    for i in range(4):
        t = list(last4)
        if i >= 1:
            t[i-1], t[i] = t[i], t[i-1]
        if ''.join(t).count('AGC') >= 1:
            return False
    return True


def dfs(cur, last3, N, memo=[]):
    if last3 in memo[cur]:
        return memo[cur][last3]

    if cur == N:
        return 1

    ret = 0
    for c in 'AGCT':
        if check(last3 + c):
            ret = (ret + dfs(cur+1, last3[1:]+c, N, memo)) % (10**9 + 7)
    memo[cur][last3] = ret
    return ret


def main():
    input = sys.stdin.readline
    N = int(input())

    memo = [{} for _ in range(N+1)]
    print(dfs(0, 'TTT', N, memo))

if __name__ == '__main__':
    main()

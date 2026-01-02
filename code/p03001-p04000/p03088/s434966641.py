def main():
    n = int(input())
    MOD = 10 ** 9 + 7
    note = [{} for _ in range(n+1)]

    def ok(last4):
        for i in range(4):
            t = list(last4)
            if i >= 1:
                t[i-1], t[i] = t[i], t[i-1]
            if ''.join(t).count('AGC') >= 1:
                return False
        return True

    def dfs(cur, last3):
        if last3 in note[cur]:
            return note[cur][last3]
        if cur == n:
            return 1
        ret = 0
        for c in 'ACGT':
            if ok(last3 + c):
                ret += dfs(cur + 1, last3[1:] + c)
                ret %= MOD
        note[cur][last3] = ret
        return ret

    print(dfs(0, 'TTT'))


main()

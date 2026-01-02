#貰うDP
import itertools
N, MOD = int(input()), 10**9+7
memo = [{'AGC':0, 'ACG':0, 'GAC':0} for i in range(N + 1)]
C = list('ACGT')
for c in itertools.product(C, C, C):
    c = ''.join(c)
    if c in memo[3]:
        continue
    else:
        memo[3][c] = 1

def ok(last4):
    for i in range(4):
        t = list(last4)
        if i>= 1:
            t[i-1], t[i] = t[i], t[i-1]
            if ''.join(t).count('AGC') == 1:
                return False
    return True

def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    ret = 0
    for c in 'ACGT':
        if ok(c + last3):
            ret = (ret + dfs(cur - 1, c + last3[:-1])) % MOD
    memo[cur][last3] = ret
    return ret

def answer(n):
    ans = 0
    clist = list('ACGT')
    for c in itertools.product(clist, clist, clist):
        ch = ''.join(c)
        ans += dfs(n, ch)
    return ans % MOD

print(answer(N))
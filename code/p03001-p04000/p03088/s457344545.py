import sys
sys.setrecursionlimit(10**7)
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return sys.stdin.readline().strip()
INF = 10 ** 18
MOD = 10 ** 9 + 7

def main_old(): 
    N = II()
    
    dp = {'a': [1,1,4,16] + [0 for _ in range(N)],
    't': [1,1,4,16] + [0 for _ in range(N)],
    'g': [1,1,4,15] + [0 for _ in range(N)],
    'c': [1,1,4,14] + [0 for _ in range(N)]
    }

    codons = ['a', 't', 'g', 'c']

    # if N < 5:
    # for i in range(4, N+1):
    #     dp['a'][i] = dp['a'][i-1] +  dp['t'][i-1] +  dp['g'][i-1] +  dp['c'][i-1]
    #     dp['t'][i] = dp['a'][i-1] +  dp['t'][i-1] +  dp['g'][i-1] +  dp['c'][i-1]
    #     dp['g'][i] = dp['a'][i-2] * 3 + dp['t'][i-2] * 4 + dp['g'][i-2] * 4 + dp['c'][i-2] * 4
    #     dp['c'][i] = dp['a'][i-3] * 9 + dp['t'][i-3] * 12 + dp['g'][i-3] * 11 + dp['c'][i-3] * 12
    for i in range(4, N+1):
        dp['a'][i] = dp['a'][i-3] * 14 + dp['t'][i-3] * 16 + dp['g'][i-3] * 15 + dp['c'][i-3] * 16
        dp['t'][i] = dp['a'][i-3] * 14 + dp['t'][i-3] * 16 + dp['g'][i-3] * 15 + dp['c'][i-3] * 16
        dp['g'][i] = dp['a'][i-3] * 13 + dp['t'][i-3] * 15 + dp['g'][i-3] * 15 + dp['c'][i-3] * 15
        dp['c'][i] = dp['a'][i-3] * 9 + dp['t'][i-3] * 14 + dp['g'][i-3] * 13 + dp['c'][i-3] * 14

    sum_ = 0
    for x in codons:
        sum_ += dp[x][N] % MOD
    print(sum_ % MOD)
    return

def is_valid(s):
    if s[0:3] == 'AGC' or s[0]+s[2:4] == 'AGC' or s[0:2] + s[3] == 'AGC' or s[1:4] == 'AGC' or s.count('GAC') > 0 or s.count('ACG') > 0:
        return False
    else:
        return True

def main(): 
    N = II()

    if N == 3:
        print(61)
        return
    
    import collections
    dp = collections.defaultdict(int)
    import itertools
    for st in itertools.product('AGCT', repeat=4):
        st = ''.join(st)
        if is_valid(st):
            dp[st] = 1
        else:
            dp[st] = 0

    for i in range(4, N):
        dp2 = collections.defaultdict(int)
        for st in itertools.product('AGCT', repeat=4):
            st = ''.join(st)
            for char in 'AGCT':
                nex = st[1:4] + char
                if is_valid(nex):
                    dp2[nex] = (dp2[nex] + dp[st])%MOD
                else:
                    pass
        dp = dp2

    sum_ = 0
    for st in itertools.product('AGCT', repeat=4):
        st = ''.join(st)
        sum_ = (sum_ + dp[st])%MOD
    print(sum_)

main()
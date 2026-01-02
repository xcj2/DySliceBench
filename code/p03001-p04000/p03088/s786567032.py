import sys
sys.setrecursionlimit(10**7)
INF = 10 ** 18
MOD = 10 ** 9 + 7
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x) - 1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def SI(): return input()

from itertools import product

def cnt(N):
    ret = 0
    for s in product('ACGT', repeat=N):
        s = ''.join(s)
        if 'AGC' in s or 'GAC' in s or 'ACG' in s:
            continue
        if 'AGGC' in s or 'ATGC' in s or 'AGTC' in s:
            continue
        ret += 1
    return ret

def main():
    N = II()
    ans = 0
    dp = {'':1, 'A':0, 'G':0, 'GA':0, 'AC':0, 'AT':0, 'AG':0,
        'ATG':0, 'AGT':0, 'AGG':0}
    for _ in range(N):
        tmp = {}
        tmp[''] = dp[''] * 2 + dp['G'] * 2 + \
            dp['AC'] * 2 + dp['AT'] * 2 + \
            dp['ATG'] * 1 + dp['AGT'] * 1 + dp['AGG'] * 1
        tmp['A'] = dp[''] + dp['A'] + dp['GA'] + dp['AC'] + dp['AT'] + dp['AGT']
        tmp['G'] = dp[''] + dp['G'] + dp['AGG'] + dp['ATG'] + dp['AGT']
        tmp['GA'] = dp['G'] + dp['AG'] + dp['ATG'] + dp['AGG']
        tmp['AC'] = dp['A']
        tmp['AT'] = dp['A'] + dp['GA']
        tmp['AG'] = dp['A'] + dp['GA']
        tmp['ATG'] = dp['AT']
        tmp['AGT'] = dp['AG']
        tmp['AGG'] = dp['AG']
        dp = tmp
    ans = sum(v for v in dp.values())

    return ans % MOD

print(main())
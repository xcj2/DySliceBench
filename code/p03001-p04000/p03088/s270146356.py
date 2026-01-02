ngs4 = ["ATGC", "AGTC","ACGC", "AGCC","AGGC", "AGGC"]
ngs3 = ["AGC", "ACG", "GAC"]
def is_valid(b):
    s = b[-4:]
    if s in ngs4:
        return False
    s = s[-3:]
    if s in ngs3:
        return False
    return True

N = int(input())
memo = [{} for i in range(N+1)]
acgt = ["A", "C", "G", "T"]
MOD = 10**9 + 7
def dp(i, last3):
    if last3 in memo[i]:
        return memo[i][last3]

    if i == N:
        return 1
    
    ret = 0
    for c in acgt:
        candi = last3 + c
        if is_valid(candi):
            ret = (ret + dp(i+1, last3[1:] +c)) % MOD
    memo[i][last3] = ret
    return ret

def sub():
    print(dp(0, "TTT"))

sub()

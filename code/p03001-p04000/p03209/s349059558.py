N,X = map(int,input().split())

# B[L] = 1 + B[L-1] + 1 + B[L-1] + 1
# B[0] = 1
def Ber_memo(L,memo=[0]*(N+1)):
    if L == 0:
        return 1
    if memo[L] != 0:
        return memo[L]
    memo[L] = 2*Ber_memo(L-1) + 3
    return memo[L]

# P[L] = P[L-1] + 1 + P[L-1]
# P[L] = 1
def Patty_memo(L,memo=[0]*(N+1)):
    if L == 0:
        return 1
    if memo[L] != 0:
        return memo[L]
    memo[L] = 2*Patty_memo(L-1) + 1
    return memo[L]

def rec_memo(L=N,bottom=X):
    if L == 0:
        return 1
    if bottom <= 1:
        return 0
    elif bottom <= 1 + Ber_memo(L-1):
        return rec_memo(L-1,bottom-1)
    elif bottom == 1 + Ber_memo(L-1) + 1:
        return Patty_memo(L-1) + 1
    elif bottom <= 1 + Ber_memo(L-1) + 1 + Ber_memo(L-1):
        return Patty_memo(L-1) + 1 + rec_memo(L-1,bottom-(1+Ber_memo(L-1)+1))
    elif bottom <= 1 + Ber_memo(L-1) + 1 + Ber_memo(L-1) + 1:
        return Patty_memo(L-1) + 1 + Patty_memo(L-1)

print(rec_memo())
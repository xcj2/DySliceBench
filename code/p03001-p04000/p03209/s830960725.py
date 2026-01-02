N,X = map(int,input().split())

# B[L] = 1 + B[L-1] + 1 + B[L-1] + 1
# B[0] = 1
def Ber(L):
    if L == 0:
        return 1
    return 2*Ber(L-1) + 3

# P[L] = P[L-1] + 1 + P[L-1]
# P[L] = 1
def Patty(L):
    if L == 0:
        return 1
    return 2*Patty(L-1) + 1

def rec(L=N,bottom=X):
    if L == 0:
        return 1
    if bottom <= 1:
        return 0
    elif bottom <= 1 + Ber(L-1):
        return rec(L-1,bottom-1)
    elif bottom == 1 + Ber(L-1) + 1:
        return Patty(L-1) + 1
    elif bottom <= 1 + Ber(L-1) + 1 + Ber(L-1):
        return Patty(L-1) + 1 + rec(L-1,bottom-(1+Ber(L-1)+1))
    elif bottom <= 1 + Ber(L-1) + 1 + Ber(L-1) + 1:
        return Patty(L-1) + 1 + Patty(L-1)

print(rec())
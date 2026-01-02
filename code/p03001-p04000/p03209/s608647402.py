N,X = map(int,input().split())
B = [-1 for i in range(51)]
P = [-1 for i in range(51)]

def buns(L):
    if L == 0:#再帰終了条件
        B[L] = 0
        return B[L]
    else:
        if B[L] == -1:
            B[L] = buns(L-1)*2 + 2
            return B[L]
        else:
            return B[L]

def patty(L):
    if L == 0:#再帰終了条件
        P[L] = 1        
        return P[L]
    else:
        if P[L] == -1:
            P[L] = patty(L-1)*2 + 1
            return P[L]
        else:
            return P[L]


buns(N)
patty(N)
memo = [B[i] + P[i] for i in range(51)]

def func(L,X):

    if L == 0:
        if X <= 0:
            return 0
        else:
            return 1
    elif X <= memo[L-1]+1:
        return func(L-1,X-1)
    else :
        return P[L-1] + 1 + func(L-1,X-2-memo[L-1])


print(func(N,X))
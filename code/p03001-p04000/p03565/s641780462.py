S_prime = input()
T = input()

def judge(A,B):
    for i in range(len(A)):
        if A[i] != B[i] and A[i] != "?" and B[i] != "?":
            return False
    return True

def dec(S_prime,T):
    S_cand = []
    for i in range(len(S_prime)-len(T)+1):
        if judge(S_prime[i:i+len(T)],T):
            S_cand.append( S_prime[:i] + T + S_prime[i+len(T):] )
    return S_cand

def S_change(S):
    S = list(S)
    for i in range(len(S)):
        if S[i] == "?":
            S[i] = "a"
    S = "".join(S)
    return S

if len(dec(S_prime,T)) == 0:
    print("UNRESTORABLE")
else:
    Ans = dec(S_prime,T)
    for i in range(len(Ans)):
        Ans[i] = S_change(Ans[i])
    Ans.sort()
    print(Ans[0])

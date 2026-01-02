def pare_exist(ST_pare_lst, Si, Ti):
    if (Si, Ti) in ST_pare_lst:
        return True
    else:
        for Sj, Tj in ST_pare_lst:
            if (Sj == Si and Tj != Ti) or (Sj != Si and Tj == Ti):
                return False
        
        ST_pare_lst.append((Si, Ti))
        return None

def exchanging(S, T):
    ST_pare_lst = []
    length = len(S)

    for i in range(length):
        judge = pare_exist(ST_pare_lst, S[i], T[i])
        if judge is None:
            pass
        elif judge == True:
            pass
        else:   #   judge == False
            return False
    return True

def same_chr_contain(S, T):
    S_chr_lst = []
    T_chr_lst = []
    for i in range(len(S)):
        if not S[i] in S_chr_lst:
            S_chr_lst.append(S[i])
        if not T[i] in T_chr_lst:
            T_chr_lst.append(T[i])

    if len(S_chr_lst) == len(T_chr_lst):
        return True
    else:
        return False

S = input()
T = input()

ST_pare_lst = []
length = len(S)

if not same_chr_contain(S, T):
    print("No")
elif exchanging(S, T):
    print("Yes")
else:
    print("No")

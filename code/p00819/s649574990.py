def C(S):
    return S[1:] + S[0]


def J(S):
    return S[-1] + S[:-1]


def E(S):
    temp = len(S) // 2
    if len(S) % 2 == 0:
        S = S[temp:] + S[:temp]
    else:
        S = S[temp + 1:] + S[temp] + S[:temp]

    return S


def A(S):
    return S[::-1]


def M(S):
    temp = []
    for s in S:
        if s.isdecimal():
            temp.append("0" if s == "9" else str(int(s) + 1))
        else:
            temp.append(s)
    return "".join(temp)


def P(S):
    temp = []
    for s in S:
        if s.isdecimal():
            temp.append("9" if s == "0" else str(int(s) - 1))
        else:
            temp.append(s)
    return "".join(temp)


ans = []

n = int(input())

for i in range(n):
    messenger = input()
    messenger = messenger[::-1]
    S = input()
    for m in messenger:
        if m == "J":
            S = J(S)
        elif m == "C":
            S = C(S)
        elif m == "E":
            S = E(S)
        elif m == "A":
            S = A(S)
        elif m == "P":
            S = P(S)
        elif m == "M":
            S = M(S)

    ans.append(S)

for s in ans:
    print(s)

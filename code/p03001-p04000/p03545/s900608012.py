def sarch(B, C, D):
    return a + B * b + C * c + D * d == 7

def ansprint(B, C, D):
    print(str(a) + B + str(b) + C + str(c) + D + str(d) + "=7")

def figstr(B, C, D):
    BB = "-"
    CC = "-"
    DD = "-"
    if B == 1:
        BB = "+"
    if C == 1:
        CC = "+"
    if D == 1:
        DD = "+"
    ansprint(BB, CC, DD)

S = input()
a = int(S[0])
b = int(S[1])
c = int(S[2])
d = int(S[3])

if sarch(1, 1, 1):
    figstr(1, 1, 1)
elif sarch(1, -1, 1):
    figstr(1, -1, 1)
elif sarch(1, 1, -1):
    figstr(1, 1, -1)
elif sarch(-1, 1, 1):
    figstr(-1, 1, 1)
elif sarch(-1, -1, 1):
    figstr(-1, -1, 1)
elif sarch(1, -1, -1):
    figstr(1, -1, -1)
elif sarch(-1, 1, -1):
    figstr(-1, 1, -1)
elif sarch(-1, -1, -1):
    figstr(-1, -1, -1)

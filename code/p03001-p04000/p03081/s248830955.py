N, Q = map(int, input().split())
S = input()

TD = []
for i in range(Q):
    t, d = input().split()
    if d == 'L':
        d = -1
    else:
        d = 1
    TD.append([t, d])

def f(x):
    i = x
    for td in TD:
        if td[0] == S[i]:
            i += td[1]
            if i < 0:
                return -1
            if i >= N:
                return 1
    return 0

def bisectL():
    L = -1
    R = N
    while R - L > 1:
        M = (L + R) // 2
        if f(M) < 0:
            L = M
        else:
            R = M
    return L
    
def bisectR():
    L = -1
    R = N
    while R - L > 1:
        M = (L + R) // 2
        if f(M) > 0:
            R = M
        else:
            L = M
    return R
    
print(bisectR() - bisectL() - 1)
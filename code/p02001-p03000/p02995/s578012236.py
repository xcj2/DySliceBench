
A, B, C, D = map(int, input().split())
U = B - A + 1

MofD = 0
MofCD = 0

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def lcm(x, y):
    return (x * y) // gcd(x, y)


def sten(st, en, x):
    if x == 1:
        return en - st + 1
    st = st // x if st % x == 0 else st // x + 1
    en = en // x
    st *= x
    en *= x
    if en >= st:
        n = (en - st) // x + 1
    else:
        n = 0
    return n


MofC = sten(A, B, C)
if C != D:
    MofD = sten(A, B, D)
    MofCD = sten(A, B, lcm(C, D))

print(U-MofC-MofD+MofCD)

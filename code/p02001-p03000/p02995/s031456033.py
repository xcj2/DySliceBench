A,B,C,D = map(int,input().split())

# n 以下の数に m の倍数が何個あるかを返す関数
def baisuNum(n,m):
    return n // m

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)


# B以下　―　(A-1)以下　にCの倍数何個ある
CC = baisuNum(B,C) - baisuNum(A-1,C)
# B以下　―　(A-1)以下　にDの倍数何個ある
DD = baisuNum(B,D) - baisuNum(A-1,D)
# B以下　―　(A-1)以下　にCかつDの最小公倍数の倍数何個ある
LCM = lcm(C,D)
CD = baisuNum(B, LCM) - baisuNum(A-1, LCM)

print(B-A+1-CC-DD+CD)

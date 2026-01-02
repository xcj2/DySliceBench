def int_raw():
    return int(input())

def ss_raw():
    return input().split()

def ints_raw():
    return list(map(int, ss_raw()))

INF = 1<<29

N = int_raw()
As =[]
for _ in range(N):
    As.append(int_raw())
SUM = sum(As)

DIV = 998244353

ALL = 1
for _ in range(N):
    ALL = (ALL*3)%DIV

def main():
    dp1 = [0]*(SUM+1)
    dp3 = [0]*(SUM+1)
    dp1[0]=1
    dp3[0]=1
    
    for n in range(N):
        a = As[n]
        dp1 = [(dp1[s]+(dp1[s-a] if s>=a else 0))%DIV for s in range(SUM+1)]
        dp3 = [(dp3[s]*2 + (dp3[s-a] if s>=a else 0))%DIV for s in range(SUM+1)]

    S3 = (sum(dp3[(SUM+1)//2:])*3)%DIV
    S1 = (dp1[(SUM)//2]*3)%DIV if SUM%2==0 else 0
    return (ALL - S3 + S1 + DIV) % DIV

print(main())

import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし


N = I()
X = LI2()
X.reverse()

if N == 1 and len(X) == 1 and X[0] == 0:
    print(1)
    exit()


def popcount(n):
    res = 0
    m = n.bit_length()
    for i in range(m):
        res += (n >> i) & 1
    return res


# 1回の操作で 2*10**5 未満になることに注意

F = [0]*(2*10**5)  # F[i] = f(i)
for i in range(1,2*10**5):
    F[i] = 1 + F[i % popcount(i)]

a = sum(X)
b = a-1
c = a+1
if a == 1:
    C = [1]  # 2冪をcで割った余り
    xc = 0  # Xをcで割った余り
    for i in range(N):
        if X[i] == 1:
            xc += C[-1]
            xc %= c
        C.append((2 * C[-1]) % c)

    ANS = []
    for i in range(N):
        if X[i] == 1:
            ANS.append(0)
        else:
            ANS.append(1 + F[(xc + C[i]) % c])

    ANS.reverse()
    print(*ANS, sep='\n')
    exit()

B,C = [1],[1]  # 2冪をb,cで割った余り
xb,xc = 0,0  # Xをb,cで割った余り
for i in range(N):
    if X[i] == 1:
        xb += B[-1]
        xc += C[-1]
        xb %= b
        xc %= c
    B.append((2*B[-1])%b)
    C.append((2*C[-1])%c)

ANS = []
for i in range(N):
    if X[i] == 1:
        ANS.append(1 + F[(xb-B[i]) % b])
    else:
        ANS.append(1 + F[(xc+C[i]) % c])

ANS.reverse()
print(*ANS,sep='\n')

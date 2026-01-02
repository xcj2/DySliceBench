import math
def extgcd(a, b):
    """
    ax + by = gcd(a,b) = d となる (x,y,d) を返す
    """
    if b == 0:
        return (1, 0, a)
    q, r = a // b, a % b
    x, y, d = extgcd(b, r)
    s, t = y, x - q * y
    return s, t, d

def inv_mod(a, N):
    """
    ax = 1 mod N となる x を返す
    """
    return extgcd(a, N)[0]

def CRT(a_1, a_2, m_1, m_2):
    """
    x = a_1 mod m_1, x = a_2 mod m_2 となる x を返す
    """
    y = (a_2 - a_1) * inv_mod(m_1, m_2) % m_2
    return a_1 + m_1 * y

N = int(input())
N *= 2
K = [[1, N]]
for i in range(2, max(int(N**0.5)+1, 2)):
    if N % i == 0:
        K.append([i, N//i])

ans = float("inf")
for i in range(len(K)):
    a, b = K[i]
    if math.gcd(a, b) == 1:
        P = CRT(0, -1, a, b)
        if P != 0:
            ans = min(P, ans)
        Q = CRT(0, -1, b, a)
        if Q != 0:
            ans = min(Q, ans)

print(ans)
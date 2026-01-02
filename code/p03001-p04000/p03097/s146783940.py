import sys
readline = sys.stdin.readline

def popcount(i):
    assert 0 <= i < 0x100000000
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

P1 = [0, 2, 3, 1, 1, 3, 2, 0]
P2 = [0, 2, 3, 1, 1, 0, 2, 3]
Q = [0, 1, 1, 0]
def grey(N, K):
    if K%2 == 0:
        return False
    if N == 1:
        return [0, 1]
    if N == 2:
        return [0, 2, 3, 1]
    
    if N == K:
        L = grey(N-2, K-2)
        P = P1*((1<<(N-3))-1) + P2
        return [(1<<(N-2))*P[i]|L[i//4] for i in range(1<<N)]
    
    L = grey(N-1, K)
    return [(1<<(N-1))*Q[i%4]|L[i//2] for i in range(1<<N)]

def calc(N, y):
    k = popcount(y)
    pu = [0]*N
    cnt0 = k
    cnt1 = 0
    for i in range(N):
        if (1<<i)&y:
            pu[cnt1] = i
            cnt1 += 1
        else:
            pu[cnt0] = i
            cnt0 += 1
    return pu

def restore(N, x, pu):
    res = 0
    for i in range(N):
        if (1<<i)&x:
            res |= 1<<pu[i]
    return res
    
    
N, A, B = map(int, readline().split())

K = popcount(A^B)
Ans = grey(N, K)

if Ans:
    pu = calc(N, A^B)
    Ans = [A^(restore(N, a, pu)) for a in Ans]
    print('YES')
    print(*Ans)
else:
    print('NO')
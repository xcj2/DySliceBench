def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

def l_s(L):
    return "".join(map(str, L))

from itertools import combinations_with_replacement as cwr

N, M, Q = MI()
comb = [LI() for _ in range(Q)]
sequence = list(range(1, M + 1))
ans = 0

for A in cwr(sequence, N):
    tmp = 0
    A = list(A)
    for abcd in comb:
        a, b, c, d = abcd[0], abcd[1], abcd[2], abcd[3]
        if A[b - 1] - A[a - 1] == c:
            tmp += d
            
    ans = max(ans, tmp)
    
print(ans)
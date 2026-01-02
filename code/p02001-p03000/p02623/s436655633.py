def INT():
    return int(input())

def MI():
    return map(int, input().split())

def LI():
    return list(map(int, input().split()))

N, M, K = MI()
A = [0] + LI()
B = [0] + LI()

for i in range(1, N + 1):
    A[i] += A[i - 1]

for i in range(1, M + 1):
    B[i] += B[i - 1]
    
    if B[i] <= K:
        ans = i

ans = 0

for bk_a in range(N + 1):
    time = A[bk_a]

    if time > K:
        break
        
    l, r = -1, M + 1
    while abs(l - r) > 1:
        bk_b = (l + r) // 2

        if time + B[bk_b] <= K:
            l = bk_b
        else:
            r = bk_b
    
    bk_b = max(0, l)
    ans = max(ans, bk_a + bk_b)

print(ans)
def comb(a, b):
    ans = 1
    for i in range(b):
        ans *= (a - i)
    for i in range(2, b + 1):
        ans //= i
    return ans

def solve_k1(N):
    ans = 0
    N = str(N)
    len_N = len(N)
    ans += 9 * (len_N - 1)
    ans += int(N[0])
    return ans

def solve_k2(N):
    ans = 0
    N = str(N)
    len_N = len(N)
    if len_N < 2:
        return 0
    ans = comb((len_N - 1), 2) * 9 ** 2 + (int(N[0]) - 1) * ((len_N - 1) * 9) + solve_k1(int(N[1:]))
    return ans

def solve_k3(N):
    ans = 0
    N = str(N)
    len_N = len(N)
    if len_N < 3:
        return 0
    ans = comb(len_N - 1, 3) * 9 ** 3 + (int(N[0]) - 1) * comb(len_N - 1, 2) * 9 ** 2 + solve_k2(int(N[1:]))
    return ans

N = int(input())
K = int(input())
ans = 0
if K == 1:
    ans = solve_k1(N)
elif K == 2:
    ans = solve_k2(N)
else:
    ans = solve_k3(N)
print(ans)
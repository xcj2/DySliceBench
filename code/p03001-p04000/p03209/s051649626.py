n_x = input()
n_x_list =n_x.split(' ')

N = int(n_x_list[0])
X = int(n_x_list[1])

# g_list = [''] * N
# def G(N):
#     if N == 0:
#         return 'p'
#
#     gn_1 = G(N-1)
#
#     return 'b' + gn_1 + 'p' + gn_1 + 'b'

# g_n = G(N)
# print(g_n)
# eaten_burger = g_n[0:X]
# print(eaten_burger)
# ans = eaten_burger.count('p')
# print(ans)

def L(N):
    return 2 ** (N+2) - 3

def P(N):
    return 2 ** (N+1) - 1

def solve(N, X):
    half_l = int(L(N) / 2)
    if N == 0 and X >= 1:
        return 1
    elif N == 0 and X == 0:
        return 0

    if half_l <= 1:
        return 0
    elif X < half_l:
        return solve(N - 1, X - 1)
    elif X == half_l:
        return P(N-1)
    elif X == half_l + 1:
        return P(N-1) + 1
    elif half_l + 1 < X:
        return P(N-1) + 1 + solve(N-1, (X - L(N-1) - 2))
    elif half_l * 2 + 3 == X:
        return 2 * P(N-1) + 1


ans = solve(N, X)
print(ans)
# def f(P):
#     """与えられたPのときに、運べる荷物の数vを返す関数"""
#     i = 0  # 荷物の番号
#     v = 0  # 運べる荷物の数
#     k = 0  # トラックの番号
#     current_weight = 0  # 現在のトラックの重さ
#     # current_v = 0  # 現在のトラックに積まれている荷物の数
#
#     while True:
#         # print(i, v, k)
#
#         if W[i] > P:
#             i += 1
#         else:
#             current_weight += W[i]
#
#             if current_weight > P:
#                 k += 1
#             elif current_weight == P:
#                 i += 1
#                 v += 1
#                 k += 1
#             else:  # current_weight < P:
#                 i += 1
#                 v += 1
#
#         if i == N or k == K:
#             break
#     return v

def f(P):
    i = 0
    for k in range(K):
        current_weight = 0
        while current_weight + W[i] <= P:
            current_weight += W[i]
            i += 1
            if i == N:
                return N

    return i


def solve_binary():
    left = 0
    right = max(W)  # ではない！これだとトラックが足りなくて積み切れない場合がある。
    right = 100000 * 10000

    while (right - left) > 1:  # つまり、これが境目の証！！！
        mid = (left + right) // 2
        mid_v = f(mid)

        if mid_v >= N:
            right = mid
        elif mid_v < N:
            left = mid

    return right


def solve_linear():
    p = 1
    while True:
        v = f(p)
        # print(p, v, N)

        if v == N:
            # print(p)
            return p

        p = p + 1


N, K = map(int, input().split())
# W = list(map(int, input().split()))
W = [int(input()) for _ in range(N)]
# print(n, k, W)

# print(solve_linear())
print(solve_binary())


# coding: utf-8
def II(): return int(input())
def ILI(): return list(map(int, input().split()))


def read():
    N, K = ILI()
    A, B = [], []
    for __ in range(N):
        a, b = ILI()
        A.append(a)
        B.append(b)
    return N, K, A, B


def solve(N, K, A, B):
    l_K = [K]
    len_bin_K = len(bin(K)) - 2
    all_1 = sum([2 ** x for x in range(len_bin_K - 1)])
    l_K.append(all_1)
    for i in range(len(bin(K)) - 4, -1, -1):
        if K >> i & 1 == 1:
            now = K >> i
            now = now & ~1
            now = ~now
            now = now << (i)
            now = ~now
            l_K.append(now)

    l_ans = [0] * len(l_K)
    for i in range(N):
        for j in range(len(l_K)):
            if l_K[j] | A[i] == l_K[j]:
                l_ans[j] += B[i]
    ans = max(l_ans)
    return ans


def main():
    params = read()
    print(solve(*params))


if __name__ == "__main__":
    main()

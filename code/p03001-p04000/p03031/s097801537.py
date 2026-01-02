def read():
    N, M = list(map(int, input().strip().split()))
    S = [-1] * M
    for i in range(M):
        inputs = list(map(int, input().strip().split()))
        S[i] = sw_to_seq(inputs[0], inputs[1:])
    P = list(map(int, input().strip().split()))
    return N, M, S, P


def sw_to_seq(k, s):
    s_seq = 0
    for i in range(k):
        bit = 1 << (s[i] - 1)
        s_seq += bit
    return s_seq


def count_sw_on(s_seq, i):
    sw_on = s_seq & i
    count = 0
    while sw_on > 0:
        count += (sw_on & 1)
        sw_on >>= 1
    return count


def solve(N, M, S, P):
    count_all_sw_on = 0
    for i in range(1 << N):
        num_sw_on = 0
        for j in range(M):
            if count_sw_on(S[j], i) % 2 == P[j]:
                num_sw_on += 1
        if num_sw_on == M:
            count_all_sw_on += 1
    return count_all_sw_on


if __name__ == '__main__':
    inputs = read()
    print("%d" % solve(*inputs))
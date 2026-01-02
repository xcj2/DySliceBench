import sys
input = sys.stdin.readline


def pack(C):
    bitmask = 0
    for c in C:
        d = 1 << (c-1)
        bitmask |= d
    return bitmask


def read():
    N, M = list(map(int, input().strip().split()))
    A = list()
    C = list()
    for i in range(M):
        a, b = list(map(int, input().strip().split()))
        A.append(a)
        c = map(int, input().strip().split())
        C.append(pack(c))
    return N, M, A, C


def solve(N, M, A, C, INF=10**9):
    # dp[state][i]: i本の鍵[0, i)を使って状態stateにするための最小コスト
    n_states = 1 << N
    end_state = n_states - 1
    dp = [[INF for j in range(2)] for state in range(n_states)]
    dp[0][0] = 0
    dp[0][1] = 0

    for j in range(M):
        m0 = j & 1
        m1 = 1 - m0
        for state in range(n_states):
            next_state = state | C[j]
            dp[state][m1] = min(dp[state][m1], dp[state][m0])
            if next_state > state:
                dp[next_state][m1] = min(dp[next_state][m1], dp[state][m0] + A[j])
    
    m0 = M & 1
    return dp[end_state][m0] if dp[end_state][m0] != INF else -1


if __name__ == "__main__":
    inputs = read()
    print("%s" % solve(*inputs))

import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]

    
def main():
    N, K = read_values()
    R, S, P = read_values()
    T = input().strip()

    res = 0
    F = [True] * N
    for i, t in enumerate(T):
        if i >= K:
            if T[i - K] == T[i] and F[i - K]:
                F[i] = False
                continue
        
        if t == "r":
            res += P
        elif t == "s":
            res += R
        elif t == "p":
            res += S
    print(res)


if __name__ == "__main__":
    main()

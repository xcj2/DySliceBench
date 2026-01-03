import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def f(S, init):
    F = [init[0], init[1]]
    for i, s in enumerate(S):
        if i == 0:
            continue
        d = 1 if s == "o" else -1
        F.append(F[i - 1] * F[i] * d)
    
    if F[0] != F[-1]:
        return None
    
    d = 1 if S[0] == "o" else -1
    d *= F[0]
    N = len(S)
    if F[-2] * F[1] == d:
        # print(F)
        return F[:N]
    else:
        return None


def main():
    N = int(input())
    S = input().strip()

    for init in [(1, 1), (-1, 1), (1, -1), (-1, -1)]:
        F = f(S, init)
        if F is not None:
            F = map(lambda v: "S" if v == 1 else "W", F)
            print("".join(F))
            return 
    
    print(-1)


if __name__ == "__main__":
    main()

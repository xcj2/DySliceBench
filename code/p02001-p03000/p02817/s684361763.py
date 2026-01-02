import sys
import itertools
input = sys.stdin.readline


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def read_lists(N):
    return [read_list() for n in range(N)]


def dfs(N, L, s):
    depth = [-1] * N

    stack = [(0, s)]
    while stack:
        d, p = stack.pop()
        depth[p] = d

        for q in L[p]:
            if depth[q] != -1:
                continue
            stack.append((d + 1, q))
    return depth

    
def main():
    S, T = input().split()

    print(T + S)


if __name__ == "__main__":
    main()

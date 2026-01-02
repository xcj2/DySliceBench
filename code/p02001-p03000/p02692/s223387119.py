#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")


def yes():
    print("Yes")  # type: str


def no():
    print("No")  # type: str


def solve(N: int, A: int, B: int, C: int, s: "List[str]"):
    ABC = [A, B, C]
    ans = []
    d = {"AB": (0, 1), "BC": (1, 2), "AC": (0, 2)}
    # print(ABC)
    for i in range(N):
        j, k = d[s[i]]
        if ABC[j] == ABC[k] == 0:
            no()
            return
        if ABC[j] == ABC[k] == 1:
            if i != N-1 and (j not in d[s[i+1]]):
                j, k = k, j
            ABC[j] += 1
            ABC[k] -= 1
            ans.append("ABC"[j])
        elif ABC[j] > ABC[k]:
            ABC[j] -= 1
            ABC[k] += 1
            ans.append("ABC"[k])
        else:
            ABC[j] += 1
            ABC[k] -= 1
            ans.append("ABC"[j])

    yes()
    for a in ans:
        print(a)
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    C = int(next(tokens))  # type: int
    s = [next(tokens) for _ in range(N)]  # type: "List[str]"
    solve(N, A, B, C, s)


if __name__ == '__main__':
    main()

from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def ceil(A, B):
    if A%B == 0:
        return A//B
    return A//B+1

def solve() -> Any:
    N = read_int()
    answer = 0
    # BxA, Bx, xA
    BxA = 0
    Bx = 0
    xA = 0
    for _ in range(N):
        S = input()
        for i in range(1, len(S)):
            if S[i-1] == 'A' and S[i] == 'B':
                answer += 1
        if S[0] == 'B' and S[-1] == 'A':
            BxA += 1
        elif S[0] == 'B':
            Bx += 1
        elif S[-1] == 'A':
            xA += 1
    if BxA:
        answer += BxA-1
        if Bx:
            answer += 1
            Bx -= 1
        if xA:
            answer += 1
            xA -= 1
    k = min(Bx, xA)
    Bx -= k
    xA -= k
    answer += k
    return answer


if __name__ == '__main__':
    print(solve())

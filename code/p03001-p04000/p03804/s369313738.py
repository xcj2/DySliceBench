from sys import stdin


def main() -> None:
    global N, M, A, B
    N = next_int()
    M = next_int()
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    ans = "No"
    for Ni in range(N):
        for Nj in range(N):
            if judge(Ni, Nj):
                ans = "Yes"
                break
        if ans == "Yes":
            break
    print(ans)


def judge(ni: int, nj: int) -> bool:
    for i in range(M):
        for j in range(M):
            if ni + i >= N or nj + j >= N:
                return False
            if B[i][j] != A[ni + i][nj + j]:
                return False
    return True


def next_int() -> int:
    return int(next_str())


def next_str() -> str:
    result = ""
    while True:
        tmp = stdin.read(1)
        if tmp.strip() != "":
            result += tmp
        elif tmp != '\r':
            break
    return result


if __name__ == '__main__':
    main()
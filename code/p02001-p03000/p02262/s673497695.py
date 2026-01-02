from typing import List, Tuple


def insertion_sort(A: List[int], n: int, g: int) -> int:
    count: int = 0
    for i in range(g, n):
        j = i - g
        while j >= 0 and A[j] > A[j + g]:
            A[j], A[j + g] = A[j + g], A[j]
            j -= g
            count += 1
    return count


def shell_sort(A: List[int], n: int) -> Tuple[int, List[int], int, List[int]]:
    cnt: int = 0
    G: List[int] = [1]
    h: int = 1

    while 3 * h + 1 < n:
        h = 3 * h + 1
        G.append(h)

    G.reverse()
    m = len(G)

    for i in range(m):
        count = insertion_sort(A, n, G[i])
        cnt += count

    return m, G, cnt, A


def main():
    n: int = int(input())
    A: List[int] = []
    for _ in range(n):
        A.append(int(input()))
    m, G, cnt, A_sorted = shell_sort(A[:], n)

    print(m)
    print(*G, sep=" ")
    print(cnt)
    print(*A_sorted, sep="\n")


if __name__ == "__main__":
    main()


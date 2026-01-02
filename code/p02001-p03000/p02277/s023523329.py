from collections import deque, defaultdict


def partition(A, p, r):
    x = int(A[r][1:])
    i = p - 1
    for j in range(p, r):
        if x >= int(A[j][1:]):
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]

    return i + 1


def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


def main():
    n = int(input())
    A = []
    d = defaultdict(deque)
    stable = True
    for i in range(n):
        inp = input().replace(" ", "")
        A.append(inp)
        d[int(inp[1:])].append(inp[0])
    quick_sort(A, 0, n-1)

    # stableかどうかを確認
    for a in A:
        tmp = d[int(a[1:])].popleft()
        if a[0] != tmp:
            stable = False

    if stable:
        print("Stable")

    else:
        print("Not stable")

    for a in A:
        print(a[0], a[1:])


if __name__ == "__main__":
    main()


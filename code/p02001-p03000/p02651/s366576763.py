# xor battle


def is_included(base, X):
    base.sort(reverse=True)
    V = X
    for x in base:
        V = min(V, V ^ x)
    return V


def solve():
    N = int(input())
    a = list(map(int, input().split()))[::-1]
    player = input()[::-1]
    basement = [0]
    for i in range(N):
        v = a[i]
        K = is_included(basement, v)
        if player[i] == "0":
            if K == 0:
                pass
            else:
                basement.append(K)
        else:
            if K == 0:
                pass
            else:
                return 1

    return 0


def main():
    T = int(input())
    for i in range(T):
        A = solve()
        print(A)
    return


if __name__ == "__main__":
    main()
import bisect

def main():
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    # print(A,B,C)

    A.sort()
    B.sort()
    C.sort()

    def get_a(b):
        p = bisect.bisect_left(A, b)
        return p

    def get_c(b):
        """ bより大きい数がいくつあるか
        """
        p = bisect.bisect_right(C, b)
        return N - p

    cnt = 0
    for bi in B:
        x = get_a(bi) * get_c(bi)
        cnt += x

    print(cnt)


if __name__ == "__main__":
    main()
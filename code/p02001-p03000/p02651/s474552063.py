def main():
    def sweep(arr):
        col = max(arr).bit_length()
        row = len(arr)

        rank = 0
        for c in range(col-1, -1, -1):
            piv = -1
            for r in range(rank, row):
                if arr[r] >> c & 1:
                    piv = r
            if piv == -1:
                continue

            arr[piv], arr[rank] = arr[rank], arr[piv]

            for r in range(row):
                if r == rank:
                    continue
                if arr[r] >> c & 1:
                    arr[r] ^= arr[rank]

            rank += 1

        return sorted(arr[:rank], reverse=True)

    def solve():
        N = int(input())
        A = list(map(int, input().split()))[::-1]
        S = input()[::-1]
        B0 = []

        for a, s in zip(A, S):
            if s == '1':
                for b0 in B0:
                    if a >> b0.bit_length()-1 & 1:
                        a ^= b0
                if a:
                    return 1
            else:
                B0 = sweep(B0+[a])

        return 0

    for _ in [0]*int(input()):
        print(solve())


if __name__ == '__main__':
    main()

def main():
    def warshall_floyd(d):
        for k in range(10):
            for i in range(10):
                for j in range(10):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        return d
    def flatten_list(l):
        for el in l:
            if isinstance(el, list):
                yield from flatten_list(el)
            else:
                yield el
    H, W = list(map(int, input().split()))
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    A = list(flatten_list(A))
    C = warshall_floyd(C)
    ans = 0
    for a in A:
        if a != -1:
            ans += C[a][1]
    print(ans)


if __name__ == '__main__':
    main()

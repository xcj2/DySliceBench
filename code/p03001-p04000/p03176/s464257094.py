def update(fen, pos, value):
    size = len(fen)
    while pos < size:
        fen[pos] = max(fen[pos], value)
        pos = pos + (pos & -pos)

def query(fen, pos):
    ret  = 0
    while pos > 0:
        ret = max(ret, fen[pos])
        pos = pos - (pos & -pos)
    return ret

def main():
    N = int(input())
    H = list(map(int, input().split()))
    B = list(map(int, input().split()))
    fen = list(0 for i in range(0,N + 2))
    ans = 0
    for i in range( 0, N ):
        ret = query(fen, H[i] - 1) + B[i]
        ans = max(ans, ret)
        update(fen, H[i], ret)
    print(ans)


if __name__ == "__main__":
    main()
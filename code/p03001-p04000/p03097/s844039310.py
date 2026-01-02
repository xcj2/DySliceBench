def rm_bit(n, i):
    return n // (2**(i+1)) * (2**i) + (n % (2**i))


def ins_bit(n, i, b):
    return n // (2**i) * (2**(i+1)) + (n % (2**i)) + b * (2**i)


def solve(N, A, B):
    if N == 1:
        return [A, B]
    idx = -1
    for i in range(N):
        if (A ^ B) & (2**i):
            idx = i
            break
    ra = rm_bit(A, idx)
    rb = rm_bit(B, idx)
    a = list(map(lambda x: ins_bit(x, idx, (A >> idx) & 1), solve(N-1, ra, ra ^ 1)))
    b = list(map(lambda x: ins_bit(x, idx, (B >> idx) & 1), solve(N-1, ra ^ 1, rb)))
    return a + b


def main():
    N, A, B = map(int, input().split())
    x = A ^ B
    cnt = 0
    for i in range(N):
        if x & (2**i):
            cnt += 1
    if cnt % 2 == 0:
        print("NO")
    else:
        print("YES")
        print(*solve(N, A, B))


if __name__ == "__main__":
    main()

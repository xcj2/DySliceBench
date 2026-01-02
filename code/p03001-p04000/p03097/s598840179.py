from collections import deque


def i_to_b(n, N):
    A = [0] * N
    for i in range(N):
        A[i] = (n // 2**i) % 2
    return A


def b_to_i(A):
    ret = 0
    for i in range(len(A)):
        ret += i**2*A[i]
    return ret


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
    binA = i_to_b(A, N)
    binB = i_to_b(B, N)
    if abs(sum(binA) - sum(binB)) % 2 == 0:
        print("NO")
        return
    print("YES")
    print(*solve(N, A, B))


if __name__ == "__main__":
    main()
